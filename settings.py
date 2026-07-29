from ui import card, prompt, success, error, pause
from engine import reset_progress, load_progress

# Import your individual quests so we can replay them directly
from quests.chapter1 import quest_1
from quests.chapter2 import quest_2
from quests.chapter3 import quest_3
from quests.chapter4 import quest_4
from quests.chapter5 import quest_5
from quests.chapter6 import quest_6

def show_settings():
    # Map quest numbers to their respective functions
    quest_map = {
        1: quest_1,
        2: quest_2,
        3: quest_3,
        4: quest_4,
        5: quest_5,
        6: quest_6
    }

    while True:
        card(
            "⚙️ SETTINGS",
            "Manage your CLIQuest adventure preferences and progress data."
        )
        
        print("\n1. 🔄 Replay a Specific Quest")
        print("2. ⚠️ Reset Entire Adventure (Start over from Quest 1)")
        print("3. 🔙 Return to Main Menu\n")
        
        choice = prompt("Choose an option")
        
        if choice == "1":
            progress = load_progress()
            max_unlocked = progress.get("current_quest", 1)
            
            print(f"\n🗺️ LEVEL REPLAY (Unlocked up to Quest {max_unlocked})")
            print("You can replay any quest you've already reached.")
            
            quest_choice = prompt("Enter the quest number you want to replay (or 'b' to go back)").strip().lower()
            
            if quest_choice == 'b':
                continue
                
            try:
                q_num = int(quest_choice)
                if 1 <= q_num <= max_unlocked:
                    print(f"\n🚀 Launching Quest {q_num} for practice...")
                    pause()
                    
                    # Run the requested quest function
                    quest_map[q_num]()
                    
                    success(f"Practice complete! Returning to Settings.")
                    pause()
                else:
                    error(f"You haven't unlocked Quest {q_num} yet, or it's out of range!")
                    pause()
            except ValueError:
                error("Please enter a valid number.")
                pause()
                
        elif choice == "2":
            print("\n⚠️ WARNING: This will erase all your progress and XP!")
            confirm = prompt("Are you sure you want to start over? Type 'yes' to confirm").strip().lower()
            
            if confirm == "yes":
                reset_progress()
                success("Adventure reset! Your journey begins anew at Quest 1.")
                pause()
                return True
            else:
                print("\n👍 Reset cancelled. Your progress is safe.")
                pause()
                
        elif choice == "3" or choice == "0":
            break
        else:
            error("Invalid choice. Please pick from the options above.")
            pause()
