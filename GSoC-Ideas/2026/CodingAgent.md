# CodingAgent: Open-Source CLI AI Coding Assistant

## Background and Motivation
Our motivation for building CodingAgent is that there is still no truly good open-source coding agent that works like the best closed-source tools such as Codex, Antigravity, or Claude Code.
We’ve used all of these extensively and we are frustrated that I can’t plug my favorite open-source models into a comparable, powerful agent experience.
Key capabilities like robust persistent memory, solid MCP integration, and local vector-based storage for long-term context are either missing or poorly implemented in current open-source options.
We want to change that by creating an agent that treats memory and context as first-class citizens, not afterthoughts.
My goal is to build something that operates at the level of serious engineering workflows, not just toy demos.
In essence, We want to create the “clawdbot for coding” — a scalable, developer-first AI coding agent that is fully open, extensible, and production-ready.

## Overview of Tasks
* Setup TypeScript CLI skeleton with commander + multi-LLM config
* Build agent loop: goal → plan → file/shell tools → memory compaction
* Test end-to-end: codingagi "create hello.ts"

Candidates are expected to refine these tasks in their GSoC proposals.

## Requirements

* Model Agnostic - Works seamlessly with any LLM (Claude, OpenAI, Ollama, Kimi) via simple config, not locked to one provider
* Local vector store + structured notes that survive sessions and context limits (beats all open source agents)
* Reliable goal→plan→execute→observe cycle with MCP tools, file editing, and shell execution at Claude Code/Antigravity level (This point is very important to be explained in detail in the proposal, there are many complex plans in the market which are actually not suitable for this project, i want something straight forward, amazing and simple to use for the end user.) 

## Resources

* Learn how memory layer is used here: https://github.com/opencode-ai/opencode
* excellent for CLI structure and local model integration: https://github.com/google-gemini/gemini-cli
* Full video tutorial building CLI agents with MCP, memory, and multi-agent workflows: https://www.youtube.com/watch?v=eNbza7cBL0U
* Loves Antigravity's autonomy/browser integration but warns of destructive ops, security gaps, and enterprise compliance risks vs Claude's safer design: https://blog.getbind.co/antigravity-vs-claude-code-which-is-better-for-developers/

## Mentors

* GitHub: [coderwithsense](https://github.com/coderwithsense/); Discord: rmvfsx

## Communication Channel

Join our Discord servers (https://discord.gg/xnmAPS7zqB and https://discord.gg/fuuWX4AbJt) and discuss this idea in [general](https://discord.com/channels/1022871757289422898/1180497744666837003).
