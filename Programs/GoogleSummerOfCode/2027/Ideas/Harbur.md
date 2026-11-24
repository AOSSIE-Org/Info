# Harbur: Production-Grade Collaboration and Self-Hosted CI/CD

## Background and Motivation

[Harbur](https://github.com/imxade/harbur) is a snapshot-based code collaboration platform intended to make version control approachable without Git's branch, rebase and conflict-resolution workflow. Users upload repository snapshots, review pull requests and diffs, and merge accepted work. Open PR diffs are recalculated against the current repository snapshot as the base changes. Preserve this deliberately simple model rather than recreating a Git remote.

Harbur is often seen as a **cool project rather than a production-grade platform**. The goal is to make it a credible, reliable and enjoyable choice for real projects, while retaining low operating costs, a stateless main application and user-controlled storage. Development is intended as a **separate FOSS project based on Harbur**, without directly modifying the existing codebase.

Harbur already has a working external deployment integration. [Nix Ship](https://github.com/imxade/nixship) can connect to a Harbur instance, consume immutable snapshots and deploy merged revisions. However, Nix Ship requires a self-hosted machine or server. Serverless and cloud deployment platforms may offer free tiers, managed builds, previews, scalability and other advantages. Supporting different choices and learning their real requirements is an important part of making Harbur useful in production.

## Overview of Tasks

This is an **open-ended production-adoption project within the scope described here**, not a limited checklist or an attempt to reproduce GitHub feature for feature. Start with actual user needs and the existing Harbur code. Explore additional requirements only when they directly advance this production-readiness vision.

- **Early platform outreach and integration research.** Contact relevant deployment, cloud and CI providers **before finalizing the detailed project proposal**. Explore Vercel, Netlify, AWS, Azure, GCP and other appropriate services. Ask whether they would support Harbur, what integration route they recommend, which changes to APIs, authentication, events, source metadata or deployment flows they require, and whether technical support, CI resources or credits are available. Record actual responses, unanswered inquiries and requested changes in the proposal. Use verified feedback to guide subsequent work and return to providers to validate implemented integrations, without inventing interest or waiting until implementation is complete.
- **Unified platform APIs.** Expose the same operations available in the UI through documented general-purpose APIs, including identity and access, workspace and repository management, file and snapshot upload/download, issues, discussions, PR diffs/reviews/merges, team settings, activity, CI/CD, deployments, artifacts and releases. Support browser users, scripts, applications and automation through the same authorization rules. No AI-specific API or protocol is needed.
- **Storage independence.** Keep Google Drive as the accessible default and explore an adapter interface for S3-compatible and self-hosted storage. Preserve the stateless main application and user ownership of data and costs.
- **CI/CD with existing self-hosted runners.** Support real workflows using maintained open-source runners or other suitable CI systems. Explore **Forgejo Runner**, **Gitea Runner** and alternatives without assuming any is compatible out of the box. Prefer adapting Harbur to work with existing tools where practical, but keep the integration approach open. Trigger CI through Harbur request events, such as creating or merging a pull request. Harbur itself should remain client-driven and stateless, without a resident job runner or scheduler. Aim for shared instance-level integration rather than requiring each repository to configure a separate execution service.
- **Familiar workflows, artifacts and releases.** Preserve `.github/workflows/` and familiar GitHub Actions conventions where practical, based on demonstrated compatibility with the selected CI tools. Support access-controlled downloadable CI-generated artifacts, manual releases with downloadable assets, and releases published automatically by CI/CD pipelines with their generated assets attached.
- **Team and product experience.** Explore organizations, team membership, roles, permissions and activity history. Improve performance, onboarding, file browsing, search, navigation, accessibility, reviews, notifications, documentation, deployment and other everyday functionality that helps real users choose Harbur over established platforms. Do not restrict the work to the listed examples.
- **Authentication simplification only if complete.** Consider a database-free library such as Better Auth **only if it replaces all existing Google OAuth flows**, including sign-in, identity, sessions, owner/backup Drive consent, scopes and refresh-token handling, without retaining custom OAuth paths. Otherwise keep the working implementation unchanged.
- **Tests and maintainability.** Cover all deterministically testable API operations and system behavior, including permissions, success/failure paths, CI and integration flows, with end-to-end tests against a dedicated Google test account and Drive environment. Use Playwright for browser tests based on behavior rather than UI layout. Provide actionable errors, not silent fallbacks, unnecessary compatibility layers or dummy application data. Keep configurable values in environment variables or instance/repository settings rather than hard-coding them.

## User Expectations

A Harbur instance operator should be able to use a compatible existing self-hosted runner or CI system for workflows across the Harbur instance without setting up separate execution infrastructure for each repository. Harbur should display relevant job status, errors and results while retaining its lightweight, client-driven architecture.

A project user should be able to upload a snapshot, review its current-base diff, use issues and PRs, see relevant checks, inspect logs, download build artifacts, and publish or download releases. CI/CD pipelines should be able to produce release assets, and integrations should provide practical paths to deployment. These capabilities should also be accessible through ordinary APIs with the appropriate permissions.

The result must feel like a **production-usable product**, not a collection of isolated prototypes. Preserve Harbur's simple collaboration model and ensure features work together end to end.

## Pre-Evaluation Requirements (Before Proposal Submission)

Build and demonstrate **working Harbur CI/CD integration with at least one existing open-source self-hosted runner**, rather than a mockup or architecture-only proposal. The amount completed is **open-ended within the production-readiness vision above**. Implement as much of that scope as possible, including the full project if feasible. This demonstration is essential evidence of working software, not a limit on what can be finished. Do not withhold features to reserve them for GSoC or pursue unrelated product goals.

1. **Inspect and run Harbur**, examining its existing integration APIs and workflow conventions. **Contact relevant deployment, cloud and CI providers before submitting the proposal.** Document who was contacted, their actual replies or pending status, recommended integration paths, requested changes and how these findings shape project priorities. Do not assume a reply or commitment.
2. **Research and test existing self-hosted runners**, selecting any suitable option, including the suggested projects if they fit. Demonstrate the **actual connection and configuration with Harbur**, ideally reusable across repositories on the instance. Run a real repository workflow, using `.github/workflows/` where supported, and show both successful and deliberately failing executions with real statuses, logs and errors. You may host the runner on an **Oracle Cloud Always Free VPS**, subject to availability and eligibility, or on another suitable machine. Do not assume a runner integrates with Harbur without additional work.
3. Demonstrate a pipeline from a Harbur repository snapshot through the runner and back to the user, including a genuine downloadable generated artifact. Also show any further completed capabilities, such as CI-created releases or deployment.
4. Verify essential authorization and recovery behavior, including job failure and runner unavailability. Explain the tested runner's capabilities and limitations and provide reproducible setup and testing instructions.

**Showcase video:** Record one short video showing the selected **existing self-hosted runner** operating, **how it is connected to Harbur**, real workflow execution including success and failure, the resulting statuses and logs, and a generated artifact being downloaded. Include other completed functionality where practical. Show the actual product, not slides, dummy data or mock responses. Protect credentials.

**Progress sharing:** You may share short progress videos in the project Discord channel while working.

## Requirements and Selection Criteria

- **Product ownership:** Understand Harbur's collaboration model and the reasons users choose mature alternatives. Explore genuine adoption gaps and make clear, defensible trade-offs rather than inventing problems or copying Git features.
- **Working software:** Demonstrate a tested integration with an existing self-hosted runner and observable end-to-end results. Value quality, usability and correctness over a large amount of unverified code.
- **Engineering quality:** Preserve Harbur's client-driven, stateless application model with no resident job runner or background CI polling. Start workflows from actual Harbur events. If scheduled workflows are supported, rely on scheduling capabilities of the chosen CI system rather than assuming a standalone runner schedules YAML by itself. Prefer existing runner capabilities and changes on Harbur's side where practical, without prescribing a fixed integration design. Address credentials, runner isolation, error visibility, recovery and realistic costs.
- **Integration judgment:** **Early provider outreach is a pre-evaluation priority** because the findings should define substantial implementation work. Distinguish native support from an API adapter and explain requested changes. Evaluate the quality of outreach and technical planning, not the number of replies received. Never present a lack of response as support.
- **Verification:** Test deterministic behavior, APIs, permissions, failures and recovery as work progresses. Prefer behavioral browser tests over brittle UI selectors. Use real test resources where needed and keep secrets out of source control.
- **Communication and understanding:** Explain decisions and limitations, report progress and demonstrate working increments. AI tools may help with implementation or review, but understanding and verifying the results remains your responsibility.

## What You Need to Do in Your Proposal

Explain the project's **why, what and how**, what you have already implemented and tested, the intended user experience, deployment instructions, and a realistic plan for remaining production work. Include **early platform outreach findings**, each provider's actual response or pending status, requested integration changes, and how these define and prioritize implementation work.

Describe the runner options researched, the real integration tested, workflow compatibility and limitations, how the chosen approach fits Harbur's stateless model, artifact/release handling, test evidence, constraints and trade-offs. If much or all of the defined scope is complete, identify meaningful remaining improvements **within the production-readiness vision above**.

## Resources

- [Harbur repository](https://github.com/imxade/harbur)
- [Nix Ship, an existing Harbur deployment integration](https://github.com/imxade/nixship)
- [Forgejo Runner and Forgejo Actions documentation](https://forgejo.org/docs/latest/user/actions/overview/)
- [Gitea Runner documentation](https://docs.gitea.com/runner/)
- [Oracle Cloud Always Free resources, an optional runner testing host](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm)
- [GSoC idea template](../../Template.md)

## Mentors

- **GitHub:** [@imxade](https://github.com/imxade)
- **Discord:** @Rituraj

## Communication Channel

Discuss implementation progress and unresolved questions in the [AOSSIE Discord community](https://discord.gg/xnmAPS7zqB), coordinating the appropriate project discussion channel with the mentors.
