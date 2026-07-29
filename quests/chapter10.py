from ui import card, success, error, prompt, pause
from mentor import say

def quest_10():

    card(
        "🧭 CHAPTER 10 — THE SHAPE SHIFTER",
        "Your camp is established. Your journal is written.\n\n"
        "But as your outpost grows, things will get messy.\n"
        "You need to know how to organize your files and give them better names."
    )

    pause()

    say(
        "Explorer...\n\n"
        "In Windows or macOS, you right-click a file to rename it, and you click-and-drag to move it.\n\n"
        "In Linux, we do both of these things with a single, shape-shifting command: **mv**.\n"
        "To the computer, renaming a file and moving a file are exactly the same thing—you are just giving the file a new path."
    )

    card(
        "🎯 MISSION",
        "Rename your 'journal.txt' to something more professional: 'logbook.txt'."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : mv\n\n"
        "Full Meaning : Move\n\n"
        "Simple Explanation:\n"
        "Moves a file to a new location, OR renames it if you keep it in the same folder."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "The syntax is always: mv [source] [destination]\n\n"
        "To Rename : mv old_name.txt new_name.txt\n"
        "To Move   : mv file.txt folder_name/"
    )

    pause()

    say(
        "Don't worry about making mistakes here. If you accidentally rename a file to the wrong thing,\n"
        "you can always just shape-shift it back!\n\n"
        "Let's practice renaming your journal first."
    )

    # Interactive Prompt for Renaming - NO SPOON FEEDING
    while True:

        command = prompt("Type the command to rename 'journal.txt' to 'logbook.txt'")
        clean_command = command.strip().lower()

        # Success condition
        if clean_command == "mv journal.txt logbook.txt":
            say(
                "Like magic.\n\n"
                "The file 'journal.txt' vanishes, and 'logbook.txt' instantly takes its place with all your text perfectly intact."
            )
            break
        
        # Guided Error Handling
        if not clean_command.startswith("mv"):
            if "rename" in clean_command:
                error("Good guess, but Linux doesn't use a 'rename' command for this. We use the shape-shifter. Try again.")
            else:
                error("You need the shape-shifter command to do this. Review the 'COMMAND' card above.")
        
        elif "journal.txt" not in clean_command or "logbook.txt" not in clean_command:
            error("The system needs two pieces of information: the current name of the file, and the new name. You are missing one.")
            
        elif clean_command.find("logbook.txt") < clean_command.find("journal.txt"):
            error("Watch your order, Explorer! It is always [source] first, then [destination].")
            
        else:
            error("The syntax is a little off. Look closely at the format: mv [source] [destination]")

    pause()

    say(
        "Now, let's prove it works as a mover, too.\n\n"
        "In the real terminal, you are going to create an 'archives' folder, rename your journal, and then move it inside."
    )

    card(
        "🌍 FIELD MISSION",
        "Open your real terminal. We are going to combine your past skills with your new one:\n\n"
        "1. Run: mv journal.txt logbook.txt  (This renames it)\n"
        "2. Run: ls  (Notice 'journal.txt' is gone, but 'logbook.txt' is there!)\n"
        "3. Run: mkdir archives  (Create a new folder to hold old logs)\n"
        "4. Run: mv logbook.txt archives/  (This moves the file into the folder)\n"
        "5. Run: ls archives/  (To peek inside the folder and confirm it's safe!)\n\n"
        "Press Enter when you're ready to continue."
    )

    pause()

    say(
        "Brilliant work.\n\n"
        "You aren't just learning commands anymore—you are chaining them together to control your system."
    )

    success(
        "Mission accomplished!\n\n"
        "You can now rename and move files flawlessly using the 'mv' command."
    )

    return True
