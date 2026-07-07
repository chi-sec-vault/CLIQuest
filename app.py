from user import get_user_name
from menu import show_main_menu

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("        🧭 CLIQuest")
print("   Learn Linux One Quest at a Time")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

name = get_user_name()

print(f"\n👋 Welcome back, {name}!")
print("Ready to conquer today's commands? 🚀")

choice = show_main_menu(name)

print(f"\nYou selected option {choice}.")
