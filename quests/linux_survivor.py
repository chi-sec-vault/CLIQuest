from ui import card, success, error, prompt, pause
from mentor import say

def survivor_challenge():

    card(
        "🚨 THE SURVIVOR TRIAL — OPERATION: LOST EVIDENCE",
        "A senior analyst has compromised a secure server.\n\n"
        "They left sensitive evidence scattered in the terminal and panicked.\n"
        "Your mission is to secure the evidence, back it up, and clean the tracks."
    )

    pause()

    say(
        "Explorer...\n\n"
        "This is your proving ground. To officially earn the title of 'Linux Survivor',\n"
        "you must execute this operation flawlessly.\n\n"
        "I will not give you the commands. I will only give you the objectives."
    )

    card(
        "🎯 PHASE 1: SECURE THE AREA",
        "Objective: Create a new folder named 'case_042' to hold the evidence."
    )

    # Phase 1: mkdir
    while True:
        command = prompt("Type the command to create the 'case_042' folder")
        clean_command = command.strip().lower()

        if clean_command == "mkdir case_042":
            say("Area secured.")
            break
        
        if "make" in clean_command or "create" in clean_command:
            error("Think back to your base-building training. What is the abbreviation for 'make directory'?")
        else:
            error("Not quite. You need to create a directory named 'case_042'.")

    pause()

    card(
        "🎯 PHASE 2: ENTER THE ZONE",
        "Objective: Navigate inside the 'case_042' folder."
    )

    # Phase 2: cd
    while True:
        command = prompt("Type the command to move into 'case_042'")
        clean_command = command.strip().lower()

        if clean_command == "cd case_042":
            say("You are in.")
            break
        
        error("How do you change directories? Review your navigation skills.")

    pause()

    card(
        "🎯 PHASE 3: RECORD THE EVIDENCE",
        "Objective: Safely append the word 'Hacker' into a file named 'suspect.txt'."
    )

    # Phase 3: echo & >>
    while True:
        command = prompt("Type the command to append 'Hacker' to 'suspect.txt'")
        clean_command = command.strip().replace("'", '"')

        if "echo" in clean_command and ">> suspect.txt" in clean_command:
            say("Evidence recorded.")
            break
        
        if "> suspect.txt" in clean_command and ">>" not in clean_command:
            error("Careful! A single '>' overwrites. We need to append safely. Try again.")
        else:
            error("You need to print the text and redirect it safely into 'suspect.txt'.")

    pause()

    card(
        "🎯 PHASE 4: CLONE THE DATA",
        "Objective: Make a backup copy of 'suspect.txt' and name it 'suspect.backup'."
    )

    # Phase 4: cp
    while True:
        command = prompt("Type the command to copy the evidence file")
        clean_command = command.strip().lower()

        if clean_command == "cp suspect.txt suspect.backup":
            say("Data cloned and secured.")
            break
        
        error("How do you make a copy? Remember: command, source, then destination.")

    pause()

    card(
        "🎯 PHASE 5: SHAPE SHIFT",
        "Objective: Rename the original 'suspect.txt' file to 'official_report.txt'."
    )

    # Phase 5: mv
    while True:
        command = prompt("Type the command to rename 'suspect.txt' to 'official_report.txt'")
        clean_command = command.strip().lower()

        if clean_command == "mv suspect.txt official_report.txt":
            say("File renamed perfectly.")
            break
        
        error("What command shape-shifts files to rename them? Remember the syntax!")

    pause()

    card(
        "🎯 PHASE 6: LEAVE NO TRACE",
        "Objective: Permanently delete the 'suspect.backup' file to hide your tracks."
    )

    # Phase 6: rm
    while True:
        command = prompt("Type the command to delete 'suspect.backup'")
        clean_command = command.strip().lower()

        if clean_command == "rm suspect.backup":
            say("Tracks erased. You are a ghost.")
            break
        
        error("How do you permanently remove a file? Do not use the word 'delete'!")

    pause()

    say(
        "Incredible work, Explorer.\n\n"
        "You didn't just type commands. You executed a full cybersecurity operation.\n"
        "You now have the muscle memory to navigate, manipulate, and secure any Linux server."
    )

    card(
        "🌍 REAL-WORLD EXECUTION",
        "Now, do it in the real terminal. Run this entire operation from memory:\n\n"
        "1. Create 'case_042'\n"
        "2. Move into it\n"
        "3. Append 'Hacker' to 'suspect.txt'\n"
        "4. Copy it to 'suspect.backup'\n"
        "5. Rename 'suspect.txt' to 'official_report.txt'\n"
        "6. Delete 'suspect.backup'\n"
        "7. Read 'official_report.txt' using cat to admire your work!\n\n"
        "Press Enter when your operation is complete."
    )

    pause()

    success(
        "🏅 ACHIEVEMENT UNLOCKED: LINUX SURVIVOR\n\n"
        "You have conquered Campaign 1.\n"
        "But your journey is just beginning.\n\n"
        "Rest up, Explorer. Next time, we dive into Campaign 2: The Linux Detective..."
    )

    return True
