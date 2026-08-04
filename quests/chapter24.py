from ui import card, success, error, prompt, pause
from mentor import say

def quest_24():

    card(
        "🧭 CAMPAIGN 3: GUARDIANS OF LINUX — CHAPTER 24",
        "The Locksmith\n\n"
        "You've downloaded a powerful security script. You try to run it.\n"
        "Linux says: 'Permission denied.'\n\n"
        "The system isn't broken. It's protecting you. By default, Linux locks files so they cannot be executed as programs."
    )

    pause()

    say(
        "Think back to when we used 'ls -la', Explorer.\n\n"
        "Remember those weird letters on the left side of the screen? Like '-rw-r--r--'?\n"
        "Those are the locks. 'r' means Read. 'w' means Write.\n\n"
        "Notice what's missing? The letter 'x' for eXecute. Without that 'x', a file is just dead text. "
        "To bring a script to life, you have to act as the locksmith and add the execute permission."
    )

    card(
        "🎯 MISSION",
        "Change the permissions of a file to make it executable."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : chmod\n\n"
        "Full Meaning : Change Mode\n\n"
        "Simple Explanation:\n"
        "It modifies the read, write, and execute permissions (the 'mode') of a file."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Format: chmod [permissions] [filename]\n\n"
        "Example: chmod +x script.sh\n\n"
        "Pro-Tip: The '+x' literally means 'add execute'. It is the most common way hackers and developers wake up their scripts."
    )

    pause()

    say(
        "Let's forge our first key in the simulator. Imagine you have a file named 'scanner.sh'."
    )

    # Interactive Prompt for chmod
    while True:
        command = prompt("Type the command to add execute permissions to 'scanner.sh'")
        clean_command = command.strip().lower()

        if clean_command == "chmod +x scanner.sh":
            say(
                "Click.\n\n"
                "The lock turns. The file is no longer just a text document; it is now a live program ready to run."
            )
            break
        
        if clean_command.startswith("chown"):
            error("That command changes *who* owns the file. Right now, we want to change the file's *mode* or permissions.")
        elif clean_command.startswith("sudo"):
            error("You usually don't need root power if you already own the file! Let's just use the base command to change the mode.")
        elif not clean_command.startswith("chmod"):
            error("Not quite. Think about the command that stands for 'Change Mode'.")
        elif "+x" not in clean_command:
            error("You brought the locksmith's tool, but you didn't tell it what to do! How do we 'add' the 'execute' permission?")
        elif "scanner.sh" not in clean_command:
            error("The tool is ready, and the key is cut, but what file are we unlocking? Don't forget your target.")
        else:
            error("Almost! Check your spacing. It should be the command, the permission change, and then the filename.")

    pause()

    say(
        "You understand the theory. Now, I want you to see the locks change with your own eyes."
    )

    card(
        "🌍 FIELD MISSION",
        "Let's make a file executable on your real Kali machine.\n\n"
        "Open your real terminal and follow these exact steps:\n"
        "1. Create an empty file: touch magic.sh\n"
        "2. Look at its locks: ls -l magic.sh (Notice there are no 'x's).\n"
        "3. Forge the key: chmod +x magic.sh\n"
        "4. Look at the locks again: ls -l magic.sh\n\n"
        "Did you see the 'x' appear? The filename might even have changed colors to show it's now a program!\n\n"
        "Press Enter here once you've successfully picked the lock on your real machine."
    )

    pause()

    success(
        "Mission accomplished!\n\n"
        "You are officially a locksmith. You've learned how to bring scripts to life."
    )

    return True
