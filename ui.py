WIDTH = 60


def divider():
    """Print a horizontal divider."""
    print("━" * WIDTH)


def blank():
    """Print a blank line."""
    print()


def center(text):
    """Center text on the terminal."""
    print(text.center(WIDTH))


def banner():
    """Display the CLIQuest banner."""
    divider()
    center("🧭 CLIQuest")
    center("Learn Linux One Quest at a Time")
    divider()


def page_header(name, campaign, quest, xp):
    """Display Explorer information."""
    blank()
    print(f"🧑 Explorer : {name}")
    print(f"🗺️ Campaign : {campaign}")
    print(f"📜 Quest    : {quest}")
    print(f"⭐ XP       : {xp}")
    divider()


def card(title, body):
    """Display a content card."""
    blank()
    divider()
    print(title)
    divider()
    blank()
    print(body)
    blank()
    divider()


def success(message):
    """Display a success message."""
    blank()
    divider()
    print("🎉 SUCCESS")
    divider()
    print(message)
    divider()


def error(message):
    """Display an error message."""
    blank()
    divider()
    print("❌ Oops!")
    divider()
    print(message)
    divider()


def prompt(message):
    """Display a styled input prompt."""
    return input(f"\n👉 {message}: ")

def pause():
    input("\nPress Enter to continue...")
