# OGH: Local-First Live Streaming for Mobile and Desktop

## Background and Motivation

[OGH](https://github.com/AOSSIE-Org/Ogh) is AOSSIE's open-source, local-first streaming application, currently supporting Android capture and direct multistreaming. The goal is to bring an OBS/PRISM-style production experience to **Android, Windows and Linux (Wayland)** while keeping capture, composition, recording and outgoing streams on the user's device.

## Overview of Tasks

The linked issues define the scope in more detail. Contributors should consider the product as a whole, not treat each issue as an isolated task.

- **Desktop:** [shared application foundation](https://github.com/AOSSIE-Org/Ogh/issues/17), [Windows streaming](https://github.com/AOSSIE-Org/Ogh/issues/20) and [Linux Wayland streaming](https://github.com/AOSSIE-Org/Ogh/issues/21), including native capture and direct multistreaming.
- **Local production:** [scenes](https://github.com/AOSSIE-Org/Ogh/issues/18), [multi-source composition](https://github.com/AOSSIE-Org/Ogh/issues/22), [visual editing](https://github.com/AOSSIE-Org/Ogh/issues/23), [transitions](https://github.com/AOSSIE-Org/Ogh/issues/24), [audio mixing](https://github.com/AOSSIE-Org/Ogh/issues/27), [recording](https://github.com/AOSSIE-Org/Ogh/issues/19) and [low-end-device performance](https://github.com/AOSSIE-Org/Ogh/issues/28).
- **Unified chat:** [assess cross-platform chat](https://github.com/AOSSIE-Org/Ogh/issues/26). Implement locally only if the agreed platforms can be reliably supported on-device, otherwise use the cloud interface.
- **Cloud and exploration:** [design the provider-neutral interface and build a self-hosted reference service](https://github.com/AOSSIE-Org/Ogh/issues/25). Explore both providers that **implement features** and those that **supply compute/storage resources**, without deciding the architecture beforehand. Investigate platform APIs, restrictions and cloud-dependent features such as moderation, bots, analytics, captions/translation, AI summaries/clips, VTubing, archives and notifications. Explain feasibility, local/cloud placement and trade-offs.

## What You Need to Do During GSoC's Application Phase

Build and demonstrate a **working MVP**, not just a design or a mocked interface:

1. Prepare **one private GitHub repository** containing the OGH application and the **separately runnable, self-hosted cloud-service project**, with concise build and deployment instructions.
2. Deliver working **Android, Windows and Linux clients**. Provide an Android APK and Windows/Linux executables produced as **GitHub Actions artifacts**, following the existing build approach.
3. Demonstrate **real video/audio multistreaming to multiple destinations** and deploy the cloud service on a machine/server. From OGH, open the provider connection, visit its site, sign in/sign up, authorize, return through the callback, discover and enable account capabilities, and **use the implemented cloud features during a live stream**. See [desktop #17](https://github.com/AOSSIE-Org/Ogh/issues/17), [Windows #20](https://github.com/AOSSIE-Org/Ogh/issues/20), [Linux #21](https://github.com/AOSSIE-Org/Ogh/issues/21) and [cloud #25](https://github.com/AOSSIE-Org/Ogh/issues/25).
4. Record **one clear, narrated walkthrough video** showing Android, Windows and Linux in use, actual live streaming, cloud-server startup/deployment, connection and authorization, and working feature usage rather than simulated screens.
5. **When submitting the GSoC proposal (not before), invite [@imxade](https://github.com/imxade) as a collaborator** to the private repository. Include its link and the single video link in your proposal.

The MVP is a **minimum, not a limit**. You may complete additional issues, or even the full scope, before applying.

### Requirements and Selection Criteria

- **Ownership and autonomy:** understand OGH's vision, take responsibility for the whole product experience, make well-reasoned decisions, work independently and communicate blockers early.
- **Quality and maintainability:** do not settle for code that merely “works once.” Prioritize clear architecture, careful implementation, usability and UI/UX details. Be able to explain what you built, why it works and its limitations.
- **Verification at each milestone:** test progressively, including real encoded output, permissions, device/platform behaviour, error paths, security and cleanup. Keep builds reproducible and CI meaningful. See [RTMP tests #16](https://github.com/AOSSIE-Org/Ogh/issues/16) and [cross-platform QA #29](https://github.com/AOSSIE-Org/Ogh/issues/29). Clearly disclose checks you could not run.
- **Progress communication:** regularly record short demos or tutorials showing features, usage and test results, in addition to the required proposal video.
- **Thoughtful exploration:** investigate and try feasible approaches before choosing cloud features or interfaces. AI assistance is acceptable, but understanding, validation and long-term maintainability remain your responsibility.

## What You Need to Do in Your Proposal

Explain **why, what and how** you built the project. Describe what already works, your exploration findings and architectural choices, what remains, and a realistic, testable milestone plan for the coding period. If you have progressed beyond the MVP, describe the additional work and how you would use the remaining GSoC period. Include the private repository link, narrated demonstration video and build/deployment instructions.

## Resources

- [OGH repository and issues](https://github.com/AOSSIE-Org/Ogh)
- [Cloud interface and feature exploration](https://github.com/AOSSIE-Org/Ogh/issues/25)

## Mentors

- **GitHub:** [@imxade](https://github.com/imxade)
- **Discord:** @Rituraj

## Communication Channel

Discuss the idea, feasibility and progress in the [OGH Discord channel](https://discord.com/channels/1022871757289422898/1531495258217648268).
