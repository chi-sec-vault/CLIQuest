from ui import card, success, error, prompt, pause
from mentor import say

def quest_8():

    card(
        "🧭 CHAPTER 8 — READ THE SCROLL",
        "You wrote your thoughts into 'journal.txt' using nano, Explorer.\n\n"
        "But as a terminal master, you don't always want to open a whole text editor\n"
        "just to read a file."
    )

    pause()

    say(
        "Explorer...\n\n"
        "When you want to quickly check the contents of a configuration file, a log, or a note,\n"
        "you use **cat**.\n\n"
        "It instantly unrolls the file and streams the text right onto your screen."
    )

    card(
        "🎯 MISSION",
        "Display the contents of your 'journal.txt' file using the 'cat' command."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : cat\n\n"
        "Full Meaning : Concatenate\n\n"
        "Simple Explanation:\n"
        "Display the contents of a file directly in your terminal.\n\n"
        "💡 *Historical Note:*\n"
        "It means 'concatenate' because it was originally designed to link multiple files together, but today, everyone uses it just to read files!"
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Type 'cat' followed by the name of the file you want to read.\n\n"
        "Format: cat [filename]"
    )

    pause()

    card(
        "🖥️ DEMONSTRATION",
        "$ cat journal.txt\n\n"
        "The terminal simply spits out exactly what you wrote in nano, then waits for your next command."
    )

    pause()

    # Wrap input in a continuous loop for a smooth retry experience
    while True:

        command = prompt("Type the command to read your journal file")

        if command.strip().lower() == "cat journal.txt":

            say(
                "The words appear on your screen.\n\n"
                "Your records are secure, readable, and instantly accessible."
            )

            card(
                "🌍 FIELD MISSION",
                "Open your real terminal.\n\n"
                "Make sure you are in the folder where your 'journal.txt' lives, and run:\n\n"
                "cat journal.txt\n\n"
                "Press Enter when you're ready to continue."
            )

            pause()

            say(
                "Brilliant work, Explorer.\n\n"
                "Reading files with 'cat' is an essential daily habit for any Linux user."
            )

            success(
                "Mission accomplished!\n\n"
                "You can now read file contents using the 'cat' command."
            )

            return True

        # Themed retry prompt for Chapter 8
        error(
            "The scroll remains tightly sealed, Explorer. Check your syntax and make sure you're reading 'journal.txt' with cat!"
        )
