from ui import card, success, error, prompt, pause
from mentor import say

def quest_19():

    card(
        "🧭 CAMPAIGN 3: GUARDIANS OF LINUX — CHAPTER 19",
        "The Blind Spot\n\n"
        "Attackers don't leave their tracks sitting in plain sight.\n"
        "They hide their tools in the shadows—inside files starting with a dot.\n"
        "Right now, your standard view is completely blind to them."
    )

    pause()

    say(
        "Take a breath, Explorer. In Campaign 2, we tracked down logs and scripts,\n"
        "but a true Guardian knows that what you *don't* see can hurt you.\n\n"
        "If you look at your home directory right now with ordinary commands, everything looks clean.\n"
        "But Linux keeps quiet configuration files, history logs, and settings tucked away out of sight."
    )

    card(
        "🎯 MISSION",
        "Reveal everything lurking in the shadows of your home directory."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : ls -a\n\n"
        "Full Meaning : List All (including hidden files starting with a dot)\n\n"
        "Simple Explanation:\n"
        "By default, Linux hides any file or folder that starts with a dot (dotfiles).\n"
        "Adding the '-a' flag lifts the blindfold and shows you everything."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Format: ls -a [directory]\n\n"
        "Example: ls -a\n\n"
        "Pro-Tip: Attackers love using dotfiles because standard system checks ignore them completely."
    )

    pause()

    say(
        "Let's practice spotting the hidden files in our simulator first."
    )

    # Interactive Prompt for ls -a
    while True:
        command = prompt("Type the command to list all files, including hidden ones")
        clean_command = command.strip().lower()

        if clean_command in ["ls -a", "ls -al", "ls -la"]:
            say(
                "Spot on.\n\n"
                "Suddenly, files like .bashrc and .config appear out of nowhere."
            )
            break
        
        if not clean_command.startswith("ls"):
            if "cd" in clean_command:
                error("We aren't moving folders right now; we want to see what's already around us.")
            else:
                error("We're starting with our old friend the 'list' command ('ls'). Try adding the flag for 'all'.")
        elif clean_command == "ls":
            error("That's the standard view! It hides anything starting with a dot. We need the flag that shows ALL files.")
        else:
            error("Close! Just the base command to list files, followed by a space and the flag for 'all'.")

    pause()

    say(
        "You're getting the hang of it. Now let's take this to your actual machine."
    )

    card(
        "🌍 FIELD MISSION",
        "Let's check your real Kali home directory for hidden files.\n\n"
        "Open your real Kali terminal and run:\n"
        "ls -a ~\n\n"
        "Look at all those dotfiles! Those are the hidden configuration files that shape your user environment.\n\n"
        "Press Enter here once you've lifted the blindfold on your real machine."
    )

    pause()

    success(
        "Mission accomplished!\n\n"
        "You've lifted the blindfold. Next, we combine sight with detailed inspection."
    )

    return True
