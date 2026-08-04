# 🧭 CLIQuest Curriculum

> **Learn Linux. One Quest at a Time.**

## Overview

CLIQuest is not a Linux tutorial.

It is an interactive learning adventure designed to help beginners become confident Linux users through storytelling, demonstrations, exploration, and hands-on practice.

Every command should solve a real problem.

Every quest should build confidence.

Every Explorer should feel safe to learn, make mistakes, and ask questions.

---

# 🎯 Learning Objectives

By completing CLIQuest, every Explorer should be able to:

- Understand fundamental Linux concepts.
- Navigate the Linux terminal confidently.
- Understand what Linux commands mean instead of memorizing them.
- Solve real-world Linux problems.
- Develop confidence through practice and repetition.
- Think like a Linux user instead of simply remembering commands.

---

# 📚 CLIQuest Teaching Standard

Every quest follows the same teaching structure to create true understanding.

---

## 🌍 1. Story
Every lesson begins with a story. Stories create curiosity and provide context before introducing a command.

## 🎯 2. Mission
Every quest gives the Explorer a clear, actionable mission.

## 📖 3. Command Introduction
Every command is introduced with its true meaning, origin, and a simple explanation.

## 🎭 4. Demonstration
Show the command in action before fully explaining it, allowing the Explorer to observe and learn.

## 🤔 5. Let the Explorer Guess
Prompt the Explorer to think critically about what the command does before they type it.

## 💡 6. Explanation
Explain technical terms instantly using plain language (e.g., Directory = Folder, Path = Location).

## 🌍 7. The Field Mission (Breaking the 4th Wall)
CLIQuest is a guide, not a simulator. Every quest forces the Explorer to leave the game, open their actual Linux terminal, and execute the command in the real world. Learning happens in the game; confidence happens in the real terminal.

## 🎉 8. Celebration & Reflection
Celebrate completed quests, reinforce key mindsets (like *"Linux rewards curiosity"*), and tie the lesson into the next step of the journey.

---

# 🌍 Campaign 1 — Welcome to Linux

## Story

Congratulations, Explorer!

You've just joined a cybersecurity team. Your mentor has handed you access to a Linux terminal.

Your first mission is simple: **Learn how to survive.**

Every quest introduces one command and one new idea.

---

## 🧭 Quest 1 — Who Am I?
- **Command:** `whoami`
- **Simple Explanation:** Show the username of the person currently using Linux.

## 🧭 Quest 2 — Where Am I?
- **Command:** `pwd`
- **Simple Explanation:** Show me the folder I'm currently in.

## 🧭 Quest 3 — What's Around Me?
- **Command:** `ls`
- **Simple Explanation:** Show the files and folders in my current location.

## 🧭 Quest 4 — Time to Explore
- **Command:** `cd`
- **Simple Explanation:** Move from one folder to another.

## 🧭 Quest 5 — Build Your Base
- **Command:** `mkdir`
- **Simple Explanation:** Create a new folder.

## 🧭 Quest 6 — Leave Your Mark
- **Command:** `touch`
- **Simple Explanation:** Create a brand new, empty file.

## 🧭 Quest 7 — The Scribe's Quill
- **Command:** `nano`
- **Simple Explanation:** Open a user-friendly text editor inside the terminal.

## 🧭 Quest 8 — Read the Scroll
- **Command:** `cat`
- **Simple Explanation:** Display the contents of a file.

## 🧭 Quest 9 — The Stream Director
- **Command:** `echo` & Redirection (`>`, `>>`)
- **Simple Explanation:** Send text directly into a file without opening an editor.

## 🧭 Quest 10 — The Shape Shifter
- **Command:** `mv`
- **Simple Explanation:** Move a file or rename it.

## 🧭 Quest 11 — Make a Copy
- **Command:** `cp`
- **Simple Explanation:** Create a duplicate of a file or folder.

## 🧭 Quest 12 — Leave No Trace
- **Command:** `rm` / `rmdir`
- **Simple Explanation:** Delete files or empty folders.

---

# 🏁 Final Mission — Operation: Lost Evidence

A senior cybersecurity analyst accidentally left important evidence somewhere on a Linux server.

Your mission is to find it, navigate through the system, organize the evidence, make a backup, and prepare it for investigation.

**Achievement Unlocked:** 🏅 *Linux Survivor*

---
# 🔍 Campaign 2 — Linux Detective

## Story
Now that you know how to navigate and manage files, it's time to find needles in haystacks. A rogue agent is moving through the system, and you need to track them down using advanced search, filtering, and inspection tools.

---

## 🧭 Chapter 13 — The Grid Search
- **Command:** `find`
- **Simple Explanation:** Search the live filesystem dynamically based on criteria like names or types.

## 🧭 Chapter 14 — The Index Query
- **Command:** `locate`
- **Simple Explanation:** Instantly search a pre-built system index instead of crawling the hard drive.

## 🧭 Chapter 15 — The Filter
- **Command:** `grep`
- **Simple Explanation:** Search inside text files for specific words or patterns.

## 🧭 Chapter 16 — The Assembly Line
- **Command:** `|` (The Pipe)
- **Simple Explanation:** Connect multiple tools together so data flows directly from one to the next.

## 🧭 Chapter 17 — The Sneak Peek
- **Command:** `head`
- **Simple Explanation:** Instantly view the first 10 lines of a massive file without flooding your screen.

## 🧭 Chapter 18 — The Stakeout
- **Command:** `tail`
- **Simple Explanation:** Read the most recent entries at the end of a log file or watch events live (`-f`).

---

# 🏁 Campaign 2 Final Exam — The Rogue Agent

A rogue agent has infiltrated the system and is tampering with files. Using `locate`, `tail`, and the Pipe operator with real system files, you track them down and lock them out.

**Achievement Unlocked:** 🎖️ *The Linux Detective Badge*

---

# 🛡️ Campaign 3 — Guardians of Linux

## Story
You tracked down the rogue agent's tracks in Campaign 2, but the threat isn't over. To truly secure the server, you must step up from a Detective to a Guardian—learning to reveal hidden files, inspect permissions, wield administrative authority, and lock down system assets.

---

## 🧭 Chapter 19 — The Blind Spot
- **Command:** `ls -a`
- **Simple Explanation:** Reveal hidden dotfiles (like `.bashrc`) that normal `ls` ignores.

## 🧭 Chapter 20 — The Long View
- **Command:** `ls -la`
- **Simple Explanation:** Combine sight (`-a`) and detailed inspection (`-l`) to reveal permissions, ownership, file size, and dates.

## 🧭 Chapter 21 — The Surgical Strike
- **Command:** `sudo`
- **Simple Explanation:** Temporarily execute a single command with root privileges.

## 🧭 Chapter 22 — The Master Key
- **Command:** `su` / `su root`
- **Simple Explanation:** Swap your entire active user session to the root administrator.

## 🧭 Chapter 23 — The Watchtower
- **Command:** `id`
- **Simple Explanation:** Display your numerical User ID (UID), Group ID (GID), and group memberships.

## 🧭 Chapter 24 — The Locksmith
- **Command:** `chmod`
- **Simple Explanation:** Add or remove read (`r`), write (`w`), or execute (`x`) permissions on a file.

## 🧭 Chapter 25 — The Title Deed
- **Command:** `chown`
- **Simple Explanation:** Reassign ownership of a file to a new user.

---

# 🏁 Campaign 3 Final Mission — The Vault Lockdown

An automated security protocol has locked down the server. You must bypass the lockdown, claim an override file, and execute it using `id`, `sudo`, `su`, `chown`, and `chmod` in a high-stakes sequence.

**Achievement Unlocked:** 🛡️ *Guardian of Linux*

---

# 🌐 Campaign 4 — Network Explorer

## Story
Up until now, you've been exploring a single island: your own local machine. But Linux is built for the open ocean. It's time to make contact with the outside world, discover your network identity, and interact with remote servers.

---

## 🧭 Chapter 26 — The Sonar
- **Command:** `ping`
- **Full Meaning:** Packet InterNet Groper
- **Simple Explanation:** Send a network pulse to a remote server to verify it is online and reachable.

## 🧭 Chapter 27 — The Address Book
- **Command:** `ip a` (or `ifconfig`)
- **Full Meaning:** IP Address
- **Simple Explanation:** Discover your machine's own network identity and local IP address.

## 🧭 Chapter 28 — The Downloader
- **Command:** `wget`
- **Full Meaning:** Web Get
- **Simple Explanation:** Pull files and tools directly from the internet into your terminal.

## 🧭 Chapter 29 — The Radar
- **Command:** `ss` / `netstat`
- **Full Meaning:** Socket Statistics
- **Simple Explanation:** Scan your own system to see what network ports are open and listening.

*(Boss Fight to be mapped out!)*

---
# 🚀 Future Campaigns

- **Campaign 5 — System Defender:** Apply Linux skills to security scenarios using `ssh`, `scp`, and `systemctl`.
- **Campaign 6 — Shell Master:** Master advanced bash scripting, aliases, and automation.
