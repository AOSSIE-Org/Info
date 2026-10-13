# AOSSIE Teaser Video Production Guide

A practical handbook for open-source contributors to produce high-impact, energetic **Teaser Videos** for AOSSIE projects.

---

## 1. Overview & Objective

A **Teaser Video** is a short, fast-paced video designed to spark curiosity, excitement, and community engagement. Think of it as a **movie trailer** for your open-source project: its mission is not to teach every single button or feature, but to make the viewer say: *"Wow, this looks incredible—I need to check this out!"*

### Key Characteristics:
* **Energetic & Forward-Leaning**: Quick cuts (1 to 3 seconds per shot), lively motion graphics, and animated kinetic typography.
* **Value-First**: Hooks the audience immediately with a relatable developer struggle and unveils your project as the modern answer.
* **Driven by Rhythm & Music**: Upbeat, copyright-free background music drives the tempo of the edits.

---

## 2. Duration Contract

| Parameter | Specification | Notes |
| :--- | :--- | :--- |
| **Recommended Length** | **30 to 45 seconds** | Ideal for social feeds (X/Twitter, LinkedIn, YouTube Shorts). |
| **Hard Maximum Cap** | **60 seconds** | Teaser videos should **never exceed 60 seconds** in total. |
| **Bumper Inclusion** | **Included in runtime** | Total time includes the official 2–3s AOSSIE intro and closing outro. |

> [!IMPORTANT]
> **Why the 60-Second Cap?**  
> While the sweet spot for a teaser is 30–45 seconds, complex projects with multiple visual dashboards or CLI outputs sometimes need slightly more breathing room. However, exceeding 60 seconds dilutes the teaser's punchiness and causes viewer drop-off. Keep the core teaser body between **25 and 50 seconds** so that with the 2–3s AOSSIE intro and 3–5s outro card, the final video sits safely at or below **60 seconds**.

---

## 3. Copyright-Free Audio & Sound Design Guide

Audio is the heartbeat of a teaser video. A dynamic soundtrack transforms static screen captures into an exciting story. However, open-source projects must strictly adhere to digital copyright compliance.

### 🚫 The Golden Rule: Never Use Unlicensed or Incompatible Music
* **Do NOT** use unlicensed commercial tracks, chart-topping pop songs, movie scores, or viral audio lacking open distribution rights.
* **Why this matters**: Using unlicensed or rights-restricted tracks causes automated Content ID copyright strikes, video mutes, takedown notices on YouTube/social media, and immediate pull request rejection by AOSSIE maintainers.
* **Always use Properly Licensed Music**: Use tracks released under Creative Commons (CC0 or CC-BY with attribution) or dedicated royalty-free open libraries safe for commercial and open-source redistribution.

---

### Curated Libraries to Find Free & Safe Music

Here are top recommended platforms to source copyright-free music for your video:

| Platform | License & Terms | Best For | Link |
| :--- | :--- | :--- | :--- |
| **YouTube Audio Library** | 100% royalty-free, pre-cleared for YouTube. Most tracks require no attribution (check track details). | Safe, zero-claim background tracks filtered by genre and mood. | [YouTube Studio Audio Library](https://studio.youtube.com/) |
| **Pixabay Music** | Free for commercial and non-commercial use under Pixabay Content License. No attribution required. | Modern electronic, upbeat synth, tech, and corporate beats. | [pixabay.com/music](https://pixabay.com/music/) |
| **Free Music Archive (FMA)** | Creative Commons tracks. Filter by CC0 (public domain) or CC-BY (attribution required). | Diverse indie electronic, synthwave, and lo-fi tracks. | [freemusicarchive.org](https://freemusicarchive.org/) |
| **Incompetech** | Free with CC-BY attribution to Kevin MacLeod. | Reliable instrumental soundtracks across distinct genres. | [incompetech.com](https://incompetech.com/) |
| **Bensound** | Free tier available under CC-BY attribution. | Polished upbeat, corporate, and tech background music. | [bensound.com](https://bensound.com/) |
| **CapCut Built-In Commercial Music** | Filterable by "Commercial Use" within CapCut's audio tab. | Quick in-editor soundtrack selection without external downloads. | Included in CapCut App |

> [!TIP]
> **Attribution Requirement**: If you choose a track licensed under **Creative Commons Attribution (CC-BY)**, include the artist credit, song title, license link, the track's source URL (when supplied by the licensor), and a statement indicating whether changes were made to the audio (as required by CC BY 4.0) in your PR description so maintainers can append it to the video's public description upon publishing.

---

### Audio Mixing Best Practices for Teasers

1. **Pick the Right Genre & BPM**:
   * Target tempo: **115 to 135 BPM** (upbeat electronic, future bass, modern tech house, or driving instrumental synth).
   * Avoid sleepy acoustic tracks or distracting songs with loud lead vocals.
2. **Cut on the Beat**:
   * Place markers on the musical downbeats on your editing timeline.
   * Sync visual cuts, screen zooms, and text transitions directly to the rhythm.
3. **Volume Balance & Ducking**:
   * If your teaser uses **text overlays only** (music-driven): Aim for an integrated loudness of approximately `-14 LUFS`, while keeping true peak levels between `-1 dBTP` and `-3 dBTP` to prevent inter-sample clipping or distortion during encoding.
   * If your teaser includes **voiceover or sound bites**: Apply **Audio Ducking** to reduce music volume down to `-20 dB` to `-25 dB` whenever the narrator speaks, returning to full energy during visual pauses.

---

## 4. Recommended Tools & Software

You have full flexibility in choosing your video production tools. Several excellent tools are available to suit different workflows:

### 1. [CapCut](https://www.capcut.com/) (Highly Recommended for Teasers)
* **Why it's great**:
  * Free desktop, web, and mobile versions with timeline multi-track editing.
  * Rich library of dynamic text presets, kinetic animations, and glitch/motion transitions.
  * Built-in beat detection (`Auto Beat`) to effortlessly snap cuts to musical tempo.
  * In-app commercial audio library and sound effects (whooshes, clicks, pops).
  * Direct 1080p 60fps export with zero watermarks on standard free exports (verify available export settings and stick to eligible free assets, as settings and watermark policies can vary by platform, assets, or subscription).
* **Best used for**: Assembling screen recordings, adding punchy text callouts, beat-synced cutting, and final branding.

### 2. [Arcade](https://app.arcade.software/) (Available Option for UI Snippets)
* **What it does**: AI-assisted interactive screen recording tool that automatically tracks mouse clicks and extracts project brand colors.
* **Credits on Free Tier**: 200 credits/month (30-second video costs 50 credits). Note that manual adjustments on an existing draft cost 0 credits.
* **Watermark Policy**: Free tier exports include an Arcade watermark. If you record snippets with Arcade, remove the watermark using tools like [Online Video Cutter - Remove Watermark](https://online-video-cutter.com/remove-logo) before assembling in your editor.

### 3. Screen Recorders (Lossless 1080p 60fps)
* **[OBS Studio](https://obsproject.com/)**: Free, open-source recording suite. Perfect for silky-smooth 60fps captures of web apps, terminal CLI commands, or animations without compression artifacts.
* **Native Browser / OS Recorders**: Windows Game Bar (`Win + G`), macOS QuickTime, or Chrome extensions.

### 4. Alternative Timeline Editors
* **DaVinci Resolve**: Industry-grade free video editor with advanced color grading and Fairlight audio tools.
* **Clipchamp**: Free built-in Windows editor with clean text presets and simple timeline management.

---

## 5. Step-by-Step Production Workflow

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ 1. Define Hook  │ ──> │ 2. Storyboard   │ ──> │ 3. Record UI    │ ──> │ 4. Music & Edit │
│    (First 3 sec)│     │    (30–45s plan)│     │    (1080p 60fps)│     │    (CapCut)     │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
                                                                                 │
                                                                                 ▼
                                                                        ┌─────────────────┐
                                                                        │ 5. Bumpers & QA │
                                                                        │    (Max 60s)    │
                                                                        └─────────────────┘
```

### Step 1 — Define the 3-Second Hook
Online viewers decide whether to keep watching within the first 3 seconds. Introduce your hook immediately during the opening 0:00–0:03 window (for example, as a bold text overlay across the official intro bumper):
* *Example (Question)*: *"Struggling to track contributor impact across 50+ repositories?"*
* *Example (Bold Statement)*: *"GitHub analytics shouldn't require complex SQL queries."*

---

### Step 2 — Storyboard the 30–45 Second Arc
Structure your teaser into clear, rapid phases:

| Timestamp | Phase | Content |
| :--- | :--- | :--- |
| **0:00 – 0:03** | **Official Intro & Hook** | Official AOSSIE 2–3s animated bumper with hook text overlay to capture viewer attention within the first 3 seconds. |
| **0:03 – 0:08** | **The Problem** | Rapid text punchline highlighting the developer pain point. |
| **0:08 – 0:15** | **The Reveal** | *"Introducing [Project Name]"* + Logo reveal with dynamic transition. |
| **0:15 – 0:35** | **Hero Feature Blitz** | 2 to 3 rapid snippets showcasing visually impressive UI actions (e.g., interactive graph, one-click report, live filtering). Each shot lasts 2–4 seconds max. |
| **0:35 – 0:42** | **Key Impact / Value** | Punchy text: *"Open Source. Fast. 100% In-Browser."* |
| **0:42 – 0:45** | **Call to Action (Outro)** | Official AOSSIE closing card with GitHub star link and Discord invite. |

---

### Step 3 — Record High-Quality Product Footage
* Open your project in a clean browser window (close unnecessary tabs, disable personal extensions, hide bookmarks bar).
* Zoom the browser interface to **110%–125%** so text and numbers remain readable on mobile screens.
* **Sanitize Credentials**: Never expose active personal access tokens (PATs), secret API keys, or private user data.
* Record smooth interactions at **1080p 60fps** using OBS Studio or your preferred screen recorder.

---

### Step 4 — Source a Copyright-Free Audio Track
* Browse [Pixabay Music](https://pixabay.com/music/) or the [YouTube Audio Library](https://studio.youtube.com/).
* Search for keywords: `Technology`, `Cyberpunk`, `Upbeat Electronic`, `Future Bass`, or `Corporate Tech`.
* Download an MP3 or WAV file and verify the license terms.
* If you publish the video on X, LinkedIn, or another platform, confirm that the selected track's license permits that use and record any required attribution.

---

### Step 5 — Assemble and Edit (in CapCut or Chosen Editor)
1. Import your UI recordings, selected audio track, and the official AOSSIE intro/outro clips.
2. Align the audio track and use beat-detection markers to time cuts.
3. Apply subtle zoom-ins on key buttons or graphs to draw the eye to the action.
4. Add bold, high-contrast text overlays (use sans-serif fonts, white text with dark drop-shadow or accent highlight).
5. Keep shot lengths short: 2 to 3 seconds per clip prevents viewers from losing interest.

---

### Step 6 — Prepend Intro & Append Outro Bumpers
* **Intro**: Prepend the official 2–3 second AOSSIE intro bumper.
* **Outro**: Append the official community closing end card.
* **Verify Final Time**: Check the timeline to ensure the entire render (from first second to the final frame) is **strictly $\le$ 60 seconds**.

---

## 6. Pre-Publishing Checklist

Before submitting your teaser video PR, confirm every item on this checklist:

- [ ] **Runtime**: Total video duration is **between 30 and 45 seconds** (hard maximum **60 seconds**, inclusive of intro/outro).
- [ ] **Audio Compliance**: Soundtrack is properly licensed and compatible (royalty-free, CC0, or CC-BY with attribution; no unlicensed commercial audio).
- [ ] **Attribution Documented**: If using CC-BY audio, attribution details are included in the PR description.
- [ ] **Resolution & Aspect Ratio**: 1080p (`1920x1080`, 16:9 landscape) at 30 or 60 fps, alongside a separate vertical (`1080x1920`, 9:16) or square (`1080x1080`, 1:1) export for YouTube Shorts and mobile feeds.
- [ ] **AOSSIE Branding**: Contains the official AOSSIE animated intro bumper and closing CTA outro card.
- [ ] **Watermark-Free**: No third-party editor logos or platform watermarks are visible.
- [ ] **Pacing**: Visual cuts are snappy (1–3s per shot), visually synced to musical rhythm.
- [ ] **Legibility**: Text overlays and UI elements are crisp and readable on mobile devices.
- [ ] **Sanitized**: Zero secrets, tokens, or credentials visible on screen.
- [ ] **Format & File Size**: Rendered as H.264 MP4; file size kept compact (under 50 MB recommended for teasers).
