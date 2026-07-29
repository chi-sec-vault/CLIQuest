from ui import card, success, error, prompt, pause
from mentor import say

def quest_6():

    card(
        "🧭 QUEST 6 — LEAVE YOUR MARK",
        "You've built a room, Explorer.\n\n"
        "But an empty room is just a hollow space.\n"
        "A true base needs tools, records, and secrets."
    )

    pause()

    say(
        "Explorer...\n\n"
        "Every explorer needs a journal to record their findings,\n"
        "write their scripts, and store their data.\n\n"
        "In Linux, a file isn't created by opening a heavy application\n"
        "like Microsoft Word and clicking 'Save As'.\n\n"
        "It is created instantly, directly from the command line."
    )

    card(
        "🎯 MISSION",
        "Create a brand new, empty file called 'journal.txt'."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : touch\n\n"
        "Full Meaning : Touch (Create File)\n\n"
        "Simple Explanation:\n"
        "Creates a brand new, empty file.\n\n"
        "Think of it like tapping a blank piece of paper with your finger,\n"
        "and it instantly materializes on your desk."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "In Linux, file extensions like '.txt' aren't strictly required,\n"
        "but they are incredibly helpful for humans to remember what is inside.\n\n"
        "Always give your files clear names.\n\n"
        "Format: touch [filename]"
    )

    pause()

    card(
        "🖥️ DEMONSTRATION",
        "$ touch journal.txt\n\n"
        "Like 'cd' and 'mkdir', the system is completely silent if it succeeds.\n"
        "It creates the blank file and waits for your next move."
    )

    pause()

# Wrap input in a continuous loop for a smooth retry experience
    while True:

        command = prompt("Type the command to create your journal file")

        if command.strip().lower() == "touch journal.txt":

            say(
                "There it is.\n\n"
                "A blank page waiting for your commands.\n"
                "Your camp is fully established."
            )

            card(
                "🌍 FIELD MISSION",
                "Open your Linux terminal.\n\n"
                "If you just finished Quest 5, you should currently be standing inside your 'outpost' directory.\n\n"
                "Run this exact sequence:\n\n"
                "1. touch journal.txt   (To create your blank file)\n"
                "2. ls                  (To verify that your journal now sits on the desk)\n\n"
                "Press Enter when you're ready to continue."
            )

            pause()

            say(
                "Excellent work, Explorer.\n\n"
                "You now know how to look around, move, build, and create.\n\n"
                "You are officially a Linux user."
            )

            success(
                "Mission accomplished!\n\n"
                "You can now create files using the 'touch' command."
            )

            return True

        # Themed retry prompt for Chapter 6
        error(
            "The pen slipped on the blank page, Explorer. Take another look at the syntax and try writing the command again!"
        )
