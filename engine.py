import json
import os

# Load the Explorer's progress
def load_progress():
    default_progress = {
        "current_campaign": 1,
        "current_quest": 1,
        "xp": 0
    }
    
    try:
        with open("data/progress.json", "r") as file:
            saved_data = json.load(file)
            
            # The "Old Save" Fix: Check for missing labels and add them
            for key, value in default_progress.items():
                if key not in saved_data:
                    saved_data[key] = value
                    
            return saved_data
            
    except FileNotFoundError:
        # If the file is missing (new player), start them at the beginning!
        return default_progress
        
    except json.JSONDecodeError:
        # The "Corrupted Save" Fix: If the file is blank or broken, start fresh
        return default_progress

# Save the Explorer's progress
def save_progress(progress):
    # Make sure the 'data' folder exists before we try to put a file inside it
    if not os.path.exists("data"):
        os.makedirs("data")
        
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
