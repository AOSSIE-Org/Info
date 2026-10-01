# Teaser vs. Explainer: Choosing the Right Product Video

When creating a video for an AOSSIE project, the first step is determining the format that aligns with your communication goals. Teasers and Explainers serve distinct purposes, target different viewer mindsets, and require different pacing, audio styles, and production techniques.

This guide clarifies the differences so you can select the right format or plan a complementary two-video strategy for your project.

---

## 1. Quick Comparison Matrix

| Dimension | Teaser Video | Explainer Video |
| :--- | :--- | :--- |
| **Primary Objective** | Spark interest, curiosity, and hype | Educate, onboard, and explain functionality |
| **Viewer Question Answered** | *"Why should I care about this project?"* | *"What is this, how does it work, and how does it help me?"* |
| **Target Audience Mindset** | Casual browser, social media scroller, prospective contributor | Developer or user evaluating the tool for practical adoption |
| **Recommended Duration** | **30 to 45 seconds** | **60 to 90 seconds** |
| **Hard Maximum Duration** | **60 seconds** (inclusive of bumpers) | **120 seconds** (inclusive of bumpers) |
| **Pacing & Tempo** | Fast, dynamic, high-energy cuts (1–3s per shot) | Steady, measured, and easy to follow |
| **Product UI Screentime** | Rapid hero glimpses & key feature highlights | **Mandatory $\ge 60\%$** of total runtime |
| **Narration vs. Text** | Driven by punchy text callouts & dynamic music (voiceover optional) | Guided voiceover narration synchronized with live UI actions |
| **Music & Sound Style** | Upbeat, driving, copyright-free background music matched to cuts | Subtle, low-level ambient/tech soundtrack (voiceover takes center stage) |
| **Recommended Toolset** | [CapCut](https://www.capcut.com/), DaVinci Resolve, Clipchamp, OBS Studio | [CapCut](https://www.capcut.com/), [Arcade](https://app.arcade.software/), OBS Studio |


---

## 2. In-Depth Breakdown

### Teaser Video: The "Movie Trailer"

A teaser video is engineered for quick discovery and broad engagement. It hooks viewers within the first 3 seconds, articulates a recognizable developer pain point, and presents the project as the compelling modern solution.

* **Core Focus**: Highlighting value and outcomes rather than exhaustive technical workflows.
* **Length Rule**: Teasers should ideally run between **30 and 45 seconds**. While some feature-rich projects require extra breathing room, teasers must **never exceed 60 seconds** (including the official AOSSIE intro and outro bumpers).
* **Audio Atmosphere**: Music is a primary storytelling driver. Upbeat, copyright-free instrumental tracks set a forward-leaning tempo. Visual cuts and text pops should land on the musical downbeats.
* **When to Make a Teaser**:
  * Launching a new AOSSIE project release or major milestone.
  * Creating social media announcements (X/Twitter, LinkedIn, Reddit, YouTube Shorts).
  * Promoting an AOSSIE organization project for Google Summer of Code (GSoC) showcases.
  * Attracting initial community interest to star the repository.

👉 **Full Production Guide**: See [Teaser Video Production Guide](TeaserVideo.md).

---

### Explainer Video: The "Guided Walkthrough"

An explainer video is an instructional product tour designed for users and contributors who want to understand exactly what the software does and how to use it.

* **Core Focus**: Delivering practical, workflow-level clarity. It proves that the application works by demonstrating live interactions on real screens.
* **Length Rule**: Standard explainers run between **60 and 90 seconds**, with a **hard maximum cap of 120 seconds** (inclusive of official AOSSIE intro and outro bumpers).
* **Audio Atmosphere**: Clear, natural voiceover narration is the dominant audio element. Any background music must remain low and unobtrusive (ducked to `-20 dB` or lower) so speech is effortlessly intelligible.
* **UI Exposure**: Generic AI stock visuals (floating abstract shapes, corporate office handshakes) are prohibited. At least **60% of the runtime** must show the authentic application UI, terminal outputs, or dashboard interactions.
* **When to Make an Explainer**:
  * Embedding at the top of the repository `README.md` or official documentation.
  * Accompanying major version releases with clear functional walkthroughs.
  * Onboarding new contributors and users to reduce setup friction.

👉 **Full Production Guide**: See [Explainer Video Production Guide](ExplainerVideo.md).

---

## 3. Decision Tree: Which Video Should You Make?

```
                               Start Here
                                    │
                  What is your primary distribution goal?
                                    │
               ┌────────────────────┴────────────────────┐
               ▼                                         ▼
   Social Media / Community Hype            README / Docs / User Onboarding
   Fast engagement & awareness              Step-by-step functional demo
               │                                         │
               ▼                                         ▼
         Make a TEASER                            Make an EXPLAINER
       (30–45s, max 60s)                         (60–90s, max 120s)
  • Fast cuts, punchy text                 • Real UI screentime >= 60%
  • Upbeat copyright-free track            • Clear voiceover narration
  • Built with CapCut/OBS                  • Built with CapCut/Arcade/OBS
```

> [!TIP]
> **Complementary Strategy**: For flagship AOSSIE repositories, having **both** a Teaser and an Explainer is the ideal setup. Use the **Teaser** to attract traffic from social media and community posts, and place the **Explainer** directly inside the repository `README.md` to guide incoming users.

---

## 4. Universal Requirements for All AOSSIE Videos

Regardless of whether you are producing a Teaser or an Explainer, all official community video submissions must adhere to these foundational rules:

1. **Official AOSSIE Intro & Outro**: Every video must prepend the official 2–3 second AOSSIE intro bumper and append the official closing call-to-action end card.
2. **Duration Budget Includes Bumpers**: The maximum limits (**60s for Teasers**, **120s for Explainers**) apply to the **final exported video** including intro and outro bumpers.
3. **Strict Copyright Compliance**: Never use commercial music, popular songs, or unverified audio tracks. Always use verified copyright-free / royalty-free sources (e.g., YouTube Audio Library, Pixabay Music).
4. **Watermark-Free**: Videos must not contain third-party editor watermarks upon final submission.
5. **Technical Export Standards**:
   * Resolution: Full HD `1920x1080` (16:9 widescreen).
   * Framerate: 30 fps or 60 fps (60 fps preferred for smooth UI transitions).
   * Codec: H.264 / AAC inside an MP4 container.

---

## 5. Next Steps

Choose the dedicated guide for your video format:

* **[Teaser Video Production Guide](TeaserVideo.md)**: Scriptwriting, rhythm, copyright-free sound sourcing, and CapCut workflow.
* **[Explainer Video Production Guide](ExplainerVideo.md)**: Product walkthrough architecture, UI capture, voiceover narration, and editing with CapCut or Arcade.
