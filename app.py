from user import get_user_name
from menu import show_main_menu
from quests.dispatcher import start_adventure
from engine import complete_quest, load_progress
from settings import show_settings
from ui import banner

banner()

name = get_user_name()

print(f"\n👋 Welcome back, {name}!")
print("Ready to conquer today's commands? 🚀")

while True:
    choice = show_main_menu(name)

    if choice == "1":
        # THE AUTO-LOAD LOOP
        while True:
            completed = start_adventure()
            
            if completed:
                complete_quest()
                print("\n✨ Loading next quest...\n")
                # Because it's a loop, it automatically goes back up 
                # and triggers start_adventure() for the next quest!
            else:
                break # If they fail or abort, break the loop and return to menu

    elif choice == "2":
        progress = load_progress()
        max_replay = progress["current_quest"] - 1
        
        if max_replay == 0:
            print("\n❌ You haven't completed any quests yet! Go play the campaign first.")
        else:
            print(f"\n✨ You have unlocked quests 1 through {max_replay}.")
            quest_to_replay = input("👉 Which quest number would you like to replay? ")
            
            try:
                q_num = int(quest_to_replay)
                
                if 1 <= q_num <= max_replay:
                    print(f"\n⏪ Replaying Quest {q_num}...\n")
                    
                    # We pass the specific quest number to your dispatcher
                    start_adventure(q_num)
                    
                    print("\n✅ Replay complete! Returning to menu.")
                else:
                    print(f"\n❌ Please enter a number between 1 and {max_replay}.")
                    
            except ValueError:
                print("\n❌ Invalid input. Please type a number.")

    elif choice == "3":
        print("\n⚔️ Practice mode is under construction!")

    elif choice == "4":
        print("\n🤖 AI Assistant coming soon!")

    elif choice == "5":
        print("\n📖 Explorer Journal coming soon!")

    elif choice == "6":
        show_settings()  

    elif choice == "0":
        print(f"\n👋 See you on your next quest, {name}!")
        break

    else:
        print("\n❌ I didn't understand that option.")
