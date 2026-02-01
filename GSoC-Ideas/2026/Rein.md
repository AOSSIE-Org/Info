
# Improving Cross-Platform Remote Input Reliability

## Background and Motivation


[Rein](https://github.com/AOSSIE-Org/Rein) is a **cross-platform, LAN-based remote input controller**. It allows touchscreen devices to act as a trackpad and keyboard for a desktop system through a locally served web interface.

While the core functionality is already implemented, several areas require improvement to ensure consistent behavior across operating systems, display protocols, and input methods.


## Overview of Tasks

* **Improve cursor handling on Wayland:** [Highest Priority]

  * Resolve cursor position desynchronization on Wayland (e.g., KDE).
  * Investigate virtual input devices or alternative injection methods.
  * Ensure the cursor position is either correctly synced or reliably indicated.

* **Improve keyboard input handling:**

  * Ensure consistent multi-character input (e.g., glide typing, voice input).

* **Complete and normalize key mappings:**

  * Modifier keys, navigation keys, function keys, and media keys.

* **Ensure cross-platform compatibility:**

  * Test across operating systems and display protocols.
  * Document platform-specific limitations and behavior.

* Additional: [Low priority]

  * Enable stable LAN access without relying on changing IP addresses.

Candidates are expected to refine these tasks in their GSoC proposals.


## Requirements

* **Technical Skills:**

  * Familiarity with the current stack: **WebSockets**, **TanStack**, **Nut.js**, **TypeScript** and **Node.js**.
  * Knowledge of input injection and virtual input devices.
  * Experience with **cross-platform packaging of Node.js applications**.

* **Proposal Expectations:**

  * Be clear, concise, and easy to understand.
  * Demonstrate understanding of current limitations and the end-to-end flow of how they'll be addressed.
  * Include decision points and actions, ideally illustrated with diagrams.
  * Identify where alternative libraries could improve reliability or compatibility.

* **General Abilities:**

  * Take ownership and work autonomously.
  * Evaluate decisions and tech stack against alternatives.
  * Maintain cross-platform behavior and compatibility.
  * Record demo/tutorial.
  * Documentation with diagram and architecture.
  * Help gain user base and raise funds via social means.

## Resources

* Project repository:
  [https://github.com/imxade/rein](https://github.com/AOSSIE-Org/Rein)
* Project wiki & specification:
  [https://github.com/imxade/rein/wiki](https://github.com/imxade/rein/wiki)
* Contribution guidelines:
  [https://github.com/imxade/rein/wiki/contribution](https://github.com/imxade/rein/wiki/contribution)



## Mentors

* GitHub: @imxade; Discord: @Rituraj

---

## Communication Channel

Join our Discord servers (https://discord.gg/xnmAPS7zqB and https://discord.gg/fuuWX4AbJt) and discuss this idea in AOSSIE-Discord/Projects/Rein.
