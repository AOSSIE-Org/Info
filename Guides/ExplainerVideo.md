# AOSSIE Explainer Video Production Guide

A practical, step-by-step handbook for open-source contributors to produce high-quality **Explainer Videos** for AOSSIE projects.

---

## 1. Overview & Objective

An **Explainer Video** is an instructional product tour designed to help developers, users, and prospective contributors understand what your project is, how it works, and how it solves real problems.

Unlike a high-energy teaser, an explainer is methodical, grounded, and educational. It acts as a **guided product walkthrough**: it respects the viewer's time by proving that the software works through live interface interactions.

### Core Principles:
* **Real Product UI is Mandatory**: At least **60% of the total runtime** must feature the live application, web dashboard, CLI terminal, or repository outputs. Generic AI stock visuals (floating abstract 3D shapes, corporate handshakes) are strictly prohibited.
* **Feature Demonstrations**: Focus deeply on **2 to 3 core workflows** rather than rushing through an exhaustive list of every button.
* **Guided Narration & Subtitles**: A clear, natural voiceover guides the viewer through what is happening on screen, accompanied by synchronized captions.

---

## 2. Duration Contract

| Parameter | Specification | Notes |
| :--- | :--- | :--- |
| **Recommended Length** | **60 to 90 seconds** | Ideal length to demonstrate 2–3 workflows without losing viewer attention. |
| **Hard Maximum Cap** | **120 seconds** (2 minutes) | Videos must never exceed 120 seconds under any circumstances. |
| **Bumper Inclusion** | **Included in runtime** | Total time includes the official 2–3s AOSSIE intro bumper and closing outro card. |

> [!IMPORTANT]
> **Plan Around the Bumpers**  
> Because the official AOSSIE intro (2–3 seconds) and closing outro card (3–5 seconds) are required, aim for your core walkthrough footage to last **50 to 75 seconds**. This guarantees that the final rendered video comfortably respects the 60–90 second recommendation and stays well below the 120-second hard ceiling.

---

## 3. Toolset & Production Options

Contributors have the flexibility to choose the workflow and software that best suits their setup. You do not need expensive commercial licenses to produce an excellent explainer.

### Option A — [CapCut](https://www.capcut.com/) (Recommended for Hands-On Video Editing)
* **Overview**: A versatile, free multi-track editor available for Desktop (Windows/macOS), Web, and Mobile.
* **Key Advantages for Explainers**:
  * **Auto-Captions**: Generates synchronized subtitles from your voiceover with one click, drastically improving accessibility.
  * **Built-in Voiceover Recording**: Record clean narration directly over your timeline with background noise reduction.
  * **Callouts & Zoom Effects**: Easily add arrows, highlight boxes, and smooth zoom-ins to guide viewers' eyes to important UI buttons.
  * **Audio Ducking**: Automatically lowers background music levels when voiceover narration is speaking.
  * **Watermark-Free Export**: Supports crisp 1080p 60fps H.264 MP4 exports with zero watermarks on standard free exports; verify your available export settings and stick to eligible free assets/features, as export options and watermark behavior can vary by platform (desktop vs. mobile/web), project assets, or subscription tier.

### Option B — [Arcade](https://app.arcade.software/) (Available AI-Assisted Screen Capture Tool)
* **Overview**: A browser-based product walkthrough platform that automates UI recording, step detection, and brand color extraction.
* **Free Tier Details & Credits**:
  * Arcade provides **200 free credits per month** on individual accounts (AOSSIE does not provide paid team workspaces).
  * A 30-second video costs **50 credits**; a 60-second video costs **100 credits**. On a free plan, you can generate roughly two 60-second explainer drafts per month.
  * **Manual Edits are Free**: Once a draft is generated, making manual timeline edits, script tweaks, and visual swaps costs **0 additional credits**. Regenerating from scratch starts a new generation that consumes credits.
* **Watermark Policy**: Free tier exports include an Arcade logo watermark. Official AOSSIE submissions must be clean and watermark-free. If using Arcade:
  1. Export the MP4 from Arcade.
  2. Use [Online Video Cutter - Remove Watermark](https://online-video-cutter.com/remove-logo) to cleanly mask the watermark before adding bumpers.

### Option C — [OBS Studio](https://obsproject.com/) + Timeline Editor
* **Overview**: Free, open-source recording software that captures lossless 1080p 60fps screen recordings of web dashboards, animations, and terminal CLI sessions.
* Pair OBS recordings with editors like **CapCut**, **DaVinci Resolve**, or **Clipchamp** to assemble the final cut.

---

## 4. Step-by-Step Explainer Workflow

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ 1. Project Goal │ ──> │ 2. Pick 2–3     │ ──> │ 3. Write Script │ ──> │ 4. Record UI    │
│    & Audience   │     │    Workflows    │     │    (~130 wpm)   │     │    (Sanitized)  │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
                                                                                 │
                                                                                 ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ 8. Final QA &   │ <── │ 7. Intro/Outro  │ <── │ 6. Subtitles &  │ <── │ 5. Assemble &   │
│    Checklist    │     │    Bumpers      │     │    Audio Duck   │     │    Voiceover    │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

### Step 1 — Understand the Project & Single Takeaway
Before opening any editor, formulate the **single takeaway statement** that a viewer should understand after watching:

> *Example (OrgExplorer)*:  
> "OrgExplorer transforms GitHub organization data into interactive visual dashboards to analyze contributor networks, repository health, and activity trends in real time."

Answer four questions:
1. What does the project do in plain language?
2. Who uses it (developers, maintainers, GSoC students)?
3. What manual pain point does it solve?
4. What 2–3 visual features prove this capability?

---

### Step 2 — Map Out 2 to 3 Core Workflows
Select only the features that deliver visual proof of your takeaway statement:
* **Workflow 1**: Initial setup or search (e.g., entering an organization name and loading metrics).
* **Workflow 2**: Core interactive feature (e.g., navigating the contributor graph or filtering by language).
* **Workflow 3**: High-value outcome (e.g., viewing bus-factor risk analysis or generating an export).

---

### Step 3 — Write the Narration Script
Keep narration conversational, active, and concise. Target a speaking pace of **130 to 140 words per minute** (approx. 130–160 words total for a 60–75 second walkthrough).

#### Sample Script Structure:
```text
[0:00 - 0:03] [AOSSIE Official Animated Intro]

[0:03 - 0:15] Problem (15-20 words):
Managing large open-source organizations makes it hard to see who is contributing where 
and track repository health across dozens of repos.

[0:15 - 0:25] Solution (15-20 words):
OrgExplorer solves this with an interactive visual intelligence dashboard that runs 
entirely in your browser without requiring complex setup.

[0:25 - 0:45] Feature Demo 1 (30-40 words):
Simply search for any GitHub organization to load live repository data. OrgExplorer automatically 
inspects public repos, breaks down language distributions across tech stacks, and visualizes recent 
commit frequency alongside active pull request velocity.

[0:45 - 1:05] Feature Demo 2 (30-40 words):
Next, explore the interactive Contributor Network graph. Maintainers can instantly trace collaboration 
clusters across team boundaries, identify key community champions, and detect single-developer 
dependencies to proactively mitigate bus-factor risk before it impacts the project.

[1:05 - 1:15] Summary (15-20 words):
Gain instant visibility into your entire open-source ecosystem, audit health metrics, 
and empower maintainers without friction.

[1:15 - 1:20] [AOSSIE Official Closing CTA Outro]
```

---

### Step 4 — Record Live Screen Interactions
* **Clean Environment**: Close unused browser tabs, hide personal bookmarks, and disable distracting extensions.
* **Sanitize First**: Ensure your deployment or local demo is completely sanitized. Explicitly remove any active personal access tokens (such as GitHub PATs), API keys, or private user data from view.
* **Scale UI for Clarity**: Set browser zoom to **110%–125%** so text, buttons, and badges remain legible on smaller laptop screens.
* **Smooth Mouse Motion**: Move the cursor deliberately. Avoid erratic circular wiggling or frantic clicking.

---

### Step 5 — Record Voiceover Narration
* Record in a quiet room with minimal echo.
* Use a dedicated microphone or headset if possible.
* Speak in a natural, friendly, and professional tone.
* In CapCut, use the built-in **Record Voiceover** tool and apply **Noise Reduction** if background hiss is present.

---

### Step 6 — Subtitles & Audio Ducking
* **Synchronized Subtitles**: Explainer videos must include captions so viewers in silent environments can follow along. Use CapCut's **Auto-Captions** or equivalent tools to generate clean subtitles. Place them in the lower-third with strong contrast (white text with dark stroke or background box).
* **Subtle Background Music (Optional)**: If adding background music, use verified copyright-free tracks from the [YouTube Audio Library](https://studio.youtube.com/) or [Pixabay Music](https://pixabay.com/music/).
* **Audio Ducking**: Keep background music volume at `-22 dB` to `-26 dB` during speech so the voiceover is always front and center.

---

### Step 7 — Refine Edits & Cut Generic Stock
* **Enforce the 60% UI Rule**: Ensure the authentic application interface is visible for at least 60% of the entire video.
* **Trim Stagnant Clips**: Cut out long loading spinners or pauses. Speed up typing sequences (1.5x–2x) to keep the pacing brisk.
* **Avoid Fluff**: Delete generic stock video of office buildings, server rooms, or abstract 3D models. Every second should teach the viewer about the actual product.

---

### Step 8 — Add the AOSSIE Intro and Outro
Every official AOSSIE explainer video must include the official brand assets:
* **Intro Bumper**: Prepend the official 2–3 second animated AOSSIE intro bumper at the beginning.
* **Outro End Card**: Append the official community closing card (inviting viewers to star the repository and join the AOSSIE Discord).
* **Final Duration Audit**: Verify that the entire timeline—from the first frame of the intro to the last frame of the outro—is between **60 and 90 seconds** (never exceeding **120 seconds**).

---

## 5. Pre-Publishing Checklist

Verify every item before submitting your video PR:

- [ ] **Runtime Compliance**: Final exported video is between **60 and 90 seconds** (strict maximum: **120 seconds**, including bumpers).
- [ ] **Product Visibility**: Authentic application UI is visible for at least 60% of the runtime.
- [ ] **Feature Authenticity**: All workflows and screens shown exist in the active codebase.
- [ ] **Voiceover Clarity**: Narration is crisp, audible, well-paced, and synchronized with screen actions.
- [ ] **Accurate Subtitles**: Clean, synchronized captions are included throughout the video.
- [ ] **Audio Compliance**: Any background music used is 100% copyright-free and ducked beneath narration.
- [ ] **AOSSIE Branding**: Includes official AOSSIE intro bumper and closing CTA outro end card.
- [ ] **Watermark-Free**: No third-party editor logos or trial watermarks.
- [ ] **Resolution**: Rendered at Full HD `1920x1080` (16:9), 30 or 60 fps, H.264 MP4.
- [ ] **Sanitized**: Zero API keys, private tokens, or sensitive credentials exposed.
- [ ] **File Size**: Optimized and compressed (under 100 MB for fast GitHub PR playback).
