from ui import card, success, error, prompt, pause
from mentor import say

def quest_12():

    card(
        "🧭 CHAPTER 12 — LEAVE NO TRACE",
        "Your outpost is well-organized and secure.\n\n"
        "But as you collect data, logs, and backups, your space will eventually run out.\n"
        "In cybersecurity, leaving old files behind is not just messy—it's a security risk."
    )

    pause()

    say(
        "Explorer...\n\n"
        "It is time to learn how to clean up your tracks. But you must listen carefully.\n\n"
        "In the terminal, there is no 'Recycle Bin'. There is no 'Undo' button.\n"
        "When you tell Linux to delete a file, it is gone forever. Instantly."
    )

    card(
        "🎯 MISSION",
        "Permanently delete the 'logbook.backup' file you created."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : rm\n\n"
        "Full Meaning : Remove\n\n"
        "Simple Explanation:\n"
        "Permanently deletes files."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Format: rm [filename]\n\n"
        "Example: rm old_notes.txt"
    )

    pause()

    say(
        "Take a deep breath. Let's practice deleting the backup file.\n"
        "Type the command to remove 'logbook.backup'."
    )

    # Interactive Prompt for Deleting - NO SPOON FEEDING
    while True:

        command = prompt("Type the command to delete 'logbook.backup'")
        clean_command = command.strip().lower()

        # Success condition
        if clean_command == "rm logbook.backup":
            say(
                "Gone.\n\n"
                "The file vanishes into the void. It cannot be recovered."
            )
            break
        
        # Guided Error Handling
        if not clean_command.startswith("rm"):
            if "delete" in clean_command or "del" in clean_command:
                error("Linux doesn't use the word 'delete' for this. We use 'rm' (remove). Try again.")
            else:
                error("You need the remove command. Review the 'COMMAND' card above.")
        
        elif "logbook.backup" not in clean_command:
            if "logbook.txt" in clean_command:
                 error("Wait! Don't delete your main logbook! We only want to delete the backup file: logbook.backup")
            else:
                 error("You need to tell the system exactly which file to remove. You forgot the filename.")
            
        else:
            error("The syntax is off. Remember the format: rm [filename]")

    pause()

    say(
        "You've proven you understand the syntax. Now it is time to execute it in the real world.\n\n"
        "You will need to navigate back into your archives folder to do this."
    )

    card(
        "🌍 FIELD MISSION",
        "Open your real terminal and clean up your workspace:\n\n"
        "1. Run: cd archives  (Go where the files are)\n"
        "2. Run: ls  (Look at both logbook.txt and logbook.backup)\n"
        "3. Run: rm logbook.backup  (Delete the backup permanently)\n"
        "4. Run: ls  (Verify it is gone forever!)\n"
        "5. Run: cd ..  (Return to your base camp)\n\n"
        "Press Enter when you're ready to continue."
    )

    pause()

    say(
        "The outpost is clean. Your tracks are erased.\n\n"
        "You now have the power to create, read, move, copy, and destroy."
    )

    success(
        "Mission accomplished!\n\n"
        "You can now permanently delete files using the 'rm' command."
    )

    return True
