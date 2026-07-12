from ui import divider, page_header, prompt
from engine import load_progress


def show_main_menu(name):

    progress = load_progress()

    page_header(
        name=name,
        campaign="Linux Foundations",
        quest=progress["current_quest"],
        xp=progress["xp"]
    )

    print("\nChoose your next quest.\n")

    if progress["current_quest"] == 1:
        print("🧭 1. Begin Your Journey")
    else:
        print("🧭 1. Continue Adventure")

    print("⚔️ 2. Practice Arena")
    print("🤖 3. Ask CLIQuest")
    print("📖 4. Explorer Journal")
    print("⚙️ 5. Settings")
    print("🚪 0. Exit")

    divider()

    return prompt("Choose an option")
