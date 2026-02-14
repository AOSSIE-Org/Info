###### Discord–GitHub Sync Bot

### 1. Background

As open-source organizations grow, managing both Discord and GitHub becomes difficult.

For example:

A contributor merges 5 PRs on GitHub

But someone still has to manually give them a "Contributor" role on Discord

Maintainers manually assign issues

No automatic tracking of who is active

This takes time and often becomes messy.

I noticed that many Discord bots exist. Many GitHub apps exist.
But there is no simple, self-hosted tool that connects both properly for open-source communities.

That is the motivation behind this project.

### 2. Problem Statement

Organizations like AOSSIE manage:

GitHub repositories

Discord communities

Many contributors

Mentors and maintainers


Currently:

Roles are given manually
Issue assignments are manual
PR reviews are manually requested
Contribution tracking is not transparent
Recognition is inconsistent
As the organization grows, this becomes harder to manage.
We need automation between GitHub and Discord.

### 3. Proposed Solution

Build a simple, configurable Discord–GitHub Bot that:

Runs locally (no mandatory cloud server)

Syncs GitHub activity with Discord roles

Assigns issues automatically

Tracks contributions and assigns tokens

Can be reused by other open-source organizations

### 4. Core Features (Explained with Examples)
* Feature 1: GitHub Activity → Discord Role Sync

If someone:

Merges 5 PRs → Automatically gets Contributor

Merges 20 PRs → Gets Core Contributor

Reviews 10 PRs → Gets Reviewer

Example:

Tuba merges 5 PRs.
The bot checks GitHub API.
It updates her Discord role automatically.

No manual work required.


* Feature 2: Discord Role → GitHub Issue Assignment

Suppose we have Discord roles like:

Frontend

Backend

Documentation

If a new issue is labeled frontend on GitHub:

The bot automatically suggests or assigns it to users who have Frontend role in Discord.

This reduces maintainer workload.


* Feature 3: Contribution Scoring System

Each action earns points.

Example:

Action	Points
PR merged-> 	+10
Issue closed-> 	+5
PR review-> 	+7
Documentation PR-> 	+3

Users can type:
{/myscore}


And see:

You have 87 contribution points this month.
This creates transparency and motivation.

* Feature 4: Configurable System

Every organization is different.

So the bot will allow:

Custom role mapping
Custom scoring rules
Custom thresholds
Enable/disable features
All configurable using a simple JSON/YAML file.

### 5. Technical Approach
Architecture Overview

Discord Bot Layer (handles commands and roles)

GitHub API Layer (fetches PRs, issues, reviews)

Sync Engine (logic for automation)

Local Database (SQLite)

Config Manager

*   Why Local Execution?

According to requirements:

Should run on any computer
Should not require cloud hosting
Should not require 24/7 uptime

So:

The bot will:

Fetch GitHub activity when started
Sync roles
Update database
Exit safely if needed

### 6. Why This Project is Important

For mentors:

Saves time
Reduces manual role management
Improves issue assignment workflow

For contributors:

Fair recognition
Transparent contribution tracking
Motivational system

For organizations:

Scalable
Reusable
Open-source friendly


### 7. Future Scope

After MVP:

Web dashboard
Leaderboard system
Monthly contribution summary
Badge system
Multi-org support


### 8. Tech Stack (Proposed)

Python

discord.py

GitHub REST / GraphQL API

SQLite

Docker (optional)