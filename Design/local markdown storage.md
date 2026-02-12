# Local Markdown Storage Architecture

### 1. Problem Statement

Most note-taking apps store user data in cloud services or proprietary formats, which reduces user control and offline      reliability. 

This project needs a simple, local-first storage system for markdown notes. 

The system should work without internet, respect user privacy, and scale to thousands of files without slowing down. The goal is to make local files the single source of truth. 

### 2. Goals

Offline-first experience : 
    NO Internet,
    NO Cloud Serives,
    NO Server
   
User fully owns their data (plain markdown files)

Scales to large note collections (thousands of notes)

Easy to inspect, backup, and move files

###  3. Non-Goals

Cloud sync
Real-time collaboration
AI processing (handled in separate layers later)

### 4. Constraints

Desktop app built with Electron

Must work consistently on Windows, macOS, and Linux

Privacy-first: no hidden data collection

File system is the source of truth

### 5. High-Level Architecture

The app treats a Editor folder as a “notes workspace.”
Each note is stored as a markdown(.md) file on disk.

The app maintains:

  "in-memory index " and "local db(SQLite) 

   A file watcher to detect changes ( like : File added , file changed, file deleted , file renamed )

   A metadata layer derived from frontmatter

   All edits made inside the app directly modify markdown files, and external file changes are reflected back in the UI.

### 6. Storage Model

Notes are stored as (.md) files

Folder-based organization (nested folders = categories)

File system is the single source of truth

No proprietary database format for note content

* STRUCTURE :

   Notes/
    |--->Note1.md
    |--->Note2.md

### 7. Folder Watching Strategy

WHY needed?
    User may write notes outside the app like (vs code, notepad) then app automatically detect changes  and update by using FOLDER WATCHER

*Events handled:

File created → add note to index

File updated → refresh note content

File deleted → remove from index

Folder renamed → update paths

Bulk changes → trigger index rebuild

*Tools:
chokidar (Node.js file watcher)

### 8. Metadata Handling (Simple)

Metadata means extra info about a note like:
title
tags
created date
updated date

We store metadata inside the markdown file using frontmatter, so the file is still readable and portable.

* Example :
---
title: My First Note
tags: [gsoc, ideas]
created: 2026-02-12
---
This is my note content.

### 9. Performance Considerations (Simple)

To keep the app fast even with many notes:

-Only load a note when the user opens it (lazy loading)
-Don’t read all file contents at startup
-Build a small index for quick search
-Update index only for changed files
-Run heavy work in background
-Cache recently opened notes
-Avoid reloading everything on every file change
---
Why this helps:

Faster app startup
Smooth UI
Works well even with thousands of notes
---

### 10. Trade-offs & Risks (IMPORTANT PART)

* TRADE-OFFS

Using plain markdown files keeps things simple and transparent, but we lose strong database-like guarantees (no transactions or atomic writes).

File watching behaves differently across operating systems, so edge cases can appear on Windows, macOS, or Linux.

Parsing frontmatter on every file adds a small performance cost.

Very large folders can make the first scan slower when the app starts.
---------------------------------------
* RISKS

Files may get out of sync if the user edits the same note in multiple apps at the same time.

Symlinks and file permission issues can cause unexpected errors.

Users might accidentally delete or move important folders.

Invalid or broken markdown/frontmatter can break parsing.

Performance may degrade for extremely large note collections (10k+ files).
----------------------------------------
* MITIGATIONS

Handle file and parse errors gracefully instead of crashing the app.

Rebuild indexes in the background to avoid blocking the UI.

Ignore unsupported or broken files safely.

Allow users to limit which folders are watched.

Fall back to a full re-scan if the file watcher misses events.
--------------------------------------------

### 12. Summary
This architecture treats the local file system as the source of truth for markdown notes.
It ensures privacy, offline support, and long-term user ownership.
The design is simple, transparent, and extensible, making it suitable for building advanced features like search and AI on top without compromising user control.


### 13. RESPONSIBILITY

1️⃣ Where are notes stored?
Notes are stored as plain .md files on the user’s local file system.

2️⃣ How are they organized?
Notes are organized using folders and subfolders, just like normal files on a computer.

3️⃣ How does the app read them?
The app reads markdown files from disk and loads content only when a note is opened.

4️⃣ How does it detect changes?
A file watcher listens for create/update/delete events and updates the app in real time.

5️⃣ How does it scale?
It uses lazy loading, incremental indexing, and background scans to handle large collections.

6️⃣ How can AI sit on top later?
AI can build embeddings and search indexes on top of the local markdown files without owning the data.



