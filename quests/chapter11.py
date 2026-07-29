from ui import card, success, error, prompt, pause
from mentor import say

def quest_11():

    card(
        "🧭 CHAPTER 11 — MAKE A COPY",
        "The wasteland is unpredictable. Files can get deleted, corrupted, or accidentally overwritten.\n\n"
        "A true Explorer never relies on just one copy of their most important data."
    )

    pause()

    say(
        "Explorer...\n\n"
        "You've seen how easily data can be modified. Now you need to learn how to protect it.\n"
        "In Linux, we don't right-click and select 'Duplicate'. We use the **cp** command.\n\n"
        "It works almost exactly like 'mv', but instead of moving the file, it leaves the original intact and creates a perfect clone."
    )

    card(
        "🎯 MISSION",
        "Create a backup of 'logbook.txt'. Name the new file 'logbook.backup'."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : cp\n\n"
        "Full Meaning : Copy\n\n"
        "Simple Explanation:\n"
        "Creates a duplicate of a file or folder."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "The syntax is identical to the shape-shifter (mv):\n\n"
        "Format: cp [source] [destination]\n\n"
        "Example: cp notes.txt notes.copy"
    )

    pause()

    say(
        "Let's secure your records.\n"
        "Write the command to copy 'logbook.txt' and name the new duplicate 'logbook.backup'."
    )

    # Interactive Prompt for Copying - NO SPOON FEEDING
    while True:

        command = prompt("Type the command to back up your logbook")
        clean_command = command.strip().lower()

        # Success condition
        if clean_command == "cp logbook.txt logbook.backup":
            say(
                "Data secured.\n\n"
                "You now have two identical files. If one gets destroyed, the other survives."
            )
            break
        
        # Guided Error Handling
        if not clean_command.startswith("cp"):
            if "copy" in clean_command:
                error("You have the right idea, but Linux likes abbreviations. We just use 'cp'. Try again.")
            else:
                error("You need the copy command for this. Review the 'COMMAND' card above.")
        
        elif "logbook.txt" not in clean_command or "logbook.backup" not in clean_command:
            error("The system needs two filenames: the original file, and the name of the new backup. You are missing one (or spelled it wrong).")
            
        elif clean_command.find("logbook.backup") < clean_command.find("logbook.txt"):
            error("Careful with your aim! It is always [source] first, then [destination].")
            
        else:
            error("The syntax is a little off. Look closely at the format: cp [source] [destination]")

    pause()

    say(
        "Now, let's do it for real.\n\n"
        "Remember how you moved your logbook into the 'archives' folder in the last mission?\n"
        "You'll need to go inside that folder first to back it up!"
    )

    card(
        "🌍 FIELD MISSION",
        "Open your real terminal. We are going to stack your skills:\n\n"
        "1. Run: cd archives  (Navigate into the folder where your file lives)\n"
        "2. Run: ls  (Confirm 'logbook.txt' is sitting there)\n"
        "3. Run: cp logbook.txt logbook.backup  (Make the clone)\n"
        "4. Run: ls  (You should now see BOTH files!)\n"
        "5. Run: cd ..  (Return safely to your main base camp)\n\n"
        "Press Enter when you're ready to continue."
    )

    pause()

    say(
        "Excellent execution, Explorer.\n\n"
        "Backing up data before you make major changes is a habit that will save your life in cybersecurity."
    )

    success(
        "Mission accomplished!\n\n"
        "You can now duplicate files flawlessly using the 'cp' command."
    )

    return True
