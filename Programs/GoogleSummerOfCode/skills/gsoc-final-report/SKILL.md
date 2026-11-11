---
name: gsoc-final-report
description: Build a Google Summer of Code (GSoC) final report / final work product submission. Automates the bureaucratic parts (pulling every PR, issue, review and commit from GitHub for the coding period, sorting them into merged / open / closed, noting the last GSoC commit on unfinished PRs, adding stats and links) and leaves the summary of achievements and personal experience for the contributor to write in their own words. Use this skill whenever someone mentions a GSoC final report, final evaluation, work product submission, "list of my PRs for GSoC", wrapping up Summer of Code, or a similar end-of-program report (GSoC, Outreachy, LFX, Season of Docs), even if they only ask to "list my contributions" for the program.
---

# GSoC Final Report

Google requires every GSoC contributor to submit one stable link describing their work. The link should make it easy to see what was done, what state it is in, what is left, and where the code lives. Much of that is mechanical (listing PRs, statuses, links), and that is what this skill automates.

**The one rule that matters most:** the *Summary of achievements* and *My experience* sections are written by the contributor, not by you. Mentors asked for this explicitly: the facts can be automated, the reflection cannot. Do not draft, "suggest", or pre-fill those sections, even if asked to "just write something". You may (a) give the contributor the guiding questions in `references/report_template.md`, (b) once they have written their text, fix typos and grammar while keeping their wording and voice, and (c) point out facts their text contradicts. If they push back, explain briefly that their org asked for this part in their own words, and that it is what reviewers and future employers actually read.

## Workflow

### 1. Gather inputs (ask only for what is missing)

- GitHub username
- Organization and/or specific repos worked on (e.g. `--org sympy` or `--repo owner/name`; several allowed)
- Coding period start and end dates (default: the official coding period for that year; confirm with the contributor, since extended timelines are common)
- GSoC project title and project page URL (`https://summerofcode.withgoogle.com/programs/<year>/projects/<id>`)
- Mentors' names
- Where the report will live (GitHub Gist, README, blog, Discourse post, wiki, mailing list). This decides output format; default to Markdown.
- Any org-specific report rules. If the org has published guidelines, follow them over the default template.

**Org-specific references:** if the contributor is with **AOSSIE**, read `references/aossie.md` now. It covers AOSSIE's three GitHub orgs, where AOSSIE reports are published, and the AOSSIE report template, and it overrides the generic template below.

Use the ask_user_input tool or a single short message for the missing items. Do not ask for anything the conversation already contains.

### 2. Collect contributions automatically

Run the bundled script. It needs only the Python standard library.

```bash
python scripts/collect_contributions.py \
  --user <github-username> \
  --org <org> [--org <org2>] [--repo owner/name ...] [--preset aossie] \
  --start YYYY-MM-DD --end YYYY-MM-DD \
  --out /home/claude/gsoc_data
```

- It reads a token from `GITHUB_TOKEN` / `GH_TOKEN` if set. Without a token it still works for public repos but GitHub's search API allows only ~10 searches/minute, so the script sleeps and retries. If it is rate-limited badly, ask the contributor for a read-only token (no scopes needed for public repos) or run it locally themselves.
- Output: `contributions.json` (raw data) and `contributions.md` (ready-to-paste tables).
- What it finds: PRs authored (created or merged in the period), their status, additions/deletions, the last commit on or before the end date for PRs that are still open (Google asks for this), issues opened, and PRs reviewed.
- If the network is blocked, tell the contributor and give them the exact command to run locally, then continue once they paste back the JSON or Markdown.

### 3. Review the data with the contributor

Show a short summary (counts by status, repos touched) and ask them to:
- remove anything unrelated to GSoC (e.g. PRs from another project in the same org)
- add work the script cannot see: GitLab/other hosts, design docs, benchmarks, blog posts, talks, work in a personal repo outside the org (rerun with `--repo`)
- mark which PRs are the "core" deliverables vs. smaller fixes

### 4. Assemble the report

Use the org's template if there is one (e.g. `references/aossie.md`), otherwise `references/report_template.md`. `contributions.json` includes a `body_excerpt` for each PR; use it with the title to write factual one-line PR descriptions. Fill in every factual section from the data. Write the factual descriptions plainly (one line per PR is enough; reuse the PR title, don't embellish). For PRs that will continue after GSoC, state the last GSoC commit SHA with a link.

Leave the personal sections (summary of achievements, experience, and, in templates that have them, challenges and learnings) as clearly marked placeholders containing the guiding questions, unless the contributor has already given you their own text, in which case insert it as written (light proofreading only).

Also fill the "Current state" and "Future work" sections only from facts: open PRs, open issues, unchecked items from the proposal if the contributor shared it. If unsure, leave a placeholder and ask.

### 5. Deliver

- Default: a Markdown file the contributor can paste into a Gist/README/Discourse post. Present it as a file.
- Remind them, briefly: the link must be stable and public; discuss it with mentors before submitting; it can be edited on the dashboard until the deadline.
- Check for the common mistakes in `references/past_report_patterns.md` before handing over.

## Files

- `scripts/collect_contributions.py`: GitHub data collection (stdlib only)
- `references/report_template.md`: generic report skeleton and guiding questions for personal sections
- `references/aossie.md`: AOSSIE orgs, publishing conventions, and template
- `references/past_report_patterns.md`: what good past reports did, and common mistakes. Read it when assembling the report.
