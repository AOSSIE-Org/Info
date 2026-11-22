# Agent Platform: Reusable Chatbots for Projects and Communities

> **Required, living specification:** [Agent platform (chatbot.md)](https://github.com/imxade/idea-proposals/blob/master/ideas/chatbot.md). This is the source of truth for the current architecture, technical stack, platform behavior, deployment and acceptance requirements. Read it before implementation and revisit it as it changes. This idea describes the vision and contributor expectations, not a second technical specification.

## Background and Motivation

We want a reusable platform where people can create and configure their own bots, rather than building a separate chatbot for every project. For example, an AOSSIE project bot could help newcomers, answer recurring contributor questions from supplied documentation, handle several conversations at once, and forward unresolved matters to project maintainers through eligible chat channels. The same platform should support other communities and organizations through configuration, not hard-coded project workflows.

## Overview of Tasks

- Build a usable, multi-tenant chatbot application in which authorized owners create bots, configure their instructions and knowledge, manage connections, and change behavior without modifying application code.
- Support real two-way conversations across the initial **Discord and WhatsApp Business** integrations: a requester talks to the bot, a connected provider/maintainer can receive a handoff and respond, and the response can reach the original requester through an authorized route. Respect each platform's permissions and messaging policies.
- Handle **multiple eligible provider/staff destinations** without misrouting or leaking conversations, and **zero available provider destinations** without inventing an escalation, recipient or promised response. The bot should answer what it can from authorized context and clearly disclose what it cannot verify.
- Make the application useful beyond this example. Additional capabilities should be accessed through documented **external APIs and bot instructions**, not specialized built-in integrations such as a GitHub repository reader. Reuse existing platform/runtime capabilities rather than duplicate them.

## What You Need to Do During GSoC's Application Phase

Deliver a **working, independently deployable minimum MVP** using and validating the technology stack and Kubernetes deployment requirements in the [living specification](https://github.com/imxade/idea-proposals/blob/master/ideas/chatbot.md). It is an application to run and use, not a mockup or an architecture-only proposal.

1. Deploy the complete application, then create and configure a real logical bot through its dashboard, including instructions/context and authorized channel connections.
2. Connect and exercise that bot on **both Discord and WhatsApp Business** with real messages. Show a requester interacting with the bot, an eligible provider/maintainer receiving a question and replying, and the response reaching the requester. Demonstrate provider-initiated communication where the connected platform permits it.
3. Test the same interaction with **multiple provider routes** and with **no eligible provider route**. Verify correct routing, isolation and truthful no-handoff behavior, including failed or unavailable routes. Do not claim that unsupported WhatsApp groups or unsolicited messaging work.
4. Change bot configuration and demonstrate the resulting behavior. Verify durable conversations, authorization boundaries, error handling and recovery appropriate to the minimum baseline. Do not add task-specific GitHub readers or other bespoke tools merely for the demonstration.
5. Record **one comprehensive, clearly explained video** of the actual working product: bot creation/configuration, Discord and WhatsApp interactions in both directions, the multiple-provider and zero-provider cases, configuration changes, and the other completed features. Show observable results from the product itself, not simulated responses or unrelated tooling. Protect credentials and private conversations.

Creating external Discord/WhatsApp accounts and bot identities, completing provider onboarding, and granting server/group access for testing are responsibilities shared by the contributor and the relevant account/server owners. They are **not additional product features**. The platform still needs its own account, bot and connection-management functionality specified in the technical document.

The minimum MVP is **a floor, not a ceiling**. You may implement the full specification before submitting a proposal. Do not intentionally leave working features unfinished to reserve them for GSoC. **If ready early, we may start using this project for our own Discord bot to support contributors even before the GSoC period begins.**

## Requirements and Selection Criteria

- **Product ownership and judgment:** Understand the vision, act autonomously, notice gaps, make defensible trade-offs and be ready to explain architectural decisions and their limitations.
- **Correctness and quality:** Build maintainable, secure, usable software. Prefer integrating existing components over duplicating them. Avoid dead code, unnecessary abstractions and one-off demo hacks. Details and real user experience matter more than the volume of generated code.
- **Validate every milestone:** Test each meaningful change and integration as it is built, including real platform behavior, configuration, tenant/bot isolation, failures and recovery. Keep evidence of tests and clearly report unsupported behavior.
- **Use AI deliberately:** Tools such as ChatGPT can review changes, compare implementation against the specification and clarify design questions, but you remain responsible for understanding and verifying the result. When requesting technical guidance, share the [live specification](https://github.com/imxade/idea-proposals/blob/master/ideas/chatbot.md) so discussion is grounded in its latest requirements. Bring unresolved questions to the mentor discussion rather than guessing.
- **Communicate progress:** Share regular concise updates and short working demonstration videos throughout development, in addition to the required single comprehensive proposal video.

## What You Need to Do in Your Proposal

Explain the product's **why, what and how**, what you have actually implemented and tested, the important architectural choices and trade-offs, remaining risks, and a concrete, testable plan for anything still to be completed. If you exceed the minimum MVP or finish the full project before GSoC, describe that progress and propose meaningful further work instead of withholding features.

Develop in **one private GitHub repository** with clear setup, deployment and testing instructions. **When submitting your GSoC proposal, invite [@imxade](https://github.com/imxade) as a collaborator** and provide the private repository link, the comprehensive demonstration video link and the proposal itself. The video and repository are the primary evidence of working functionality. The proposal should make your decisions and verification easy to assess.

## Resources

- [GSoC idea template](../../Template.md)
- The required and regularly updated [agent-platform specification (chatbot.md)](https://github.com/imxade/idea-proposals/blob/master/ideas/chatbot.md)

## Mentors

- **GitHub:** [@imxade](https://github.com/imxade)
- **Discord:** @Rituraj

## Communication Channel

Discuss implementation progress and unresolved questions in the [AOSSIE Discord community](https://discord.gg/xnmAPS7zqB), coordinating the appropriate project discussion channel with the mentors.
