# What past GSoC final reports have in common

Compiled from Google's Work Product Submission Guidelines and published final reports / org instructions (e.g. OSGeo's yearly packaging instructions, Xapian's wiki reports, Gist- and README-based reports on GitHub).

## Google's baseline requirements
- One stable, public link. It is published in the GSoC archive, so it should be representative.
- It must be easy to identify what *you* did, without the reader digging through repo history.
- If the work is complete, a reader should be able to use it. If not, it must be clear what remains.
- Link to the commits / PRs and repos you worked on, and to your GSoC project page.
- If a PR will keep receiving work after GSoC, note the last commit made during GSoC.
- A single detailed PR is acceptable if it covers all the work; a dedicated GSoC repo should get a detailed README.
- Discuss the link with mentors before final evaluation.

## Sections orgs commonly ask for
- Title, org, mentors, project page link
- Abstract / overview
- State of the project *before* GSoC (OSGeo asks for this explicitly)
- What was added during GSoC, with links
- Current state, and how to test/use it ("please test my code following these instructions")
- Potential future work / remaining tasks
- Merged work and not-yet-merged work listed separately (Xapian asks for this)
- For research-like work (benchmarks, evaluations): approach, datasets, results, analysis

## Formats that work
- GitHub Gist (popular; stable URL, renders Markdown)
- README in a dedicated repo
- Blog post or org blog (e.g. blogs.python-gsoc.org)
- Org Discourse/mailing-list post (OSGeo uses this for URL stability)
- Org wiki page

## Common mistakes to check for before handing over
- Linking a fork's branch instead of the upstream PR.
- Open PRs without the last-GSoC-commit note.
- Including PRs from before the coding period or unrelated to the project (community bonding work can be included if labelled as such).
- Private links (Google Docs with restricted access, private repos).
- Personal sections written by AI. Mentors notice, and orgs may ask for these in the contributor's own words.
- No instructions for trying the work.
- Using a link that will change (e.g. a branch HEAD) as the submission URL.
