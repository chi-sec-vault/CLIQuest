from ui import card, success, error, prompt, pause
from mentor import say

def challenge_3():

    card(
        "☠️ CAMPAIGN 3 BOSS FIGHT",
        "The Vault Lockdown\n\n"
        "An automated security protocol has gone rogue and locked down the server.\n"
        "The override script is sitting in the vault, but it's stripped of its permissions and ownership.\n"
        "You must use every Guardian tool you've learned to bypass the lockdown, claim the file, and execute the override."
    )

    pause()

    say(
        "This is it, Explorer. No hand-holding. No training wheels.\n\n"
        "You have to verify your clearance, take over the system, claim the override file ('override.sh'), "
        "and forge the key to run it. Let's breach the vault."
    )

    card(
        "🎯 MISSION OBJECTIVES",
        "1. Check your current system identity.\n"
        "2. Make a surgical strike to read the secure lockdown log.\n"
        "3. Grab the master key and switch your entire session to root.\n"
        "4. Take ownership of the override script.\n"
        "5. Make the script executable."
    )

    pause()

    say("SYSTEM ALERT: Initiating breach sequence...")

    # Stage 1: id
    while True:
        command = prompt("STAGE 1: Verify your current security clearance")
        clean_command = command.strip().lower()

        if clean_command == "id":
            say("Clearance verified: uid=1000. You are a standard user. You need more power.")
            break
        elif clean_command == "whoami":
            error("That gives us your username, but the system needs to see your numerical user and group IDs. Think back to the watchtower.")
        else:
            error("Not quite. What is the short command that prints your numerical identity?")

    # Stage 2: sudo cat /var/log/lockdown
    while True:
        command = prompt("STAGE 2: Read the secure file '/var/log/lockdown' using your temporary administrative power")
        clean_command = command.strip().lower()

        if clean_command == "sudo cat /var/log/lockdown":
            say("Log accessed: 'OVERRIDE SCRIPT DETECTED. ROOT OWNERSHIP REQUIRED.'")
            break
        elif not clean_command.startswith("sudo"):
            error("Access Denied. You are trying to read a restricted file as a normal user. You need to borrow administrative power for this single action.")
        elif "cat" not in clean_command:
            error("You have the power, but what tool do we use to read the contents of a scroll (or file) to the screen?")
        elif "/var/log/lockdown" not in clean_command:
            error("Don't forget to specify exactly which file we are trying to read! Provide the full path.")
        else:
            error("Check your syntax. It should be your admin prefix, followed by the command to read, and then the target file.")

    # Stage 3: su
    while True:
        command = prompt("STAGE 3: The log demands full ownership. Swap your entire user session to the root administrator")
        clean_command = command.strip().lower()

        if clean_command in ["su", "su root", "su -"]:
            say("Master key accepted. Your terminal prompt changes from '$' to '#'. You are now root.")
            break
        elif clean_command.startswith("sudo"):
            error("A temporary pass won't work here. The system demands that you actually *become* the administrator for the rest of the session.")
        else:
            error("Not quite. Think about the master key command that lets you switch to another user account.")

    # Stage 4: chown root override.sh
    while True:
        command = prompt("STAGE 4: You are root! Now, transfer the ownership of 'override.sh' to 'root'")
        clean_command = command.strip().lower()

        if clean_command in ["chown root override.sh", "sudo chown root override.sh"]:
            say("Title deed transferred. The file 'override.sh' now belongs to the root administrator.")
            break
        elif clean_command.startswith("chmod"):
            error("That command changes the locks (permissions). We need to change the *owner* (the title deed).")
        elif "root" not in clean_command:
            error("Who are we giving the file to? The system administrator needs to own this.")
        elif "override.sh" not in clean_command:
            error("You have the command and the new owner, but what file are we transferring?")
        else:
            error("Remember the order: the command to change owner, the new owner's name, and then the file.")

    # Stage 5: chmod +x override.sh
    while True:
        command = prompt("STAGE 5: Final step! Forge the key to make 'override.sh' executable")
        clean_command = command.strip().lower()

        if clean_command in ["chmod +x override.sh", "sudo chmod +x override.sh"]:
            say("Click. The lock turns. The script lights up green—it's alive.")
            break
        elif clean_command.startswith("chown"):
            error("You already transferred the title deed! Now you need to modify the file's mode to unlock its ability to run.")
        elif "+x" not in clean_command:
            error("You brought the locksmith tool, but you didn't tell it to *add* the *execute* permission.")
        else:
            error("Check your spacing. It should be the locksmith command, the specific permission change, and the target file.")

    pause()

    say(
        "You've proven you can do it in the simulator.\n"
        "Now, you must prove you can do it on a live system from memory."
    )

    card(
        "🌍 FIELD MISSION: BREACH THE REAL VAULT",
        "Open your real Kali terminal and execute this sequence using what you've learned:\n\n"
        "1. Create an empty file named 'override.sh'.\n"
        "2. View its detailed permissions and ownership (The Long View).\n"
        "3. Grab the master key (swap to the root user).\n"
        "4. Transfer the ownership of the file to 'root'.\n"
        "5. Forge the key to add execute permissions to the file.\n"
        "6. View the detailed permissions again to verify the 'x' is there and the owner is root!\n"
        "7. Type 'exit' to return to your normal user account.\n\n"
        "Press Enter here once you've successfully claimed and unlocked the file without any hints."
    )

    pause()

    say(
        "The alarms stop. The red lights turn green. The vault doors slide open.\n\n"
        "Pull out your journal, Explorer. You've earned this."
    )

    card(
        "🎖️ BADGE EARNED: GUARDIAN OF LINUX",
        "Write this down in your journal. You have mastered:\n\n"
        "[x] ls -a & ls -la (System Visibility)\n"
        "[x] sudo & su (Privilege Escalation)\n"
        "[x] id (Identity Verification)\n"
        "[x] chmod & chown (Access Control)"
    )

    success(
        "CAMPAIGN 3 COMPLETE!\n\n"
        "You are a true Guardian of Linux. You understand permissions, identities, and root power.\n"
        "Take a breath. You're ready for Campaign 4."
    )

    return True
