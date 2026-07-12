# 🏗️ CLIQuest Architecture

> "Simple systems grow into great software."

This document describes how CLIQuest is organized and why each part of the project exists.

Our goal is to keep the project clean, modular, scalable, and beginner-friendly.

---

# 🧭 Core Philosophy

Each file should have **one responsibility**.

If a file starts doing too many things, split it into smaller modules.

Small files are easier to read, test, maintain, and improve.

---

# 📁 Project Structure

```
CLIQuest/
│
├── app.py
├── menu.py
├── user.py
├── engine.py
│
├── quests/
│   ├── __init__.py
│   ├── chapter1.py
│   ├── chapter2.py
│   └── chapter3.py
│
├── data/
│   ├── user.txt
│   ├── progress.json
│   └── achievements.json
│
├── README.md
├── CURRICULUM.md
├── DESIGN_PHILOSOPHY.md
└── ARCHITECTURE.md
```

---

# 📄 File Responsibilities

## app.py

The application's entry point.

Responsibilities:

- Start CLIQuest
- Load the Explorer
- Display the main menu
- Hand control to other modules

app.py should never contain lesson content.

---

## menu.py

Responsible for displaying menus and collecting user choices.

Responsibilities:

- Main menu
- Settings menu
- Future campaign selection
- Achievement menus

menu.py should never teach commands.

---

## user.py

Responsible for everything related to the Explorer.

Responsibilities:

- Create new Explorer profile
- Load Explorer information
- Save Explorer information
- Personalize greetings

Future responsibilities:

- Learning preferences
- Accessibility settings
- Preferred language

---

## engine.py

The heart of CLIQuest.

Responsibilities:

- Track campaign progress
- Unlock quests
- Award XP
- Save progress
- Track completed quests
- Unlock achievements

The engine controls the adventure.

---

## quests/

Contains every learning quest.

Each chapter lives in its own file.

Example:

chapter1.py

Contains:

- Quest 1
- Quest 2
- Quest 3

No progress tracking happens here.

Quests only teach.

---

## data/

Stores user progress.

Example:

user.txt

Stores:

- Explorer name

progress.json

Stores:

- Current campaign
- Current quest
- XP
- Level

achievements.json

Stores:

- Badges
- Completed achievements
- Milestones

---

# 🔄 Application Flow

```
Start CLIQuest

↓

Load Explorer

↓

Load Progress

↓

Display Welcome Screen

↓

Display Main Menu

↓

Explorer Selects Option

↓

Engine Decides What Happens

↓

Quest Begins

↓

Explorer Completes Quest

↓

Engine Saves Progress

↓

Return to Menu
```

---

# 🧩 Module Communication

```
app.py

↓

menu.py

↓

engine.py

↓

quests/

↓

data/
```

Every module has a single responsibility.

---

# 🚀 Scalability

CLIQuest should grow by adding new modules, not by making old files larger.

When new features are added, create new files where appropriate.

Avoid large files with multiple responsibilities.

---

# 📚 Teaching Architecture

Every quest follows the same structure.

Story

↓

Mission

↓

Command Introduction

↓

Demonstration

↓

Explorer Guess

↓

Explanation

↓

Practice

↓

Celebration

↓

Reflection

---

# 🌟 Future Modules

Possible additions:

inventory.py

Handles badges, rewards, and collectibles.

mentor.py

Controls the AI mentor personality.

journal.py

Stores Explorer reflections and notes.

arena.py

Practice mode with challenges.

settings.py

User preferences and accessibility.

analytics.py

Tracks learning progress and command mastery.

---

# 🎯 Guiding Principle

Every new feature should answer three questions.

1. Does this improve learning?

2. Does this improve the Explorer's experience?

3. Does it belong in its current file?

If the answer to Question 3 is "no," create a new module.

---

# 🧭 Final Thought

CLIQuest is not just software.

It is an educational adventure.

Every module should make the Explorer feel more confident, more curious, and more excited to continue learning.
