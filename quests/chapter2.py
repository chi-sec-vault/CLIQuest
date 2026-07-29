from ui import card, success, error, prompt, pause
from mentor import say

def quest_2():

    card(
        "🧭 QUEST 2 — WHERE AM I?",
        "Welcome back, Explorer!\n\n"
        "You've learned who you are.\n\n"
        "Now it's time to discover where you are."
    )

    pause()

    say(
        "Explorer...\n\n"
        "Knowing your name is only the beginning.\n\n"
        "Every explorer must also know where they stand.\n\n"
        "Without knowing your location,\n"
        "every step becomes a guess."
    )

    card(
        "🎯 MISSION",
        "Discover your current location inside the Linux filesystem."
    )

    pause()

    say(
        "This time, I won't simply give you the answer.\n\n"
        "Think carefully...\n\n"
        "What command could ask Linux where you are?"
    )

    card(
        "📖 COMMAND",
        "Command      : pwd\n\n"
        "Full Meaning : Print Working Directory\n\n"
        "Print        : Display information\n"
        "Working      : Your current active location\n"
        "Directory    : The folder you're currently in\n\n"
        "Simple Explanation:\n"
        "Shows the exact folder you're currently inside."
    )

    pause()

    card(
        "🖥️ DEMONSTRATION",
        "$ pwd\n\n"
        "/home/hope/CLIQuest\n\n"
        "Linux has revealed your current location."
    )

    pause()

# Wrap input in a continuous loop for a smooth retry experience
    while True:

        command = prompt("Type the command exactly as shown")

        if command.strip().lower() == "pwd":

            say(
                "Interesting...\n\n"
                "Curiosity has guided you well.\n\n"
                "Let's see where Linux says you are..."
            )

            card(
                "🌍 FIELD MISSION",
                "Open your Linux terminal.\n\n"
                "Run:\n\n"
                "pwd\n\n"
                "Take a moment to observe the output.\n\n"
                "• Where are you currently standing in your machine?\n\n"
                "Press Enter when you're ready to continue."
            )
            
            pause()

            say(
                "Welcome back, Explorer.\n\n"
                "You now know two important things.\n\n"
                "Who you are.\n"
                "Where you are.\n\n"
                "A true explorer is never lost.\n\n"
                "But tell me...\n\n"
                "What surrounds you?\n\n"
                "We'll discover that in your next quest."
            )

            success(
                "Mission accomplished!\n\n"
                "Linux has revealed your current location using the 'pwd' command."
            )

            return True

# Themed retry prompt for Chapter 2
        error(
            "You wandered off the map, Explorer. Take a breath and check your coordinates again!"
        )
