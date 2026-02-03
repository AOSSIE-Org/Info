
# Improving Cross-Platform Remote Input Reliability

## Background and Motivation

[Rein](https://github.com/AOSSIE-Org/Rein) is a **cross-platform, LAN-based remote input controller**. It allows touchscreen devices to act as a trackpad and keyboard for a desktop system through a locally served web interface.

While the core functionality is already implemented, several areas require improvement to ensure consistent behavior across operating systems, display protocols, and input methods.

---

## Overview of Tasks

* **Improve cursor handling on Wayland** *(Highest Priority)*

  * Resolve cursor position desynchronization on Wayland (e.g., KDE).
  * Investigate virtual input devices or alternative input injection methods.
  * Ensure the cursor position is either correctly synced or reliably indicated.

* **Improve keyboard input handling**

  * Ensure consistent multi-character input (e.g., glide typing, voice input).

* **Complete and normalize key mappings**

  * Modifier keys, navigation keys, function keys, and media keys.

* **Ensure cross-platform compatibility**

  * Test across operating systems and display protocols.
  * Automate creation of distributables for all supported platforms
    (Linux must be distributed as a Flatpak).
  * Document platform-specific limitations and behavior.

* **Improve UI/UX**

  * Make the interface more intuitive and easier to use.

* **Improve LAN accessibility**

  * Enable stable LAN access without relying on changing IP addresses, which currently requires re-scanning.
  * This'll help when system input fails and the app is configured to auto-start.

Candidates are expected to refine these tasks in their GSoC proposals.

---

## Requirements

### Technical Skills

* Familiarity with the current stack:
  **TypeScript**, **Node.js**, **WebSockets**, **TanStack**, **Nut.js**
* Understanding of input injection and virtual input devices.
* Experience with **cross-platform packaging of Node.js applications**.
* Ability to test across different operating systems and environments
  (using VMs), including **Linux, macOS, Windows**, and potentially others.

### Proposal Expectations

* Clear, concise, and easy to understand.
* Demonstrates understanding of current limitations and the **end-to-end flow** of proposed solutions.
* Includes decision points and actions, ideally supported with **diagrams**.
* Identifies where alternative libraries could improve reliability or compatibility.
* Discusses potential future improvements and scope.

### General Abilities

* Ability to take ownership and work autonomously.
* Evaluate technical decisions and the existing stack against alternatives.
* Maintain cross-platform behavior and compatibility.
* Record demos or tutorials when appropriate.
* Produce clear documentation, including diagrams and architecture overviews.
* Help grow the user base through community and social channels.

---

## Resources

* Project repository:
  https://github.com/AOSSIE-Org/Rein
* Project wiki & specification:
  https://github.com/AOSSIE-Org/Rein/wiki
* Contribution guidelines:
  https://github.com/AOSSIE-Org/Rein/wiki/contribution

---

## Mentors

* GitHub: @imxade
  Discord: @Rituraj

---

## Communication Channel

Join our Discord server ([https://discord.gg/xnmAPS7zqB](https://discord.gg/xnmAPS7zqB) and discuss this idea in
**AOSSIE-Discord → Projects → Rein**.
