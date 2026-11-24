# OGH: Local-First Live Streaming for Mobile and Desktop

## Background and Motivation

[OGH](https://github.com/AOSSIE-Org/Ogh) is AOSSIE's open-source, local-first streaming application, currently supporting Android capture and direct multistreaming. The goal is to bring an OBS/PRISM-style production experience to **Android, Windows and Linux (Wayland)** while keeping capture, composition, recording and outgoing streams on the user's device.

## Overview of Tasks

The linked issues define the scope in more detail. Contributors should consider the product as a whole, not treat each issue as an isolated task.

- **Desktop:** [shared application foundation](https://github.com/AOSSIE-Org/Ogh/issues/17), [Windows streaming](https://github.com/AOSSIE-Org/Ogh/issues/20) and [Linux Wayland streaming](https://github.com/AOSSIE-Org/Ogh/issues/21), including native capture and direct multistreaming.
- **Local production:** [scenes](https://github.com/AOSSIE-Org/Ogh/issues/18), [multi-source composition](https://github.com/AOSSIE-Org/Ogh/issues/22), [visual editing](https://github.com/AOSSIE-Org/Ogh/issues/23), [transitions](https://github.com/AOSSIE-Org/Ogh/issues/24), [audio mixing](https://github.com/AOSSIE-Org/Ogh/issues/27), [recording](https://github.com/AOSSIE-Org/Ogh/issues/19) and [low-end-device performance](https://github.com/AOSSIE-Org/Ogh/issues/28).
- **Unified chat:** [assess cross-platform chat](https://github.com/AOSSIE-Org/Ogh/issues/26). Implement locally only if the agreed platforms can be reliably supported on-device, otherwise use the cloud interface.
- **Cloud and exploration:** [design the provider-neutral interface and build a self-hosted reference service](https://github.com/AOSSIE-Org/Ogh/issues/25). Explore both providers that **implement features** and those that **supply compute/storage resources**, without deciding the architecture beforehand. Investigate platform APIs, restrictions and cloud-dependent features such as moderation, bots, analytics, captions/translation, AI summaries/clips, VTubing, archives and notifications. Explain feasibility, local/cloud placement and trade-offs.

## Pre-Evaluation Requirements (Before Proposal Submission)

### Early Streamer and Community Outreach (Preferred)

Contributors are strongly encouraged to contact streamers and streaming communities before finalizing their proposals. Ask about problems with current desktop and mobile streaming tools, missing features and requested improvements. Use genuine feedback to guide priorities for local production and cloud features.

Approach relevant, active streamers and communities with focused, individual questions rather than mass messages or spam. **Substantive response evidence is preferred, not required.** Useful responses identify concrete problems, requested features or actionable suggestions. Automated acknowledgments and vague replies such as "we will get back to you" are not meaningful feedback. No screenshots of outreach attempts are needed.

Build and demonstrate **working software**, not an architecture-only plan or mockup. The amount completed is **open-ended within OGH's vision and linked issues**. Complete as much of that defined scope as possible, including the full project if feasible. Do not leave features unfinished merely to reserve them for GSoC, and do not expand into unrelated product goals.

1. Deliver working **Android, Windows and Linux clients**. Provide an Android APK and Windows and Linux executables produced as **GitHub Actions artifacts**, following the existing build approach.
2. Demonstrate **real video and audio multistreaming to multiple destinations** and deploy the separately runnable, self-hosted cloud service on a machine or server. From OGH, open the provider connection, visit its site, sign in or sign up, authorize, return through the callback, discover and enable account capabilities, and **use the implemented cloud features during a live stream**. See [desktop #17](https://github.com/AOSSIE-Org/Ogh/issues/17), [Windows #20](https://github.com/AOSSIE-Org/Ogh/issues/20), [Linux #21](https://github.com/AOSSIE-Org/Ogh/issues/21) and [cloud #25](https://github.com/AOSSIE-Org/Ogh/issues/25).

**Showcase video:** Record one clear, narrated video showing Android, Windows and Linux in use, actual live streaming, the cloud server starting and deploying, connection and authorization, and working cloud features. Show other completed features as well, with real product behavior rather than simulated screens. Protect credentials.

**Progress sharing:** You may share short progress videos or tutorials in the project Discord channel while working.

## Requirements and Selection Criteria


- **Ownership and autonomy:** understand OGH's vision, take responsibility for the whole product experience, make well-reasoned decisions, work independently and communicate blockers early.
- **Quality and maintainability:** do not settle for code that merely “works once.” Prioritize clear architecture, careful implementation, usability and UI/UX details. Be able to explain what you built, why it works and its limitations.
- **Verification at each milestone:** test progressively, including real encoded output, permissions, device/platform behaviour, error paths, security and cleanup. Keep builds reproducible and CI meaningful. See [RTMP tests #16](https://github.com/AOSSIE-Org/Ogh/issues/16) and [cross-platform QA #29](https://github.com/AOSSIE-Org/Ogh/issues/29). Clearly disclose checks you could not run.
- **Progress communication:** communicate implementation progress, test results and blockers clearly throughout development.
- **Thoughtful exploration:** investigate and try feasible approaches before choosing cloud features or interfaces. AI assistance is acceptable, but understanding, validation and long-term maintainability remain your responsibility.

## What You Need to Do in Your Proposal

Explain **why, what and how** you built the project. Describe what already works, your exploration findings and architectural choices, tests performed, what remains, and a realistic, testable milestone plan for the coding period. If much or all of the defined scope is already complete, describe meaningful remaining work **within OGH's vision and linked issues**.

Briefly summarize any substantive streamer or community feedback and how it influenced your priorities. **Screenshots of specific responses are preferred**, showing the responder's identifiable email address or social handle and the platform. Redact unrelated sensitive information. Do not include generic acknowledgments or screenshots of outreach attempts. Receiving replies is not required.

## Resources

- [OGH repository and issues](https://github.com/AOSSIE-Org/Ogh)
- [Cloud interface and feature exploration](https://github.com/AOSSIE-Org/Ogh/issues/25)

## Mentors

- **GitHub:** [@imxade](https://github.com/imxade)
- **Discord:** @Rituraj

## Communication Channel

Discuss the idea, feasibility and progress in the [OGH Discord channel](https://discord.com/channels/1022871757289422898/1531495258217648268).
