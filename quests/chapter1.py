from ui import card, success, error, prompt, pause
from mentor import say

def quest_1():

    card(
        "🧭 QUEST 1 — WHO AM I?",
        "Welcome to your first quest!\n\n"
        "Today you'll learn your very first Linux command."
    )

    pause()

    say(
        "Welcome, Explorer.\n\n"
        "Every Linux journey begins with curiosity.\n\n"
        "Today, you'll learn your very first Linux command.\n\n"
        "Take your time.\n\n"
        "Every Linux professional once stood exactly where you are now."
    )

    card(
        "🎯 MISSION",
        "Discover your current Linux username."
    )

    pause()

    say(
        "Explorer...\n\n"
        "Imagine you've just logged into a Linux machine you've never used before.\n\n"
        "Before you explore...\n"
        "Before you change anything...\n\n"
        "Wouldn't you first want to know who is currently signed in?\n\n"
        "Let's discover the command that answers that question."
    )

    card(
        "📖 COMMAND",
        "Command      : whoami\n\n"
        "Full Meaning : Who Am I\n\n"
        "Explanation  : Displays the username of the person currently logged into Linux."
    )

    pause()

    command = prompt("Type the command exactly as shown")

    if command.strip().lower() == "whoami": # Added .lower() for safety

        say(
            "Interesting...\n\n"
            "So you believe that's the correct command?\n\n"
            "Let's find out..."
        )

        card(
            "🌍 FIELD MISSION",
            "Open your Linux terminal.\n\n"
            "Run:\n\n"
            "whoami\n\n"
            "Take a moment to observe the output.\n\n"
            "• Did it print your username?\n\n"
            "Press Enter when you're ready to continue."
        )

        pause()

        say(
            "Welcome back, Explorer.\n\n"
            "You didn't just learn a command.\n\n"
            "You learned the very first question every Linux user asks.\n\n"
            "'Who am I?'\n\n"
            "Our journey has only just begun."
        )
        
        success(
            "Mission accomplished!\n\n"
            "You can now discover your identity using the 'whoami' command."
        )

        return True

    error(
        "Not quite.\n\n"
        "The correct command is:\n\n"
        "whoami"
    )

    return False
