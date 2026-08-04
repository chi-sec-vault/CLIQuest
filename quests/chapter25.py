from ui import card, success, error, prompt, pause
from mentor import say

def quest_25():

    card(
        "🧭 CAMPAIGN 3: GUARDIANS OF LINUX — CHAPTER 25",
        "The Title Deed\n\n"
        "You know how to change the locks ('chmod').\n"
        "But what if you need to transfer ownership of the entire file?"
    )

    pause()

    say(
        "Let's set the scene, Explorer.\n\n"
        "Imagine you've written a security script. It works perfectly. Now, you want the system itself "
        "to run it every night automatically.\n\n"
        "The problem? The system won't trust a file owned by a standard user. You have to transfer the "
        "ownership of that file directly to the system administrator."
    )

    card(
        "🎯 MISSION",
        "Transfer the ownership of a file to the root user."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : chown\n\n"
        "Full Meaning : Change Owner\n\n"
        "Simple Explanation:\n"
        "It strips the current owner off a file and assigns it to a new user."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Format: sudo chown [new_owner] [filename]\n\n"
        "Example: sudo chown root backup.sh\n\n"
        "Pro-Tip: You almost always need 'sudo' when using 'chown'. Linux won't let ordinary users just give "
        "files to other people (or take them) without administrative power!"
    )

    pause()

    say(
        "Let's transfer a deed in the simulator. Imagine you have a file named 'secret.txt'.\n"
        "We need to give it to the system creator: 'root'."
    )

    # Interactive Prompt for chown
    while True:
        command = prompt("Type the command to change the owner of 'secret.txt' to 'root' (Don't forget your admin prefix!)")
        clean_command = command.strip().lower()

        if clean_command == "sudo chown root secret.txt":
            say(
                "The deed is transferred.\n\n"
                "If you ran 'ls -l' right now, you would see your name wiped off the file, replaced by 'root'."
            )
            break
        
        if clean_command.startswith("chown"):
            error("Ah! The system won't let an ordinary user give away property to the root administrator. What prefix do we need to authorize this?")
        elif clean_command.startswith("chmod"):
            error("That command changes the permissions (the locks). We want to change the actual owner.")
        elif clean_command.startswith("sudo chmod"):
            error("You've got the admin prefix, but 'chmod' is for locks. We need the command for changing owners.")
        elif not clean_command.startswith("sudo chown"):
            error("Not quite. We need your surgical strike admin prefix, followed by the two-word command that means 'change owner'.")
        elif "root" not in clean_command:
            error("Who are we giving this file to? Make sure you specify the new owner before the filename.")
        elif "secret.txt" not in clean_command:
            error("You've got the admin power and the new owner, but you forgot the target! What file are we transferring?")
        else:
            error("Almost there. Remember the format: sudo [command] [new_owner] [filename].")

    pause()

    say(
        "You've learned how to transfer power. Let's do it for real."
    )

    card(
        "🌍 FIELD MISSION",
        "Let's transfer ownership of the file we created in the last chapter.\n\n"
        "Open your real Kali terminal and run these steps:\n"
        "1. Check the current owner: ls -l magic.sh (It should show your username).\n"
        "2. Transfer it: sudo chown root magic.sh\n"
        "3. Look at it again: ls -l magic.sh (Your name is gone. It says 'root'!).\n\n"
        "Bonus: Try to delete 'magic.sh' without using sudo. The system will stop you, because you don't own it anymore!\n\n"
        "Press Enter here once you've successfully transferred the deed."
    )

    pause()

    success(
        "Mission accomplished!\n\n"
        "You've mastered permissions, identities, and ownership. The Guardians of Linux campaign is complete."
    )

    return True
