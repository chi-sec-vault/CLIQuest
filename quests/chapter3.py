from ui import card, success, error, prompt, pause
from mentor import say

def quest_3():

    card(
        "🧭 QUEST 3 — WHAT'S AROUND ME?",
        "Every explorer must learn to observe\n"
        "before taking the next step."
    )

    pause()

    say(
        "Explorer...\n\n"
        "You now know who you are. (whoami)\n"
        "You know where you are. (pwd)\n\n"
        "But imagine standing in an unfamiliar room\n"
        "with your eyes closed.\n\n"
        "Would you start walking?"
    )
    
    pause()

    say(
        "Probably not.\n\n"
        "Wise explorers observe before they move.\n\n"
        "Linux rewards curiosity.\n\n"
        "Let's look around."
    )

    pause()

    card(
        "📜 STORY",
        "You arrive in an unfamiliar room.\n\n"
        "It could contain useful tools...\n"
        "Important documents...\n"
        "Or hidden passages.\n\n"
        "First, you must discover what surrounds you."
    )

    pause()

    card(
        "🎯 MISSION",
        "Reveal the files and folders in your current location."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : ls\n\n"
        "Meaning      : List\n\n"
        "Unlike 'pwd', 'ls' is not an acronym.\n"
        "It simply means 'List'."
    )

    pause()

    card(
        "💡 SIMPLE EXPLANATION",
        "The ls command displays everything inside\n"
        "your current directory.\n\n"
        "This includes files and folders."
    )

    pause()

    card(
        "🖥️ DEMONSTRATION",
        "$ ls\n\n"
        "app.py\n"
        "engine.py\n"
        "mentor.py\n"
        "quests\n"
        "data\n"
        "README.md\n\n"
        "Linux is showing everything that exists in your current location.\n"
        "Each name is either a file or a directory that you can explore."
    )

    pause()

    say(
        "Explorer...\n\n"
        "You'll use 'ls' more than almost any other Linux command.\n\n"
        "Whenever you feel lost...\n"
        "Look around first."
    )

    pause()

    command = prompt("Type the command that lists everything around you")

    if command.strip().lower() == "ls":

        say(
            "Excellent work, Explorer.\n\n"
            "You've opened your eyes.\n\n"
            "A wise explorer never walks blindly."
        )
        
        pause()

        card(
            "🌍 FIELD MISSION",
            "Open your Linux terminal.\n\n"
            "Run:\n\n"
            "ls\n\n"
            "Take a moment to observe the output.\n\n"
            "• Which files do you recognize?\n"
            "• Can you spot the CLIQuest folder?\n\n"
            "Press Enter when you're ready to continue."
        )

        pause() 

        say(
            "Welcome back, Explorer.\n\n"
            "Real explorers don't just study maps.\n"
            "They walk the terrain.\n\n"
            "Now you know what surrounds you.\n\n"
            "Next, you'll learn how to move through this world."
        )

        success(
            "Mission accomplished!\n\n"
            "You can now reveal the files and folders\n"
            "around you using the 'ls' command."
        )

        return True

    error(
        "Almost there, Explorer.\n\n"
        "The command you're looking for is:\n\n"
        "ls\n\n"
        "It lists the files and folders around you."
    )

    return False
