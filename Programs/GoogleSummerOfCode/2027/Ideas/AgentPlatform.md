# Agent Platform: Reusable Chatbots for Projects and Communities

> **Required, living specification:** [Agent platform](https://github.com/imxade/idea-proposals/blob/master/ideas/chatbot.md). This is the source of truth for the current architecture, technical stack, platform behavior, deployment and acceptance requirements. Read it before implementation and revisit it as it changes. This idea describes the vision and contributor expectations, not a second technical specification.

## Background and Motivation

We want a reusable platform where people can create and configure their own bots, rather than building a separate chatbot for every project. For example, an AOSSIE project bot could help newcomers, answer recurring contributor questions from supplied documentation, handle several conversations at once, and forward unresolved matters to project maintainers through eligible chat channels. The same platform should support other communities and organizations through configuration, not hard-coded project workflows.

## Overview of Tasks

- Build a usable, multi-tenant chatbot application in which authorized owners create bots, configure their instructions and knowledge, manage connections, and change behavior without modifying application code.
- Support real two-way conversations across the initial **Discord and WhatsApp Business** integrations: a requester talks to the bot, a connected provider/maintainer can receive a handoff and respond, and the response can reach the original requester through an authorized route. Respect each platform's permissions and messaging policies.
- Handle **multiple eligible provider/staff destinations** without misrouting or leaking conversations, and **zero available provider destinations** without inventing an escalation, recipient or promised response. The bot should answer what it can from authorized context and clearly disclose what it cannot verify.
- Make the application useful beyond this example. Additional capabilities should be accessed through documented **external APIs and bot instructions**, not specialized built-in integrations such as a GitHub repository reader. Reuse existing platform/runtime capabilities rather than duplicate them.

## Pre-Evaluation Requirements (Before Proposal Submission)

### Early User and Business Outreach

Before finalizing the proposal, study the platform's vision and identify potential users who could benefit from configurable AI agents.

- **Who to contact:** Relevant small businesses, customer support teams, appointment-based services, booking providers, community managers and other organizations.
- **What to ask:** Current problems, repetitive workflows, desired features and interest in trying or supporting the platform. Possible use cases include customer support, booking and appointment assistance, voice interaction and prompt-configured agents.
- **How to approach them:** Focus on personalized outreach to people or organizations with a relevant need and a reasonable likelihood of responding. Avoid mass messaging and spam.
- **Feedback:** Receiving replies is not required. Substantive feedback includes specific problems, feature requests, integration guidance or concrete interest in piloting or supporting the product. Automated acknowledgments and vague promises to follow up do not count as meaningful responses.

Use the findings to identify realistic audiences and guide priorities within the project's existing vision and specification.

Build and demonstrate a **working, independently deployable application** using the technology stack and Kubernetes deployment requirements in the [living specification](https://github.com/imxade/idea-proposals/blob/master/ideas/chatbot.md). The amount completed is **open-ended within that specification and the vision above**. Implement as much of the defined scope as possible, including the full project if feasible. Do not stop at an artificial minimum, leave working features unfinished for GSoC, or add unrelated features. The result must be usable software, not a mockup or architecture-only proposal.

1. **Preferably deploy the complete application using Oracle Cloud Always Free resources**.
   - **First preference:** An OKE Basic cluster with Always Free-eligible worker nodes.
   - **Second preference:** An Always Free ARM VM running K3s if OKE Basic is not feasible.
   - Check account eligibility, regional availability, resource limits and potential charges while preserving the Kubernetes-only deployment requirement.
   - Then create and configure a real logical bot through its dashboard, including instructions, context and authorized channel connections.
2. Exercise **both Discord and WhatsApp Business** with real messages.
   - Show a requester interacting with the bot.
   - Show an eligible provider or maintainer receiving a handoff and replying, and the response reaching the requester.
   - Demonstrate provider-initiated communication where the connected platform permits it.
3. Test provider routing.
   - Test multiple eligible provider routes and no eligible provider route, including failed or unavailable destinations.
   - Verify correct routing, isolation and truthful no-handoff behavior.
   - Do not claim that unsupported WhatsApp groups or unsolicited messaging work.
4. Change bot configuration and demonstrate the resulting behavior.
   - Verify durable conversations, authorization boundaries, error handling and recovery.
   - Do not add task-specific GitHub readers or other bespoke tools merely for the demonstration.

Creating external Discord and WhatsApp accounts, completing provider onboarding, and granting server or group access for testing involve the relevant account owners. These are **not additional product features**. The application still needs its own account, bot and connection-management functionality from the specification.

**Showcase video:** Record one comprehensive, clearly explained video of the **actual implemented product**. Show:
- Bot creation and configuration.
- Two-way Discord and WhatsApp interactions.
- Multiple-provider and zero-provider cases.
- Configuration changes and other completed functionality.

Show observable results rather than simulated responses or unrelated tooling. Protect credentials and private conversations.

**Progress sharing:** You may share short progress videos in the project Discord channel while working. If ready early, the platform may be used for an AOSSIE Discord bot before the GSoC period begins.

## Requirements and Selection Criteria

- **Product ownership and judgment:** Understand the vision, act autonomously, notice gaps, make defensible trade-offs and be ready to explain architectural decisions and their limitations.
- **Correctness and quality:** Build maintainable, secure, usable software. Prefer integrating existing components over duplicating them. Avoid dead code, unnecessary abstractions and one-off demo hacks. Details and real user experience matter more than the volume of generated code.
- **Validate every milestone:** Test each meaningful change and integration as it is built, including real platform behavior, configuration, tenant/bot isolation, failures and recovery. Keep evidence of tests and clearly report unsupported behavior.
- **Use AI deliberately:** Tools such as ChatGPT can review changes, compare implementation against the specification and clarify design questions, but you remain responsible for understanding and verifying the result. When requesting technical guidance, share the [live specification](https://github.com/imxade/idea-proposals/blob/master/ideas/chatbot.md) so discussion is grounded in its latest requirements. Bring unresolved questions to the mentor discussion rather than guessing.
- **Communicate progress:** Share concise updates, raise unresolved questions and explain completed work as development progresses.

## What You Need to Do in Your Proposal

Explain the product's **why, what and how**, what you have actually implemented and tested, the important architectural choices and trade-offs, remaining risks, and a concrete, testable plan for anything still to be completed. If much or all of the defined scope is complete before GSoC, describe that progress and propose meaningful further work **within the linked specification and this idea's vision**. Make your decisions and verification easy to assess.

Include early outreach findings in the proposal:
- Briefly identify the audiences contacted and any relevant findings. Explain how the feedback informed your priorities.
- **If substantive responses were received, include screenshots showing the feedback, the responder's identifiable email address or social handle, and the platform.** Redact unrelated sensitive information.
- Do not include screenshots of outreach attempts or generic acknowledgments. If nobody responded, simply state that.

## Resources

- [GSoC idea template](../../Template.md)
- The required and regularly updated [agent-platform specification (chatbot.md)](https://github.com/imxade/idea-proposals/blob/master/ideas/chatbot.md)

## Mentors

- **GitHub:** [@imxade](https://github.com/imxade)
- **Discord:** @Rituraj

## Communication Channel

Discuss implementation progress and unresolved questions in the [AOSSIE Discord community](https://discord.gg/xnmAPS7zqB), coordinating the appropriate project discussion channel with the mentors.
