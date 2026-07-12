from user import get_user_name
from menu import show_main_menu
from quests.dispatcher import start_adventure
from engine import complete_quest
from ui import banner

banner()

name = get_user_name()

print(f"\n👋 Welcome back, {name}!")
print("Ready to conquer today's commands? 🚀")

while True:

    choice = show_main_menu(name)

    if choice == "1":
        completed = start_adventure()
        if completed:
            complete_quest()

        else:
            print("\n📚 Complete the quest to earn XP.")

    elif choice == "2":
        print("\n⚔️ Practice mode is under construction!")

    elif choice == "3":
        print("\n🤖 AI Assistant coming soon!")

    elif choice == "4":
        print("\n📖 Explorer Journal coming soon!")

    elif choice == "5":
        print("\n⚙️ Settings coming soon!")

    elif choice == "0":
        print(f"\n👋 See you on your next quest, {name}!")
        break

    else:
        print("\n❌ I didn't understand that option.")
