# 🎨 AOSSIE Brand & Style Guidelines

> **Live Status & Asset Exports**  
> Whenever you need to check the live kit status, inspect vector components, or require manual asset exports (SVG, PNG, high-resolution backdrops, or editable templates), please refer to the official Figma design files below:
> 
> - 🎨 **AOSSIE Brand Kit Figma**: [AOSSIE's Brand Kit](https://www.figma.com/design/ywJ3jFa67bdQsN5XczrHy3/AOSSIE-s-Brand-Kit?node-id=0-1&t=ZhcV3uSoGJkrObo0-1)
> - 🖼️ **AOSSIE All Logos Hub Figma**: [Logos Hub](https://www.figma.com/design/cQCpSQv0M6FAc62ncunx8s/Logos?node-id=0-1&t=8pZG0veAJXDpYwI0-1)
> - 📂 **AOSSIE Drafts and Backups Figma**: [Drafts & BackUps](https://www.figma.com/design/t0XXc7r3lTO3Y2m8HnU1Vv/Drafts-and-BackUps?node-id=0-1&t=CGmXm2dMtpXWMG89-1)

---

## 📖 1. Introduction

Welcome to the **AOSSIE Brand Kit Guidelines**. This guide is designed for everyone in the AOSSIE community - contributors, collaborators, builders, event organizers, and curious minds who want to understand and apply the AOSSIE brand with consistency, clarity, and care.

By sticking to these guidelines, we ensure a unified, professional, and recognizable identity across all digital platforms, media, presentations, and open-source initiatives.

### 🇦🇺 The AOSSIE Brand Identity Formula

$$\text{Innovative} + \text{Educational} + \text{Open Source} + \text{Australian} = \mathbf{AOSSIE}$$

**AOSSIE** stands for **Australian Open Source Software Innovation and Education**. Our brand represents technological advancement, academic research, and community-driven open-source development rooted in Australia.

---

## 🔣 2. Logo System & Asset Usage

The AOSSIE logo system combines identity, technology, and mission. The Australian continent silhouette establishes our geographic roots, while the embedded binary code pattern (`10101...`) symbolizes software development and digital innovation. The stylized curly braces `{}` in the wordmark directly reference programming languages and modern development culture.

### Logo Variants

| Variant | Description | Recommended Usage |
| :--- | :--- | :--- |
| **Primary Logo** | Full logo with Australia binary map, `A{}`SSIE wordmark, and organization tagline. | High-impact locations, default brand representation, project landing pages, official documents. |
| **Secondary Logo** | Minimal `a{}ssie.` wordmark with stylized programming braces. | Header bars, wide horizontal spaces, footers, compact web application headers. |
| **Logomark** | Standalone Australian silhouette containing binary code pattern. | Favicons, social media profile avatars, badges, app icons where text is unnecessary. |

### Color Consistency & Background Adaptation
All logo variants exist in **Dark Background** and **Light Background** options to maintain legibility across various themes.

> [!CAUTION]
> **Minimum Scaling Rule**: Never scale any logo or logomark below **24 px** in height or width. Always test for visual clarity and readability before publishing.

### 📥 Exporting Assets from Figma
To manually export assets from the official Figma files:
1. Select the component or frame in Figma.
2. Use `Cmd/Ctrl + C` or hold `Option/Alt-drag` to duplicate/copy components.
3. In the Export section of the right sidebar in Figma, add an **SVG** export configuration and click **Export**.

> [!TIP]
> **Need to convert a PNG logo to SVG or vector format?**  
> Refer to our detailed [PNG to SVG Logo Conversion & Vector Guidelines](./Guides/PNG-to-SVG-Conversion-Guide.md) for step-by-step software workflows, auto-tracing parameters, and vector design standards.


---


## 🎨 3. Colour Scheme

The AOSSIE color palette is inspired by Australia’s national colors (Green & Gold), reflecting growth, innovation, optimism, and community spirit.

| Role | Color Name | Hex Code | RGB | ID |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Color** | Golden Wallet | `#FFCD00` | `255, 205, 0` | `A-001` |
| **Secondary Color**| Baggy Green | `#00843D` | `0, 132, 61` | `A-002` |
| **Dark Neutral** | Dark Background| `#121212` | `18, 18, 18` | `A-003` |
| **Light Neutral** | Pure White | `#FFFFFF` | `255, 255, 255` | `A-004` |
| **Muted Neutral** | Muted Grey | `#7A7A7A` | `122, 122, 122` | `A-005` |

> [!TIP]
> Always use exact Hex codes or RGB values provided above (or Figma color picker) to guarantee color accuracy across digital products and print media.

---

## 🔤 4. Typography

AOSSIE uses **Inter** as its primary typeface across all digital applications, web platforms, and print communications.

### Why Inter?
- **Performance & Scalability**: Inter is an open-source, highly legible, optimized font family suitable for small screens and high-resolution displays.
- **Consistency**: Reduces reliance on licensed custom web fonts and ensures cross-platform visual uniformity.

*Note: Project maintainers may request custom font pairings for specialized projects upon prior approval, with Inter serving as the default fallback.*

### Type Hierarchy & Scale

| Style | Font Weight | Font Size | Best Used For |
| :--- | :--- | :--- | :--- |
| **Display** | Inter Black | 72 px | Hero headlines, large banners |
| **Heading 1** | Inter Bold | 48 px | Main page titles, major section headings |
| **Heading 2** | Inter SemiBold | 36 px | Section subheadings |
| **Heading 3** | Inter Medium | 28 px | Component titles, card headers |
| **Body** | Inter Regular | 18 px | Paragraphs, documentation text |
| **Caption** | Inter Medium | 14 px | Image captions, metadata, tags |
| **Button** | Inter SemiBold | 14 px | CTAs, UI buttons, interactive labels |

---

## 🖼️ 5. Social Banners & Virtual Backdrops

### Social Media Banners
- **Primary Banner**: Designed for high-impact social presence (LinkedIn, Twitter/X, YouTube). Features key organization highlights: *10+ Years of Innovation*, *20+ Open-Source Projects/Year*, *8K+ Contributors*.
- **Secondary Banner**: Monochromatic and minimal design for documentation headers, presentations, and background graphics.

### Virtual Meeting Backdrops
- Intended for webinars, virtual conferences, GSoC meetings, interviews, and community meetups.
- Designed with a clean side panel ensuring the AOSSIE logo is visible without obscuring the speaker.

> [!TIP]
> **Backdrop Quality**: When exporting virtual meeting backdrops from Figma, export at **8x scale** to ensure crisp visual presentation on high-definition video calls.

---

## 🎴 6. Organization Business Cards

Members and mentors can generate an official AOSSIE organization business card upon proper administrative approval.
- **Front Component (`card_front`)**: Contains the primary AOSSIE logo, tagline, and official website URL (`www.aossie.org`).
- **Back Component (`card_back`)**: Features customizable fields for `{Person Name}`, `{Designation}`, `{Contact}`, `{LinkedIn ID}`, and `{Mail}`.

---

## 📣 7. Social Media Post Templates

To maintain brand consistency across announcements and community updates, two post templates are available in Figma:

### Template Type 1: High-Impact Announcements
- **Best Suited For**: Product launches, major milestone updates, GSoC selection announcements, feature releases, and partnership news.
- **Structure**: Main Title + Org/Feature Logo + Tagline + Content/Metrics block + Prominent CTA button.

### Template Type 2: Informative & Community Content
- **Best Suited For**: Event details, workshop announcements, contributor spotlights, blog highlights, and educational content.
- **Structure**: Heading + Description + Showpiece Image + CTA + Date Range + Source + CTA Button + Topic Tags (`{TAG1} • {TAG2} • {TAG3}`).

---

## 💡 8. Design Principles & Best Practices

When creating marketing assets, graphics, or UI components for AOSSIE, follow these core principles:

1. **Clarity Over Clutter**: Keep layouts clean, spacious, and focused. Use bold, clear typography that conveys the message immediately.
2. **Personality with Purpose**: Use illustrative elements (e.g., binary overlays, code brackets `{}`) that educate and represent software engineering, not just decorative art.
3. **Respect Minimum Sizes**: Keep logos legible; never shrink logos below 24 px.
4. **Use Official Assets**: Do not modify logo colors, stretch vector proportions, or alter brand fonts arbitrarily. Use the pre-built Figma assets.

---

## 📂 9. Repository Media Assets & Directory Index

Below is the directory index providing clickable access to all local media assets available inside this repository.

### 📁 Root Media Directories
- 📂 **[Brand/Media Assets](./Brand/Media%20Assets/)** - Primary repository media assets folder.
- 📁 **[Project Icons SVGs](./Brand/Media%20Assets/Project%20Icons%20SVGs/)** - Project logos and icons for all AOSSIE sub-projects.
- 📁 **[AOSSIE Intro Video](./Brand/Media%20Assets/AOSSIE%20Intro%20Video)** - The official intro video for AOSSIE provided in Original, 1080p, 720p and gif.
- 📁 **[AOSSIE Project Video Guide](./Brand/Media%20Assets/AOSSIE%20Project%20Video%20Guide)** - Comprehensive guides for creating project Teaser and Explainer videos.

---

### 🚀 A. AOSSIE Intro Video
**Directory Path**: [`Brand/Media Assets/AOSSIE Intro Video`](./Brand/Media%20Assets/AOSSIE%20Intro%20Video)

| Asset Name | Format | Direct Link | Description |
| :--- | :--- | :--- | :--- |
| **intro_original** | MP4 | [`intro_original.mp4`](./Brand/Media%20Assets/AOSSIE%20Intro%20Video/intro_original.mp4) | Highest Quality Intro Video (Preferred) |
| **intro_1080p** | MP4 | [`intro_1080p.mp4`](./Brand/Media%20Assets/AOSSIE%20Intro%20Video/intro_1080p.mp4) | 1080p Quality Intro Video |
| **intro_720p** | MP4 | [`intro_720p.mp4`](./Brand/Media%20Assets/AOSSIE%20Intro%20Video/intro_720p.mp4) | 720p Quality Intro Video  |
| **intro_gif** | GIF | [`intro_gif.gif`](./Brand/Media%20Assets/AOSSIE%20Intro%20Video/intro_gif.gif) | GIF Intro Video  |
---

### 🧳 B. Merchandise & Bag Assets
**Directory Path**: [`Brand/Media Assets/Bag`](./Brand/Media%20Assets/Bag/)

| Asset Name | Format | Direct Link | Description |
| :--- | :--- | :--- | :--- |
| **AOSSIE Logo Vector** | SVG | [`aossie_logo.svg`](./Brand/Media%20Assets/Bag/aossie_logo.svg) | Vector SVG logo for bag printing |
| **Bag Design 2** | PNG | [`bag_design2.png`](./Brand/Media%20Assets/Bag/bag_design2.png) | Secondary backpack design render |
| **Backpack Mockup** | PNG | [`bag_mockup.png`](./Brand/Media%20Assets/Bag/bag_mockup.png) | High-res mockup of AOSSIE backpack |
| **Bag Strip Accent** | SVG | [`bag_strip.svg`](./Brand/Media%20Assets/Bag/bag_strip.svg) | Vector strip graphic accent |

---

### 🚩 C. Social Media Banners
**Directory Path**: [`Brand/Media Assets/Banner`](./Brand/Media%20Assets/Banner/)

| Asset Name | Format | Direct Link | Description |
| :--- | :--- | :--- | :--- |
| **Primary Banner** | PNG | [`banner_primary.png`](./Brand/Media%20Assets/Banner/banner_primary.png) | High-impact green & gold social banner |
| **Primary Banner Mockup**| PNG | [`banner_primary_mockup.png`](./Brand/Media%20Assets/Banner/banner_primary_mockup.png) | Profile header mockup preview |
| **Secondary Banner** | PNG | [`banner_secondary.png`](./Brand/Media%20Assets/Banner/banner_secondary.png) | Monochromatic minimal banner |

---

### 📹 D. Virtual Meeting Backdrops
**Directory Path**: [`Brand/Media Assets/Meeting Backdrops`](./Brand/Media%20Assets/Meeting%20Backdrops/)

| Asset Name | Format | Direct Link | Description |
| :--- | :--- | :--- | :--- |
| **Backdrop 1** | PNG | [`backdrop1.png`](./Brand/Media%20Assets/Meeting%20Backdrops/backdrop1.png) | Blue curved side-panel backdrop |
| **Backdrop 2** | PNG | [`backdrop2.png`](./Brand/Media%20Assets/Meeting%20Backdrops/backdrop2.png) | Dark blue variant backdrop |
| **Backdrop 1 Mockup** | PNG | [`backdrop_mockup1.png`](./Brand/Media%20Assets/Meeting%20Backdrops/backdrop_mockup1.png) | Video call preview (Backdrop 1) |
| **Backdrop 2 Mockup** | PNG | [`backdrop_mockup2.png`](./Brand/Media%20Assets/Meeting%20Backdrops/backdrop_mockup2.png) | Video call preview (Backdrop 2) |

---

### 🎴 E. Organization Cards
**Directory Path**: [`Brand/Media Assets/Organization Card`](./Brand/Media%20Assets/Organization%20Card/)

| Asset Name | Format | Direct Link | Description |
| :--- | :--- | :--- | :--- |
| **Card Front Template** | PNG | [`card_front.png`](./Brand/Media%20Assets/Organization%20Card/card_front.png) | Front side organization card design |
| **Card Back Template** | PNG | [`card_back.png`](./Brand/Media%20Assets/Organization%20Card/card_back.png) | Back side template with contact fields |
| **Card Mockup 1** | PNG | [`card_mockup1.png`](./Brand/Media%20Assets/Organization%20Card/card_mockup1.png) | Realistic print mockup 1 |
| **Card Mockup 2** | PNG | [`card_mockup2.png`](./Brand/Media%20Assets/Organization%20Card/card_mockup2.png) | Realistic print mockup 2 |
| **Card Mockup 3** | PNG | [`card_mockup3.png`](./Brand/Media%20Assets/Organization%20Card/card_mockup3.png) | Card stack perspective mockup |
| **Card Mockup 4** | PNG | [`card_mockup4.png`](./Brand/Media%20Assets/Organization%20Card/card_mockup4.png) | Handheld card mockup |

---

### 📱 F. Social Media Post Templates
**Directory Path**: [`Brand/Media Assets/Social Media Posts`](./Brand/Media%20Assets/Social%20Media%20Posts/)

| Asset Name | Format | Direct Link | Description |
| :--- | :--- | :--- | :--- |
| **Post Template 1** | PNG | [`post_template1.png`](./Brand/Media%20Assets/Social%20Media%20Posts/post_template1.png) | Type 1: High-impact announcement post |
| **Post Template 2** | PNG | [`post_template2.png`](./Brand/Media%20Assets/Social%20Media%20Posts/post_template2.png) | Type 2: Informative & community content |
| **Post Mockup** | PNG | [`post_mockup.png`](./Brand/Media%20Assets/Social%20Media%20Posts/post_mockup.png) | Example GSoC selection announcement post |

---

### 🏷️ G. Swags & Stickers
**Directory Path**: [`Brand/Media Assets/Swags`](./Brand/Media%20Assets/Swags/)

| Asset Name | Format | Direct Link | Description |
| :--- | :--- | :--- | :--- |
| **AOSSIE Keycaps** | PNG | [`aossie_keycaps.png`](./Brand/Media%20Assets/Swags/aossie_keycaps.png) | Keycaps graphic swag |
| **AOSSIE Sticker** | PNG | [`aossie_sticker.png`](./Brand/Media%20Assets/Swags/aossie_sticker.png) | Primary logo sticker cutout |
| **Brewed for Builders**| PNG | [`brewed_for_builders.png`](./Brand/Media%20Assets/Swags/brewed_for_builders.png) | Coffee mug sticker graphic |
| **Building Future** | PNG | [`building_future.png`](./Brand/Media%20Assets/Swags/building_future.png) | Kangaroo open-source sticker |
| **Coding Kangaroo** | PNG | [`coding_kangaroo.png`](./Brand/Media%20Assets/Swags/coding_kangaroo.png) | Coding Kangaroo sticker artwork |
| **GitHub Contributions**| PNG | [`github_contributions.png`](./Brand/Media%20Assets/Swags/github_contributions.png) | Code • Contribute • Repeat graphic |
| **Logomark Sticker** | PNG | [`logomark_sticker.png`](./Brand/Media%20Assets/Swags/logomark_sticker.png) | Australia binary map sticker cutout |
| **OSS Stamp** | PNG | [`oss_stamp.png`](./Brand/Media%20Assets/Swags/oss_stamp.png) | "OSS for Everyone" stamp graphic |

---

### 🛠️ H. Useful Assets & Badges
**Directory Path**: [`Brand/Media Assets/Useful Assets`](./Brand/Media%20Assets/Useful%20Assets/)

| Asset Name | Format | Direct Link | Description |
| :--- | :--- | :--- | :--- |
| **3D Megaphone** | PNG | [`announcement_asset.png`](./Brand/Media%20Assets/Useful%20Assets/announcement_asset.png) | Announcement Megaphone graphic element |
| **GSoC Full Logo** | SVG | [`gsoc_full_logo.svg`](./Brand/Media%20Assets/Useful%20Assets/gsoc_full_logo.svg) | Full GSoC logo badge vector |
| **GSoC White BG Logo**| SVG | [`gsoc_full_logo_whitebg.svg`](./Brand/Media%20Assets/Useful%20Assets/gsoc_full_logo_whitebg.svg) | GSoC logo badge (light background) |
| **GSoC Logomark 1** | SVG | [`gsoc_logomark1.svg`](./Brand/Media%20Assets/Useful%20Assets/gsoc_logomark1.svg) | GSoC code icon badge variant 1 |
| **GSoC Logomark 2** | SVG | [`gsoc_logomark2.svg`](./Brand/Media%20Assets/Useful%20Assets/gsoc_logomark2.svg) | GSoC code icon badge variant 2 |

---

### 🎨 I. Project Logos & Icons
**Directories**: [`Project Icons PNGs`](./Brand/Media%20Assets/Project%20Icons%20PNGs/) | [`Project Icons SVGs`](./Brand/Media%20Assets/Project%20Icons%20SVGs/)

| Project Name | PNG Asset | SVG Asset |
| :--- | :--- | :--- |
| **AOSSIE Logo (Default)** | [`aossie_logo.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/aossie_logo.png) | [`aossie_logo.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/aossie_logo.svg) |
| **AOSSIE Dark Logo** | [`aossie_dark_logo.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/aossie_dark_logo.png) | [`aossie_dark_logo.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/aossie_dark_logo.svg) |
| **AOSSIE Light Logo** | [`aossie_light_logo.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/aossie_light_logo.png) | [`aossie_light_logo.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/aossie_light_logo.svg) |
| **AOSSIE Logomark** | [`aossie_logomark.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/aossie_logomark.png) | [`aossie_logomark.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/aossie_logomark.svg) |
| **Secondary Logo** | [`aossie_secondary_logo.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/aossie_secondary_logo.png) | [`aossie_secondary_logo.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/aossie_secondary_logo.svg) |
| **DIT Logo** | [`dit_logo.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/dit_logo.png) | [`dit_logo.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/dit_logo.svg) |
| **Djed Alliance Logo** | [`djed_alliance_logo.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/djed_alliance_logo.png) | [`djed_alliance_logo.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/djed_alliance_logo.svg) |
| **FATE Logo** | [`fate_logo.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/fate_logo.png) | [`fate_logo.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/fate_logo.svg) |
| **PictoPy Logo** | [`pictopy_logo.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/pictopy_logo.png) | [`pictopy_logo.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/pictopy_logo.svg) |
| **Resonate Logo** | [`resonate_logo.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/resonate_logo.png) | [`resonate_logo.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/resonate_logo.svg) |
| **Skills Logo** | [`skills_logo.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/skills_logo.png) | [`skills_logo.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/skills_logo.svg) |
| **Stability Nexus Logo** | [`stability_nexus_logo.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/stability_nexus_logo.png) | [`stability_nexus_logo.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/stability_nexus_logo.svg) |
| **StablePay Logo** | [`stablepay_logo.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/stablepay_logo.png) | [`stablepay_logo.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/stablepay_logo.svg) |
| **TNT Logo** | [`tnt_logo.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/tnt_logo.png) | [`tnt_logo.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/tnt_logo.svg) |
| **Zplit Logo** | [`zplit_logo.png`](./Brand/Media%20Assets/Project%20Icons%20PNGs/zplit_logo.png) | [`zplit_logo.svg`](./Brand/Media%20Assets/Project%20Icons%20SVGs/zplit_logo.svg) |

---

### 🎬 J. Project Video Production Guides
**Directory Path**: [`Brand/Media Assets/AOSSIE Project Video Guide`](./Brand/Media%20Assets/AOSSIE%20Project%20Video%20Guide/)

| Document | Format | Direct Link | Description |
| :--- | :--- | :--- | :--- |
| **Video Format Overview** | Markdown | [`Videos.md`](./Brand/Media%20Assets/AOSSIE%20Project%20Video%20Guide/Videos.md) | Teaser vs. Explainer video comparison and selection matrix |
| **Teaser Video Production Guide** | Markdown | [`TeaserVideo.md`](./Brand/Media%20Assets/AOSSIE%20Project%20Video%20Guide/TeaserVideo.md) | Production handbook for short, high-energy teaser videos ($\le$ 60s) |
| **Explainer Video Production Guide** | Markdown | [`ExplainerVideo.md`](./Brand/Media%20Assets/AOSSIE%20Project%20Video%20Guide/ExplainerVideo.md) | Practical guide for instructional product walkthrough videos ($\le$ 120s) |

---

## 🤝 Summary Checklist for Contributors & Visitors

- [ ] Check the [AOSSIE Brand Kit Figma](https://www.figma.com/design/ywJ3jFa67bdQsN5XczrHy3/AOSSIE-s-Brand-Kit?node-id=0-1&t=ZhcV3uSoGJkrObo0-1) for live updates.
- [ ] Use **Golden Wallet** (`#FFCD00`) and **Baggy Green** (`#00843D`) as core brand colors.
- [ ] Use **Inter** as the default typeface.
- [ ] Download vector SVGs directly from the [Logos Hub Figma](https://www.figma.com/design/cQCpSQv0M6FAc62ncunx8s/Logos?node-id=0-1&t=8pZG0veAJXDpYwI0-1) or [Project Icons/SVGs](./Brand/Media%20Assets/Project%20Icons%20SVGs/).
- [ ] Access local media assets directly from [Brand/Media Assets](./Brand/Media%20Assets/).
- [ ] Refer to [Drafts and BackUps Figma](https://www.figma.com/design/t0XXc7r3lTO3Y2m8HnU1Vv/Drafts-and-BackUps?node-id=0-1&t=CGmXm2dMtpXWMG89-1) for raw components and WIP templates.
