import json


# Load the Explorer's progress
def load_progress():
    with open("data/progress.json", "r") as file:
        progress = json.load(file)

    return progress


# Save the Explorer's progress
def save_progress(progress):
    with open("data/progress.json", "w") as file:
        json.dump(progress, file, indent=4)


def complete_quest():
    progress = load_progress()

    progress["current_quest"] += 1
    progress["xp"] += 10

    save_progress(progress)

    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🎉 QUEST COMPLETE!")
    print("⭐ +10 XP")
    print(f"🧭 Current XP: {progress['xp']}")
    print(f"📜 Next Quest: {progress['current_quest']}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# Reset the Explorer's progress back to the beginning
def reset_progress():
    default_progress = {
        "current_campaign": 1,
        "current_quest": 1,
        "xp": 0
    }
    save_progress(default_progress)
