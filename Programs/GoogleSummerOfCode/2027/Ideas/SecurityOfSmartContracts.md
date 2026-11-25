# Security of Smart Contracts

## Background and Motivation

LLMs are making it easy to find bugs in legacy smart contract code.
We have recently already created a skill for security reviews and used in our recent projects. But this was just the first step.

What else can we do to improve smart contract security for our own contracts and for others? This is what this idea is about.

Furthermore, traditionally, users without a background 
on software engineering had to rely exclusively on audits to know whether a smart contract they wanted to use was secure. Even if the smart contract's code was open-source, most users were unable to understand it and find security flaws on it.

This partially defeated one of the initial objectives of smart contracts: that users interacting with them would be able to do so without relying on third parties, because the smart contracts would do exactly what they were programmed to do. Because users cannot understand or detect problems in the code, they end up having to rely on auditing companies. Auditing companies became a third party. And, because audits are expensive, they end up becoming a barrier of entry for developers, and this partially defeats the objective of permissionlessness of blockchain technologies. Yes, anyone has permission to deploy a smart contract. But, for it to be adopted by users, it ends up requiring an expensive audit from a few auditing companies, which end up serving as stamps of approval and permission.

But now a new possibility exists: users may ask their 
own AI agents to inspect and explain smart contract code for them before they use it.

What can we do to make this even easier for users? Would better smart contract analysis skills aimed at general users help? Would a local static frontend with a bring-your-own-key approach allowing users to connect their AI and share the link to a smart contract repo or of a deployed contract in a blockchain explorer and get an analysis of the congracts help? 



## What you Need to Do During GSoC's Application Phase

If you would like to work on this idea, you need to some (though not necessarily all) of the following:

1. Submit PRs with improvements of our security review skill.    
  - Explain in the PR's description why your changes make the improvements better. This explanation should be in your own words, not AI generated. 
  - If you used AI to generate the improvements, please include in the PR description a transcript of the chat you had with the AI.

2. Find security issues in our own legacy contracts and submit issues or PRs to fix them.
  - Absolutely do **not** flood us with AI generated low value issues and PRs. We know that anyone can ask an AI to inspect a repo, look for issues and generate PRs. We could do that too and it would be easier for us to do it, than to review this done by others.
  - We are looking for contributors who can go beyond that, who are able to truly understand a codebase and decide which issues are most relevant and critical, who are able to discuss solutions with us properly. Think about a task that you care about and build a web app that uses an LLM to do this task for the user.

3. Look at our CI/CD workflows. Is there anything there that we could improve to increase security? If so, talk to us about it in Discord.
  - Again, anyone could easily ask an AI agent for suggestions, get hundreds of suggestions and forward them to us. Absolutely, do **not** do this. You are welcome to use AI for your own research, but only contact us with suggestions that you know are really good.
  - We know we could add dozens of workflow files to our repos, checking various things. But we also want to keep our CI/CD minimal and efficient, focused on what matters. So, don't just tell us to add yet another workflow file that provides only slight benefits. 

4. Develop a prototype of a frontend that analyses smart contracts for end users.
  - Fork this repo: TODO.
  - Develop your web app inside the `prototypes/<your-github-username>` folder inside this repo.
  - If you are using AI to generate your app (and you are welcome to do it), include in the `prototypes/<your-github-username>` folder:
    - have a `prototypes/<your-github-username>/prompts` folder containing markdown files with copies of the chat sessions you had with your AI agent.
    - Submit a pull request of your web app to AOSSIE's repo.
    - Configure your own fork to deploy your web app to GitHub pages.
    - Record a demo video showing your web app.


### Requirements and Selection Criteria

* As discussed above for items 1, 2 and 3, do not spam us with AI stuff that can be easily generated. Don't be just a mere "meat proxy" between us and your AI agent.
* For items 1, 2 and 3, what matters is quality, not quantity.
* Your prototype in item 4 above should be a client-side app, with no server dependency. The LLM used by it should be either a local LLM in the user's computer (e.g. ollama-based), or a browser-based LLM, or a cloud-based LLM (e.g. Claude, ChatGPT, ...). For cloud-based LLMs, the web app should allow the user to insert his/her own key. 



## What you Need to Do in Your Proposal

Your proposal needs to discuss:

* The "Why? What? How?" of everything you are proposing.
* What you have already completed in the application phase.
* What remains to be done during GSoC's coding period.


## Mentors

* Look for mentors with the role `@TODO` in our discord servers.


## Communication Channel

Join our Discord servers (https://discord.gg/xnmAPS7zqB and https://discord.gg/fuuWX4AbJt) and discuss this idea in TODO.
