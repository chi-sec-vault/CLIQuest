from ui import card, success, error, prompt, pause
from mentor import say

def quest_20():

    card(
        "🧭 CAMPAIGN 3: GUARDIANS OF LINUX — CHAPTER 20",
        "The Long View\n\n"
        "Seeing hidden files is only half the battle.\n"
        "A Guardian needs both sight and detail: permissions, ownership, and size."
    )

    pause()

    say(
        "You've learned how to uncover hidden files with '-a'.\n\n"
        "But in the real world, an analyst doesn't run two separate commands to investigate a directory.\n"
        "They combine flags. They want to see the hidden files *and* the detailed permissions, sizes, and modification dates all at once."
    )

    card(
        "🎯 MISSION",
        "List all files, including hidden dotfiles, in meticulous long format."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : ls -la\n\n"
        "Full Meaning : List All in Long Format\n\n"
        "Simple Explanation:\n"
        "By merging '-a' (all files) with '-l' (long format), Linux gives you a complete metadata breakdown\n"
        "of everything in your directory in a single glance."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Format: ls -la [directory]\n\n"
        "Example: ls -la ~\n\n"
        "Pro-Tip: You can chain flags together in Linux. 'ls -la' and 'ls -al' do the exact same thing!"
    )

    pause()

    say(
        "Let's practice combining our sight and detail in the simulator."
    )

    # Interactive Prompt for ls -la
    while True:
        command = prompt("Type the command to list all files in long format")
        clean_command = command.strip().lower()

        if clean_command in ["ls -la", "ls -al", "ls -l -a", "ls -a -l"]:
            say(
                "Look at that cascade of text.\n\n"
                "You're seeing permissions on the left, owners in the middle, and hidden files all together.\n"
                "That is the core signature of a Linux professional."
            )
            break
        
        if clean_command == "ls -l":
            error("That gives you the detailed long format, but it's still blind to the hidden dotfiles. Add the 'all' flag!")
        elif clean_command == "ls -a":
            error("That uncovers the hidden files, but we also need the detailed long format. Add the 'long' flag!")
        elif not clean_command.startswith("ls"):
            error("We're still using our trusty list command ('ls'). Try combining the 'all' and 'long' flags.")
        else:
            error("Close! Think about how Linux lets you chain flags together after 'ls'.")

    pause()

    say(
        "You're mastering the Guardian's primary view. Let's take this to your actual machine."
    )

    card(
        "🌍 FIELD MISSION",
        "Let's inspect your real Kali home directory with full metadata.\n\n"
        "Open your real Kali terminal and run:\n"
        "ls -la ~\n\n"
        "Look closely at the output. Those letters on the left (like -rw-r--r--) are permissions.\n"
        "The names next to them are file owners. You are looking at the raw blueprint of the system.\n\n"
        "Press Enter here once you've examined your real home directory."
    )

    pause()

    success(
        "Mission accomplished!\n\n"
        "You've mastered the long view. Next, we step into administrative territory: The Key to the Kingdom."
    )

    return True
