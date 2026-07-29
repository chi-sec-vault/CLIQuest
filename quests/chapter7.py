from ui import card, success, error, prompt, pause
from mentor import say

def quest_7():

    card(
        "🧭 CHAPTER 7 — THE SCRIBE'S QUILL",
        "You created your blank 'journal.txt' file, Explorer.\n\n"
        "But a blank page is useless if you cannot write your thoughts down.\n"
        "It is time to learn how to edit files directly in the terminal."
    )

    pause()

    say(
        "Explorer...\n\n"
        "In traditional operating systems, you double-click a file to open a text editor.\n"
        "In Linux, we use powerful command-line text editors like **nano**.\n\n"
        "Nano opens a clean, built-in text editor right inside your terminal window\n"
        "allowing you to type, save, and exit."
    )

    card(
        "🎯 MISSION",
        "Open your journal file for editing using the 'nano' command."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : nano\n\n"
        "Full Meaning : Nano's ANOther editor\n\n"
        "Simple Explanation:\n"
        "Opens a user-friendly text editor inside the terminal.\n\n"
        "💡 *Pro-Tip for Nano:*\n"
        "Once you type your message inside nano, press **Ctrl + O** then **Enter** to save, and **Ctrl + X** to exit."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Type 'nano' followed by the filename you want to edit.\n\n"
        "Format: nano [filename]"
    )

    pause()

    card(
        "🖥️ DEMONSTRATION",
        "$ nano journal.txt\n\n"
        "The screen transforms into an editor. You can type whatever you want, save it, and return to your prompt."
    )

    pause()

    # Wrap input in a continuous loop for a smooth retry experience
    while True:

        command = prompt("Type the command to open your journal in nano")

        if command.strip().lower() == "nano journal.txt":

            say(
                "The editor opens before your eyes.\n\n"
                "You type your first entry into the wasteland: 'Day 1: The outposts are holding strong.'\n"
                "You save your changes and exit back to safety."
            )

            card(
                "🌍 FIELD MISSION",
                "Open your real terminal and run:\n\n"
                "nano journal.txt\n\n"
                "Type a short sentence, save it (**Ctrl + O**, **Enter**), and exit (**Ctrl + X**).\n\n"
                "Press Enter when you're ready to continue."
            )

            pause()

            say(
                "Fantastic work, Explorer.\n\n"
                "You can now create files *and* write content inside them. Next up, we'll master reading and modifying them!"
            )

            success(
                "Mission accomplished!\n\n"
                "You have successfully used the 'nano' text editor."
            )

            return True

        # Themed retry prompt for Chapter 7
        error(
            "The inkwell is closed, Explorer. Check your syntax and make sure you're opening 'journal.txt' with nano!"
        )
