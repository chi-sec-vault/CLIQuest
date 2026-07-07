def show_main_menu(name):
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🧭 CLIQuest")
    print(f"Explorer: {name}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    print("\nChoose your next quest.\n")

    print("🌱 1. Learn a Linux Command")
    print("⚔️ 2. Practice a Command")
    print("🤖 3. Ask CLIQuest")
    print("📖 4. Explorer Journal")
    print("⚙️ 5. Settings")
    print("🚪 0. Exit")

    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    choice = input("> ")

    return choice
