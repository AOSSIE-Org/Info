# Harbur: Production-Grade Collaboration and Self-Hosted CI/CD

## Background and Motivation

[Harbur](https://github.com/imxade/harbur) is a snapshot-based code collaboration platform intended to make version control approachable without Git's branch, rebase and conflict-resolution workflow. Users upload repository snapshots, review pull requests and diffs, and merge accepted work. Open PR diffs are recalculated against the current repository snapshot as the base changes. Preserve this deliberately simple model rather than recreating a Git remote.

Harbur is often seen as a **cool project rather than a production-grade platform**. The goal is to make it a credible, reliable and enjoyable choice for real projects, while retaining low operating costs, a stateless main application and user-controlled storage. Development is intended as a **separate FOSS project based on Harbur**, without directly modifying the existing codebase.

Harbur already has a working external deployment integration. [Nix Ship](https://github.com/imxade/nixship) can connect to a Harbur instance, consume immutable snapshots and deploy merged revisions. However, Nix Ship requires a self-hosted machine or server. Serverless and cloud deployment platforms may offer free tiers, managed builds, previews, scalability and other advantages. Supporting different choices and learning their real requirements is an important part of making Harbur useful in production.

## Overview of Tasks

This is an **open-ended production-adoption project**, not a limited checklist or an attempt to reproduce GitHub feature for feature. Start with actual user needs and the existing Harbur code. The following areas establish the direction and may be expanded as useful requirements are discovered.

- **Early platform outreach and integration research.** Contact relevant deployment, cloud and CI providers **before finalizing the detailed project proposal**. Explore Vercel, Netlify, AWS, Azure, GCP and other appropriate services. Ask whether they would support Harbur, what integration route they recommend, which changes to APIs, authentication, events, source metadata or deployment flows they require, and whether technical support, CI resources or credits are available. Record actual responses, unanswered inquiries and requested changes in the proposal. Use verified feedback to guide subsequent work and return to providers to validate implemented integrations, without inventing interest or waiting until implementation is complete.
- **Unified platform APIs.** Expose the same operations available in the UI through documented general-purpose APIs, including identity and access, workspace and repository management, file and snapshot upload/download, issues, discussions, PR diffs/reviews/merges, team settings, activity, CI/CD, deployments, artifacts and releases. Support browser users, scripts, applications and automation through the same authorization rules. No AI-specific API or protocol is needed.
- **Storage independence.** Keep Google Drive as the accessible default and explore an adapter interface for S3-compatible and self-hosted storage. Preserve the stateless main application and user ownership of data and costs.
- **Separate, durable, instance-wide CI/CD service.** Build a self-hostable service that connects **once to a Harbur instance**, not separately to each repository. It should receive workflow events from any repository on that instance, schedule and run jobs using connected self-hosted runners, retain necessary execution state, and report logs, results and checks to Harbur. Keep this long-running service separate from Harbur's stateless web application.
- **Familiar workflows, artifacts and releases.** Reuse `.github/workflows/` and GitHub Actions conventions where practical. Investigate [`act`](https://github.com/nektos/act) and other existing runner tooling rather than building an execution engine without need. Support access-controlled downloadable CI-generated artifacts, manual releases with downloadable assets, and releases published automatically by CI/CD pipelines with their generated assets attached.
- **Team and product experience.** Explore organizations, team membership, roles, permissions and activity history. Improve performance, onboarding, file browsing, search, navigation, accessibility, reviews, notifications, documentation, deployment and other everyday functionality that helps real users choose Harbur over established platforms. Do not restrict the work to the listed examples.
- **Authentication simplification only if complete.** Consider a database-free library such as Better Auth **only if it replaces all existing Google OAuth flows**, including sign-in, identity, sessions, owner/backup Drive consent, scopes and refresh-token handling, without retaining custom OAuth paths. Otherwise keep the working implementation unchanged.
- **Tests and maintainability.** Cover all deterministically testable API operations and system behavior, including permissions, success/failure paths, CI and integration flows, with end-to-end tests against a dedicated Google test account and Drive environment. Use Playwright for browser tests based on behavior rather than UI layout. Provide actionable errors, not silent fallbacks, unnecessary compatibility layers or dummy application data. Keep configurable values in environment variables or instance/repository settings rather than hard-coding them.

## User Expectations

A Harbur instance operator should be able to deploy the stateless platform with their chosen storage, **connect one durable self-hosted CI/CD service for the entire instance**, and run repository workflows without configuring a separate CI server for every repository. They should be able to understand job status, errors, configuration and resource usage.

A project user should be able to upload a snapshot, review its current-base diff, use issues and PRs, see relevant checks, inspect logs, download build artifacts, and publish or download releases. CI/CD pipelines should be able to produce release assets, and integrations should provide practical paths to deployment. These capabilities should also be accessible through ordinary APIs with the appropriate permissions.

The result must feel like a **production-usable product**, not a collection of isolated prototypes. Preserve Harbur's simple collaboration model and ensure features work together end to end.

## What You Need to Do During GSoC's Application Phase

Build and demonstrate a **working minimum MVP focused on the self-hosted CI/CD service and runners**, rather than a mockup or an architecture-only document.

1. **Inspect and run Harbur**, and examine its current integration APIs and workflow conventions. Reach out to relevant platforms early, before settling the integration requirements. Include what was proposed, actual replies or pending status, requested changes and the resulting plan in your proposal.
2. Build a **separately runnable, durable CI/CD service** and demonstrate the **one-time instance-level connection** to Harbur, including its configuration, authorization and successful connection verification. Connect at least one **self-hosted runner** and exercise a real repository workflow from `.github/workflows/`. A successful build and a deliberately failing run should produce meaningful statuses, logs and error output. Use a real execution path, not simulated job results.
3. Demonstrate an **end-to-end pipeline** from a Harbur repository snapshot through the runner and back to the user. Show a real downloadable generated artifact. Implement and demonstrate any further capabilities already completed, such as deployment or CI-created releases, rather than reserving them artificially for later.
4. Verify the essential authorization boundaries and basic recovery behavior of the service, including what happens when a job fails or the runner is unavailable. Supply reproducible setup and testing instructions.
5. Record **one short MVP showcase video** showing the self-hosted CI/CD server running, **how it is configured and connected to the Harbur instance**, the instance-level connection verification, a connected runner, a real workflow executing, its results and logs, and a generated artifact being downloaded. Demonstrate the actual connection and product behavior rather than slides, fake data or mock responses. Protect credentials.
6. Develop in **one private GitHub repository** with setup and testing instructions. **When submitting the GSoC proposal**, invite [@imxade](https://github.com/imxade) as a collaborator and include the private repository link and MVP showcase video.

**The MVP is a floor, not a ceiling.** You may implement more of the production platform, including the full idea, before applying. Do not intentionally hold back useful working functionality to leave work for the GSoC period.

## Requirements and Selection Criteria

- **Product ownership:** Understand Harbur's collaboration model and the reasons users choose mature alternatives. Explore genuine adoption gaps and make clear, defensible trade-offs rather than inventing problems or copying Git features.
- **Working software:** Deliver an independently deployable CI/CD service with actual self-hosted runner execution and observable end-to-end results. Value quality, usability and correctness over a large amount of unverified code.
- **Engineering quality:** Keep the main application stateless and the CI/CD service explicitly durable. Address least-privilege credentials, isolation of untrusted workflow code, error visibility, restart/retry behavior and realistic operating costs.
- **Integration judgment:** Research external services early. Distinguish native provider support from an API adapter, and explain what providers actually requested. Lack of a provider reply must not be presented as support.
- **Verification:** Test deterministic behavior, APIs, permissions, failures and recovery as work progresses. Prefer behavioral browser tests over brittle UI selectors. Use real test resources where needed and keep secrets out of source control.
- **Communication and understanding:** Explain decisions and limitations, report progress and demonstrate working increments. AI tools may help with implementation or review, but understanding and verifying the results remains your responsibility.

## What You Need to Do in Your Proposal

Explain the project's **why, what and how**, what you have already implemented and tested, the MVP showcase and deployment instructions, the user experience you aim to deliver, and a realistic plan for remaining production work. Include findings from early provider outreach, the **actual response or pending status for each platform**, any requested integration changes and how they affect the proposed design.

Describe the instance-wide CI/CD architecture, runner and workflow compatibility, artifact/release handling, API and storage plans, test evidence, constraints and trade-offs. If the MVP or larger scope is already complete, describe what additional meaningful improvements you would pursue instead of withholding features.

Submit the **private GitHub repository link**, access for [@imxade](https://github.com/imxade), and the **short MVP showcase video link** with the proposal.

## Resources

- [Harbur repository](https://github.com/imxade/harbur)
- [Nix Ship, an existing Harbur deployment integration](https://github.com/imxade/nixship)
- [act, a candidate GitHub Actions workflow executor](https://github.com/nektos/act)
- [GSoC idea template](../../Template.md)

## Mentors

- **GitHub:** [@imxade](https://github.com/imxade)
- **Discord:** @Rituraj

## Communication Channel

Discuss implementation progress and unresolved questions in the [AOSSIE Discord community](https://discord.gg/xnmAPS7zqB), coordinating the appropriate project discussion channel with the mentors.
