# AOSSIE

Read this whenever the contributor is with AOSSIE (Australian Open Source Software Innovation and Education). It overrides the generic template.

## Where AOSSIE code lives
AOSSIE projects span three GitHub organizations, and contributors often work across more than one (e.g. an AOSSIE GSoC project with repos in StabilityNexus):
- `AOSSIE-Org` (main space)
- `StabilityNexus` (blockchain projects)
- `DjedAlliance` (stablecoin projects)

Always run the collector with `--preset aossie`, which searches all three. Add `--repo owner/name` for anything elsewhere (e.g. a contributor's own repo agreed with mentors).

Older AOSSIE projects (roughly pre-2023) used GitLab (`gitlab.com/aossie`) and merge requests. The script does not cover GitLab; ask the contributor to list those manually.

## Where AOSSIE reports have been published
Ask the contributor which their mentors expect. Patterns seen in past AOSSIE reports:
- A file inside the project repo at `GSoC-<YEAR>/<ContributorName>-<Project>.md`, added via PR (e.g. `AOSSIE-Org/Perspective/GSoC-2025/ParagGhatage-Perspective.md`). Gives a stable, org-hosted link once merged.
- A standalone public repo with a README (e.g. `<user>/GSOC_2025_Report`), useful when the work spans several repos or orgs.
- A blog post (Medium etc.), common in earlier years.

If adding to the project repo, name the file following that pattern and offer a short PR description.

## Related org effort
There is an open feature request in `AOSSIE-Org/OrgExplorer` (issue #162, "Automated GSoC Final Report Generator for Contributors") proposing the same PR/issue collection inside OrgExplorer. Worth mentioning to mentors so the two efforts can share logic rather than duplicate it.

## AOSSIE report template
Mirrors the structure of well-received past AOSSIE reports. ✍️ = written by the contributor only (see SKILL.md).

```markdown
# Google Summer of Code <YEAR> – Final Report

**Project Title:** <title as on the GSoC dashboard>
**Organization:** AOSSIE
**Mentor(s):** <names>
**Contributor:** <name>
**GSoC Profile:** <https://summerofcode.withgoogle.com/programs/<year>/projects/<id>>
**GitHub Profile:** <https://github.com/<user>>
**Project Repo(s):** <links; include StabilityNexus / DjedAlliance repos if any>

---

## Introduction
<Factual: the problem the project tackles and what was proposed. Draw from the proposal / GSoC project page.>

## Goals of the Project
<Bulleted goals from the proposal. Mark each ✅ done / 🟡 partial / ❌ not done, based on the PR data and the contributor's confirmation.>

## Work Completed

### Pull Requests
<Merged PRs, newest first: "- [#N – title](url) – one-line description". Write the description from the PR title + body_excerpt in contributions.json; keep it factual.>

### Open Pull Requests
<With "Last GSoC commit: sha (date)" for each.>

### Features Added
<Group the PRs into user-visible features. Factual, no adjectives like "robust" or "seamless".>

### Issues Opened / Resolved
<From contributions.json, plus issues closed by the contributor's PRs if known.>

### Code Reviews
<PRs reviewed, if any.>

## Demo
- **Video Demo:** <link; ask the contributor. AOSSIE reports commonly include one>
- **Live Deployment:** <link, if deployed>

## Current State of the Project
- **Working features:** <factual>
- **Current limitations:** <factual; ask the contributor>

## Future Work / Next Steps
<From open PRs, open issues, and unfinished goals.>

## ✍️ Challenges Faced
<!-- Contributor writes this. What was hard, and how did you get past it? -->

## ✍️ Learnings
<!-- Contributor writes this. What did you learn, technically and about working in open source? -->

## Resources & References
<Repo, docs, proposal, blog posts.>

## ✍️ Summary of GSoC Contribution
<!-- Contributor writes this, in your own words: what you achieved and what it means for the project. -->

---
*Contributions data generated with the gsoc-final-report skill; personal sections written by the contributor.*
```

## AOSSIE-specific checks before handing over
- Repos in StabilityNexus / DjedAlliance included if the project touched them.
- Demo video and/or deployment link present (or explicitly marked as not applicable).
- Project title matches the GSoC dashboard.
- PR one-liners are factual, not promotional.
