# Triageurs

To deal with the increased load of PRs and reported issues, AOSSIE is establishing a triage taskforce. 
Eligible contributors may be awarded the _triageur_ role, which allows them to help mentors and maintainers 
review PRs and issues.


## Eligibility to be a Triageur

To be awarded the role of triageur, you must satisfy all of the following:
* have submitted at least 1 non-AI-generated PR that got merged.
* have shown evidence that you are able to evaluate and give feedback humanly.

These are minimum eligibility requirements. They are necessary, but possibly not sufficient, at the discretion of admins.

## Responsibilities of a Triageur

As a triageur, you should, as frequently as possible, review the new issues and new PRs in the following orgs:
* [https://github.com/AOSSIE-Org](https://github.com/AOSSIE-Org)
* [https://github.com/StabilityNexus](https://github.com/StabilityNexus)
* [https://github.com/DjedAlliance](https://github.com/DjedAlliance)

For convenience, here is a list of links to the lists of open PRs and issues: 
* [Open PRs at AOSSIE](https://github.com/search?q=org%3AAOSSIE-Org++&type=pullrequests&state=open)
* [Open PRs at Stability Nexus](https://github.com/search?q=org%3AStabilityNexus++&type=pullrequests&state=open)
* [Open PRs at Djed Alliance](https://github.com/search?q=org%3ADjedAlliance++&type=pullrequests&state=open)
* [Open Issues at AOSSIE](https://github.com/search?q=org%3AAOSSIE-Org++&type=issues&state=open)
* [Open Issues at Stability Nexus](https://github.com/search?q=org%3AStabilityNexus++&type=issues&state=open)
* [Open Issues at Djed Alliance](https://github.com/search?q=org%3ADjedAlliance++&type=issues&state=open)

When you review a PR, do the following:
* If the PR is AI slop, close the PR, leaving a comment that AI slop is not acceptable
  and instructing the contributor to read our [AI Usage Policy](AI-UsagePolicy.md).
   * Not all AI-generated code is AI slop. Given the subjectivity of deciding whether AI-generated code is slop, 
     please judge responsibly.
* If the PR's description does not follow the PR template, close the PR and leave a comment asking
  the contributor to resubmit and follow the PR template.
* If the PR has been reviewed by CodeRabbit and the contributor has not addressed CodeRabbit's comments,
  submit a review requesting changes and asking the contributor to address CodeRabbit's comments.
* If the PR has no unadressed CodeRabbit comments, review the PR yourself.
* If you approve the PR and you deem the PR to be simple enough that it could be quickly merged by any maintainer or admin,
  send a message to the [channel of simple PRs ready to be merged](https://discord.gg/zJb7avQr8R) with a link to the PR.
* If you approve the PR and you deem the PR to require thorough further review by a maintainer of the respective project,
  inform the maintainer of the project by tagging him/her in the PR or by informing him in the respective project channel.
  If the maintainer is unreachable or inactive, send a message to the [channel of complex PRs ready for maintainer review](https://discord.gg/PXpfXtUAbH) with a link to the PR.

When you review an issue, do the following:
* If the issue is AI slop generated merely for the sake of getting assignments and increasing PR count,
  close the issue with a comment containing a link to our [AI Usage Policy](AI-UsagePolicy.md).
* If the issue is genuine and valuable, inform the maintainer of the project by tagging him/her in the PR
  or by informing him in the respective project channel.
  If the maintainer is unreachable or inactive, send a message to the [channel of valuable issues ready for assignment](https://discord.gg/ng4YwHSTYE) with a link to the issue.

Give higher priority to older PRs and issues.

Do not use AI to review issues. Do not use AI to review PRs. We already have CodeRabbit doing AI reviews. As a triageur, you are supposed to review PRs 100% humanly.

Do not abuse the powers of the triageur role. In particular, do not do any of the following (non-exhaustively):
* Do not close any PR or issue as a way of preventing other contributors from contributing.
* Do not collude with other contributors to prioritize their PRs and issues and make them go
  through triage more quickly or easily than others.

If you see any triage action that you consider to be wrong w.r.t. the instructions above, report it in the
[Wrong Triage Report Channel](https://discord.gg/ZAthYGDJPz).


## Applying to Become a Triageur

Admins may award the triageur role to any contributor that they deem to be eligible, capable and worthy.

If you believe that you qualify, apply by sending a message to the [Triageur Application Channel](https://discord.gg/nD86fyPeXh).
Your message should include your github username, a link to some of your human-made PRs and a brief paragraph describing how 
you are able to evaluate and give feedback humanly.
