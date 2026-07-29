from ui import card, success, error, prompt, pause
from mentor import say

def quest_4():

    card(
        "🧭 QUEST 4 — TAKING A STEP",
        "You know how to look around.\n\n"
        "Now, it's time to start walking."
    )

    pause()

    say(
        "Explorer...\n\n"
        "You've opened your eyes.\n"
        "You see the paths before you.\n\n"
        "But an explorer who never leaves their starting point\n"
        "isn't an explorer at all.\n\n"
        "They are just a guard."
    )

    say(
        "It's time to take your first step."
    )

    card(
        "📜 STORY",
        "Every folder in Linux is like a room in a massive castle.\n\n"
        "Right now, you are standing in the main hall.\n"
        "But the real secrets, the tools, and the hidden passages...\n"
        "They are located deeper inside.\n\n"
        "To find them, you must learn how to walk through doors."
    )

    pause()

    card(
        "🎯 MISSION",
        "Move forward into the 'data' directory."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : cd\n\n"
        "Full Meaning : Change Directory\n\n"
        "Simple Explanation:\n"
        "The 'cd' command moves you from your current folder\n"
        "into a new one."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "You don't just type 'cd' by itself.\n\n"
        "You must tell Linux WHERE you want to go.\n\n"
        "Format: cd [name_of_folder]"
    )

    pause()

    card(
        "🖥️ DEMONSTRATION",
        "$ cd data\n\n"
        "Notice something?\n"
        "Linux didn't print a massive fireworks display.\n\n"
        "If the command works, Linux is quiet.\n"
        "It simply places you in the new room and waits."
    )

    pause()

    say(
        "A tip from the wise, Explorer...\n\n"
        "Always use 'ls' before you use 'cd'.\n\n"
        "You cannot walk into a room that doesn't exist."
    )

# Wrap input in a continuous loop for a smooth retry experience
    while True:

        command = prompt("Type the command to move into the data directory")

        # We check for exactly "cd data"
        if command.strip().lower() == "cd data":

            say(
                "Excellent.\n\n"
                "You've just crossed the threshold."
            )

            card(
                "🌍 FIELD MISSION",
                "Open your Linux terminal.\n\n"
                "Run this exact sequence of commands:\n\n"
                "1. ls       (To look at the doors)\n"
                "2. cd data  (To walk through the door)\n"
                "3. pwd      (To prove to yourself that your location changed!)\n\n"
                "Press Enter when you're ready to continue."
            )

            pause() 

            say(
                "Welcome to a new room, Explorer.\n\n"
                "You are no longer just looking at the world.\n"
                "You are moving through it."
            )

            success(
                "Mission accomplished!\n\n"
                "You can now navigate between folders using the 'cd' command."
            )

            return True

        # Themed retry prompt that encourages them without handing them the exact string
        error(
            "You bumped into a closed door, Explorer. Take a breath and try the path again!"
        )
