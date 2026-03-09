# Setting up Local Agentic Coding Setup


If you've been following the AI coding assistant space, you already know that tools like **Claude Code** are genuinely impressive. The way it reasons through codebases, handles multi-step tasks, and operates autonomously is hard to beat. But there's a real catch — that performance comes at a steep token-usage cost.

For heavy daily usage — refactoring large files, running long agentic loops, working across multiple projects — Claude Code's bills can add up surprisingly fast. And beyond cost, there's a lock-in problem: Claude Code keeps you tightly within the Anthropic model ecosystem. You get one vendor, one pricing structure, and no real flexibility to route your workloads to cheaper or even better-fit models.

This guide is about fixing that. Here's how to build a fully local agentic coding environment using **VS Code**, **Ollama**, and your choice of coding agent — giving you performance, flexibility, and cost control all at once.

---

## 1. VS Code: Your IDE

[Visual Studio Code](https://code.visualstudio.com/) needs little introduction — it's the most widely used code editor in the world for good reason. It's fast, endlessly extensible, and has a rich ecosystem of extensions that makes it the perfect foundation for an AI-augmented local setup.

### Installing VS Code

Head to [code.visualstudio.com](https://code.visualstudio.com/) and download the installer for your OS. It's available for Windows, macOS, and Linux.

Once installed, the real power comes from the extensions marketplace — which is exactly where the coding agents in this guide live.

---

## 2. Ollama: A Home for Models That Don't Cost a Dime

[Ollama](https://ollama.com/) is an optimized local inference engine that brings powerful open-source models directly onto your machine. It handles all the complexity of model loading, memory management, and hardware acceleration — you just pull a model and run it.

Ollama supports both **CPU and GPU inference**, though GPU is strongly preferred for speed and responsiveness. Whether you're on a MacBook with Apple Silicon, a Linux box with an NVIDIA card, or a Windows machine, Ollama will use whatever hardware you have and make the most of it.

For those who want to run large models but don't have the hardware for it, Ollama has also rolled out **cloud inference** — letting you run models on their servers, with some limitations on usage and model availability. It's a nice middle ground between fully local and fully cloud-dependent.

### Installing Ollama

**Windows:**

```powershell
irm https://ollama.com/install.ps1 | iex
```

**macOS / Linux:**

```bash
curl -fsSL https://ollama.com/install.sh | sh
# or
brew install ollama
```

### Running Local Models

Browse the full model library at [ollama.com/library](https://ollama.com/library) — it includes Llama 3, Mistral, Gemma, Qwen, DeepSeek Coder, and many more. To download and run any model:

```bash
ollama pull <model_name>
ollama run <model_name>
```

Models are cached locally after the first pull, so subsequent launches are instant.

---

## 3. Coding Agents

With VS Code and Ollama in place, you now need an agent layer — something that can take a task, reason through your codebase, and actually get things done. There are two strong options here, and they serve slightly different workflows.

### Continue

[Continue](https://continue.dev/) is a VS Code extension that brings AI chat, inline edits, and agentic task execution directly into your editor. It's deeply integrated into the VS Code experience — you work from the sidebar, use it inline as you type, and never have to leave your editor to interact with the model.

#### Setting Up Continue with Ollama

1. Install the Continue extension from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Continue.continue)
2. Once installed, open Continue from the **sidebar panel**
3. Go to **Settings**, then click on **Models**, then hit the **Add Model** button (the `+` icon)
4. Select **Ollama** as the provider, and leave the model set to **Autodetect** — this will automatically pick up any models you have downloaded locally via Ollama
5. Hit **Connect**, then go back

Continue will now route your conversations and agent tasks through your local Ollama models. No API key, no usage tracking, no cost.

---

### Opencode

[Opencode](https://opencode.ai/) takes a different approach — it's a terminal-based AI coding agent, similar in spirit to Claude Code, but without the vendor lock-in. Instead of being confined to one model provider, Opencode integrates with OpenAI, Anthropic, Google, Mistral, Groq, and more. You can mix and match: use a powerful paid model for complex reasoning tasks, and fall back to a free or local model for everything else.

For a fully cost-free setup, Opencode pairs naturally with Ollama — running capable open-source models on your own hardware with no API fees.

#### Installing Opencode

Run any one of the following:

```bash
curl -fsSL https://opencode.ai/install | bash
```

Or via a package manager of your choice:

```bash
npm i -g opencode-ai
bun add -g opencode-ai
brew install anomalyco/tap/opencode
paru -S opencode
```

Once installed, launch it from any project directory:

```bash
opencode
```

#### Connecting Opencode with Ollama

To launch Opencode with Ollama as the backend:

```bash
ollama launch opencode
```

From there, you can choose your model interactively. Or to launch directly with a specific model:

```bash
ollama launch opencode --model <model_name>
```

You can also setup Opencode via their extension from the marketplace [Opencode Extension](https://marketplace.visualstudio.com/items?itemName=sst-dev.opencode)


---

## Conclusion

That's the full stack — **VS Code** as your editor, **Ollama** running models locally, and either **Continue** or **Opencode** (or both) as your coding agent layer. Heavy tasks, long sessions, late-night refactors — none of it touches your API wallet.

---

### What's Next

There are a few natural upgrades that take this setup from functional to genuinely powerful.

**Add agent permissions for trusted commands.** By default, agentic tools will ask for your approval before running shell commands — which is safe, but gets tedious fast for routine operations. Most agent config files (like Opencode's `config.json` or Continue's settings) let you whitelist specific commands that can run without a confirmation prompt. Git operations are the obvious first candidate: `git status`, `git add`, `git commit`, `git push`, `git checkout` and similar commands are low-risk and get triggered constantly during normal coding sessions. Whitelisting them keeps the agent flow uninterrupted without meaningfully increasing your exposure.

---

###  Pro Tips: Saving Tokens Without Sacrificing Quality

If you're occasionally reaching for a powerful proprietary model (GPT-4o, Claude Sonnet, etc.) for complex tasks, token costs can still creep up even in an otherwise local setup. Here's a workflow that keeps those costs minimal:

> **Plan with the smart model. Execute with the local one.**

For any non-trivial task — a new feature, a refactor, an architectural change — start by asking your proprietary model to **plan the full implementation** and save that plan to a `.md` file in your project (e.g., `docs/plans/add-auth.md`). Ask it to be thorough: what files to create or modify, what the logic should look like, what edge cases to handle, what the step-by-step order of operations is.

Once you have that plan, **switch to a local Ollama model** (or a free tier model in Continue/Opencode) and point it at the plan file. Local models are more than capable of following a clear, structured spec — they just struggle with the open-ended reasoning that produced it. This way, the expensive model does a single focused burst of thinking, and the free model does all the repetitive execution work.

It's a small workflow shift that can cut your proprietary model usage by 60–80% on complex tasks, while keeping quality high where it matters.
