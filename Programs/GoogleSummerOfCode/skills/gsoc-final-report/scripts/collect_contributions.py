#!/usr/bin/env python3
"""Collect a contributor's GitHub activity for a GSoC coding period.

Stdlib only. Writes contributions.json and contributions.md to --out.

Example:
  python collect_contributions.py --user alice --org sympy \
      --start 2026-06-02 --end 2026-09-01 --out ./gsoc_data
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.github.com"

# Org presets: GitHub spaces an org's GSoC projects live in.
PRESETS = {
    "aossie": ["AOSSIE-Org", "StabilityNexus", "DjedAlliance"],
}


def get_token():
    for var in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(var):
            return os.environ[var]
    if shutil.which("gh"):
        try:
            out = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10)
            if out.returncode == 0 and out.stdout.strip():
                return out.stdout.strip()
        except Exception:
            pass
    return None


TOKEN = get_token()
CORE_EXHAUSTED = False  # set when the non-search API quota is gone for a long time


class RateLimited(Exception):
    pass


def request(url, retries=6):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "gsoc-final-report-skill"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code in (403, 429):
                reset = e.headers.get("X-RateLimit-Reset")
                retry_after = e.headers.get("Retry-After")
                wait = int(retry_after) if retry_after else (max(int(reset) - int(time.time()), 1) if reset else 15)
                if wait > 120 and e.headers.get("X-RateLimit-Remaining") == "0":
                    raise RateLimited(f"quota resets in {wait // 60} min")
                wait = min(wait + 1, 70)
                print(f"  rate limited, waiting {wait}s (set GITHUB_TOKEN to avoid this)", file=sys.stderr)
                time.sleep(wait)
                continue
            if e.code == 404:
                return None
            if e.code == 422:
                print(f"  GitHub rejected query (422): {url}", file=sys.stderr)
                return None
            raise
        except urllib.error.URLError as e:
            if attempt == retries - 1:
                sys.exit(f"Network error reaching GitHub: {e}. Run this script on your own machine instead.")
            time.sleep(3)
    sys.exit("Gave up after repeated rate limiting. Set GITHUB_TOKEN and retry.")


def detail(url):
    """Non-search API call that degrades gracefully when the hourly quota is gone."""
    global CORE_EXHAUSTED
    if CORE_EXHAUSTED:
        return None
    try:
        return request(url)
    except RateLimited as e:
        CORE_EXHAUSTED = True
        print(f"  GitHub API quota exhausted ({e}); skipping +/- stats and last-commit lookup. "
              "Set GITHUB_TOKEN and rerun for full detail.", file=sys.stderr)
        return None


def search(query):
    items, page = [], 1
    while page <= 10:
        url = f"{API}/search/issues?" + urllib.parse.urlencode({"q": query, "per_page": 100, "page": page})
        try:
            data = request(url)
        except RateLimited as e:
            sys.exit(f"Search quota exhausted ({e}). Set GITHUB_TOKEN and retry.")
        if not data:
            break
        items.extend(data.get("items", []))
        if len(data.get("items", [])) < 100:
            break
        page += 1
        if not TOKEN:
            time.sleep(6)
    return items


def body_excerpt(body, limit=300):
    """First meaningful lines of a PR description, to help write one-line summaries."""
    if not body:
        return ""
    lines = []
    for ln in body.splitlines():
        ln = ln.strip()
        if not ln or ln.startswith(("#", "<!--", "- [ ]", "- [x]", "|", "```")):
            continue
        lines.append(ln)
        if sum(len(x) for x in lines) > limit:
            break
    return " ".join(lines)[:limit]


def repo_of(item):
    # repository_url: https://api.github.com/repos/owner/name
    return "/".join(item["repository_url"].split("/")[-2:])


def scopes(args):
    s = [f"org:{o}" for o in args.org] + [f"repo:{r}" for r in args.repo]
    return s or [""]


def collect(args):
    rng = f"{args.start}..{args.end}"
    prs, issues, reviews = {}, {}, {}

    for sc in scopes(args):
        for q in (f"is:pr author:{args.user} created:{rng} {sc}",
                  f"is:pr author:{args.user} merged:{rng} {sc}"):
            print(f"search: {q}", file=sys.stderr)
            for it in search(q):
                prs[it["html_url"]] = it
        q = f"is:issue author:{args.user} created:{rng} {sc}"
        print(f"search: {q}", file=sys.stderr)
        for it in search(q):
            issues[it["html_url"]] = it
        if not args.no_reviews:
            q = f"is:pr reviewed-by:{args.user} -author:{args.user} updated:{rng} {sc}"
            print(f"search: {q}", file=sys.stderr)
            for it in search(q):
                reviews[it["html_url"]] = it

    pr_rows = []
    for url, it in prs.items():
        repo = repo_of(it)
        num = it["number"]
        info = detail(f"{API}/repos/{repo}/pulls/{num}") or {}
        merged_at = info.get("merged_at") or (it.get("pull_request") or {}).get("merged_at")
        state = "merged" if merged_at else ("open" if it["state"] == "open" else "closed")
        if (info.get("draft") or it.get("draft")) and state == "open":
            state = "draft"
        row = {
            "repo": repo, "number": num, "title": it["title"], "url": url, "state": state,
            "created_at": it["created_at"][:10], "merged_at": (merged_at or "")[:10] or None,
            "closed_at": (it.get("closed_at") or "")[:10] or None,
            "additions": info.get("additions"), "deletions": info.get("deletions"),
            "changed_files": info.get("changed_files"), "commits": info.get("commits"),
            "labels": [l["name"] for l in it.get("labels", [])],
            "body_excerpt": body_excerpt(it.get("body")),
            "last_gsoc_commit": None,
        }
        if state in ("open", "draft"):
            commits = detail(f"{API}/repos/{repo}/pulls/{num}/commits?per_page=100") or []
            before = [c for c in commits
                      if (c["commit"]["committer"]["date"] or "")[:10] <= args.end]
            if before:
                c = before[-1]
                row["last_gsoc_commit"] = {"sha": c["sha"], "url": c["html_url"],
                                           "date": c["commit"]["committer"]["date"][:10]}
            row["commits_after_end"] = len(commits) - len(before)
        pr_rows.append(row)

    issue_rows = [{"repo": repo_of(it), "number": it["number"], "title": it["title"],
                   "url": it["html_url"], "state": it["state"],
                   "created_at": it["created_at"][:10]} for it in issues.values()]
    review_rows = [{"repo": repo_of(it), "number": it["number"], "title": it["title"],
                    "url": it["html_url"], "author": it["user"]["login"]} for it in reviews.values()]

    key = lambda r: (r["repo"], r["created_at"] if "created_at" in r else "", r["number"])
    return {
        "user": args.user, "orgs": args.org, "repos": args.repo,
        "period": {"start": args.start, "end": args.end},
        "pull_requests": sorted(pr_rows, key=key),
        "issues": sorted(issue_rows, key=key),
        "reviews": sorted(review_rows, key=lambda r: (r["repo"], r["number"])),
    }


def md_escape(s):
    return s.replace("|", "\\|")


def to_markdown(d):
    prs = d["pull_requests"]
    out = [f"<!-- Generated by gsoc-final-report skill for @{d['user']}, "
           f"{d['period']['start']} to {d['period']['end']}. Review before publishing. -->", ""]

    groups = [("Merged pull requests", ["merged"]),
              ("Open pull requests (work continuing after GSoC)", ["open", "draft"]),
              ("Closed / unmerged pull requests", ["closed"])]
    for title, states in groups:
        rows = [p for p in prs if p["state"] in states]
        if not rows:
            continue
        out += [f"### {title}", ""]
        if "open" in states:
            out += ["| Repo | PR | Title | Status | Last GSoC commit |", "|---|---|---|---|---|"]
            for p in rows:
                lc = p["last_gsoc_commit"]
                lcs = f"[`{lc['sha'][:7]}`]({lc['url']}) ({lc['date']})" if lc else "<!-- add last GSoC commit -->"
                out.append(f"| {p['repo']} | [#{p['number']}]({p['url']}) | {md_escape(p['title'])} "
                           f"| {p['state']} | {lcs} |")
        elif "merged" in states:
            out += ["| Repo | PR | Title | Merged | +/- |", "|---|---|---|---|---|"]
            for p in rows:
                diff = f"+{p['additions']}/-{p['deletions']}" if p["additions"] is not None else ""
                out.append(f"| {p['repo']} | [#{p['number']}]({p['url']}) | {md_escape(p['title'])} "
                           f"| {p['merged_at']} | {diff} |")
        else:
            out += ["| Repo | PR | Title | Closed | Reason |", "|---|---|---|---|---|"]
            for p in rows:
                out.append(f"| {p['repo']} | [#{p['number']}]({p['url']}) | {md_escape(p['title'])} "
                           f"| {p['closed_at']} | <!-- why? --> |")
        out.append("")

    if d["issues"]:
        out += ["### Issues opened", "", "| Repo | Issue | Title | State |", "|---|---|---|---|"]
        for i in d["issues"]:
            out.append(f"| {i['repo']} | [#{i['number']}]({i['url']}) | {md_escape(i['title'])} | {i['state']} |")
        out.append("")

    if d["reviews"]:
        out += ["### Code reviews", ""]
        for r in d["reviews"]:
            out.append(f"- [{r['repo']}#{r['number']}]({r['url']}): {md_escape(r['title'])} (by @{r['author']})")
        out.append("")

    merged = [p for p in prs if p["state"] == "merged"]
    adds = sum(p["additions"] or 0 for p in prs)
    dels = sum(p["deletions"] or 0 for p in prs)
    line_stat = "n/a (rerun with GITHUB_TOKEN)" if d.get("details_incomplete") else f"+{adds} / -{dels}"
    repos = sorted({p["repo"] for p in prs} | {i["repo"] for i in d["issues"]})
    out += ["### Stats", "",
            f"- Pull requests: {len(prs)} total, {len(merged)} merged, "
            f"{sum(p['state'] in ('open', 'draft') for p in prs)} open, "
            f"{sum(p['state'] == 'closed' for p in prs)} closed",
            f"- Lines changed across all PRs: {line_stat}",
            f"- Issues opened: {len(d['issues'])}",
            f"- PRs reviewed: {len(d['reviews'])}",
            f"- Repositories: {', '.join(repos) if repos else 'none'}", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--user", required=True)
    ap.add_argument("--org", action="append", default=[])
    ap.add_argument("--preset", choices=sorted(PRESETS), help="add an org's known GitHub spaces, e.g. aossie")
    ap.add_argument("--repo", action="append", default=[], help="owner/name; repeatable")
    ap.add_argument("--start", required=True, help="YYYY-MM-DD")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD")
    ap.add_argument("--out", default="./gsoc_data")
    ap.add_argument("--no-reviews", action="store_true", help="skip the reviewed-by search")
    args = ap.parse_args()
    if args.preset:
        args.org = list(dict.fromkeys(args.org + PRESETS[args.preset]))

    if not args.org and not args.repo:
        print("warning: no --org/--repo given; searching all of GitHub for this user", file=sys.stderr)
    if not TOKEN:
        print("note: no GITHUB_TOKEN found; unauthenticated search is slow (~10 queries/min)", file=sys.stderr)

    data = collect(args)
    data["details_incomplete"] = CORE_EXHAUSTED
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "contributions.json").write_text(json.dumps(data, indent=2))
    (out / "contributions.md").write_text(to_markdown(data))
    print(f"Wrote {out/'contributions.json'} and {out/'contributions.md'}: "
          f"{len(data['pull_requests'])} PRs, {len(data['issues'])} issues, {len(data['reviews'])} reviews")


if __name__ == "__main__":
    main()
