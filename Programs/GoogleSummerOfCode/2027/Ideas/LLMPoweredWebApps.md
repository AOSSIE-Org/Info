# LLM-Powered Web Apps

## Background and Motivation

LLMs are revolutionizing the way we use computers and the web, 
to the point that it now feels almost pointless to develop web apps, 
because users will rather use an LLM-based AI than visit and use a web app.

A web app that just does something that a user could easily do by prompting an LLM is unlikely to be used.
A web app that is just a wrapper for an LLM, taking input from the user and then prompting an LLM and feeding the LLM's output back to the user is also unlikely to be used, because the user could just use the LLM directly.

However, there are situations where a web app that handles the interaction between the user and an LLM remains valuable. These may include (non-exhaustively):
* Tasks where the user needs to write a complex prompt and the user does not know how to write this complex prompt. So, a web app that has a complex built-in prompt can be valuable to users.
* Tasks where users need to write a complex prompt and, even though users might know how to write this prompt, it would be tedious and time-consuming for them to do it. Visiting and using a web app that has a built-in prompt could take him a few seconds, whereas using an LLM to do the same thing could take hours.
* Tasks where the output needs to be post-processed to be more useful (e.g. format data in a specific way, create charts of a specific type, ...). Although LLM-based AIs that can use tools can be instructed to post-process their output, prompting them to post-process their output in a specific way can be tedious and time-consuming.
* Tasks that are potentially useful for a large number of users. At a societal level, it may be more efficient for all those users to use a web app than for each of them to keep prompting their own AIs over and over again to do the same thing.
* Tasks where interacting by clicking, dragging, drawing... is easier than interacting via text prompting. 

## What you Need to Do During GSoC's Application Phase

If you would like to work on this idea, you need to:

1. Think about a task that you care about and build a web app that uses an LLM to do this task for the user.
2. Fork this repo: TODO.
3. Develop your web app inside the `gsoc-applications/<your-github-username>` folder inside this repo.
4. If you are using AI to generate your app (and you are welcome to do it), include in the `gsoc-applications/<your-github-username>` folder:
  - a `Prompt.md` file, containing a copy of the initial prompt that you gave to your AI agent.
  - a `Chat.md` file, containing a copy of the full conversation you had with your AI agent.
5. Submit a pull request of your web app to AOSSIE's repo.
6. Configure your own fork to deploy your web app to GitHub pages.
7. Record a demo video showing your web app.


### Requirements and Selection Criteria

* Your web app should be a client-side app, with no server dependency.
* The LLM used by your app should be either a local LLM in the user's computer (e.g. ollama-based), or a browser-based LLM, or a cloud-based LLM (e.g. Claude, ChatGTP, ...). For cloud-based LLMs, the web app should allow the user to insert his/her own key. 
  - Ideally, your web app should support multiple types of LLMs, among the types described above. For instance, it could support a browser-based model for users who don't want to bother about local models or subscriptions, a local model for users who care about privacy, and a cloud-based model for users who need more powerful models.
* Your web app should be minimalistic, clean and with very intuitive UI/UX. (Otherwise the user would just use an LLM directly.)
* Your web app should have good design and layout quality. You need to be attentive to details. Your web app should not contain defects, typos, grammar errors, window resizing issues, and so on.
* If you used AI to generate your app, your initial prompt and your chat should be of good quality. Your initial prompt should show that you had a clear idea of what you wanted and that you dind't just rely on the AI to generate something for you. Your conversation should show that you identified issues in the initially generated app and that you guided your AI agent effectively and efficiently to fix those issues.
* Your web app should be as complete as possible. We are looking for contributors who finish what they start. Completion includes (non-exhaustively): having a logo, having favicons, complying with SEO best practices, complying with best practices to make your web app AI ready, having a terms of use file and a privacy file, having a footer with information about the project, about AOSSIE and about AOSSIE's social accounts, having a social share button, having a donate button, having a good readme file according to AOSSIE's standards and describing the "why? what? how?" of your project...
  - AOSSIE has template repos that help with many of these completion requirements. Some of the requirements are already done and others are clearly marked as TODO. Therefore, we encouraged you to use our templates.
* Apps that relate to themes in which AOSSIE has been active before are preferred.
* We value apps that address real user needs and that are innovative.

## What you Need to Do in Your Proposal

Your proposal needs to discuss:

* The "Why? What? How?" of the web app you developed in the application phase.
* What you have already completed of your web app in the application phase.
* What remains to be done in your web app during GSoC's coding period.
* If applicable, the reasons why the app was not completed during the application phase.
  - We do not want you to leave your app unfinished just to get a GSoC spot to finish it.
* What you are going to do in the coding period besides the web app that you developed in the application phase.
  - Thanks to the speed of software development powered by AI, it is very probable that you can complete your web app during the application phase or within a few weeks of the coding period. If that's the case, what do you propose to do with the remaining time in your coding period? 


## Mentors

* Look for mentors with the role `@TODO` in our discord servers.

## Communication Channel

Join our Discord servers (https://discord.gg/xnmAPS7zqB and https://discord.gg/fuuWX4AbJt) and discuss this idea in TODO.
