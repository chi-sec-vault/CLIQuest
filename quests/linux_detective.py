from ui import card, success, error, prompt, pause
from mentor import say

def quest_c2_boss():

    card(
        "🧭 CAMPAIGN 2: LINUX DETECTIVE — FINAL EXAM",
        "A rogue agent has infiltrated the system.\n\n"
        "They are actively moving through standard system files, trying to blend in.\n"
        "You are the only one who knows how to track them.\n\n"
        "Catch them, and you will earn your Detective Badge."
    )

    pause()

    say(
        "Alright, Explorer. Take a breath. We're going to do this together.\n\n"
        "We know the agent is trying to tamper with the secure shell service so they can\n"
        "log in remotely. We don't have time to crawl the whole hard drive, so let's check\n"
        "the database for the file 'sshd_config'."
    )

    while True:
        command = prompt("Phase 1: Use the database to instantly look up 'sshd_config'")
        clean = command.strip().lower()

        if clean == "locate sshd_config":
            say("Got it. The database points us straight to '/etc/ssh/sshd_config'.")
            break
        
        if not clean.startswith("locate"):
            if "find" in clean:
                error("Normally 'find' is great, but we don't have time to crawl the live hard drive right now. Let's use the tool that checks the pre-built index.")
            else:
                error("We need the specific command that queries the system's file index. Think 'librarian'.")
        elif "sshd_config" not in clean:
            error("You've got the database tool ready, but you didn't tell it what file to look for. Add 'sshd_config'.")
        else:
            error("Just a small typo. Type the command to query the index, a space, and then 'sshd_config'.")

    pause()

    say(
        "Okay, they haven't touched the SSH config yet. But what if they created a hidden\n"
        "user account for themselves?\n\n"
        "Remember, every time a new user is created, they get added to the very *bottom*\n"
        "of the '/etc/passwd' file. Let's check the newest entries."
    )

    while True:
        command = prompt("Phase 2: Check the very bottom of '/etc/passwd' to see the newest users")
        clean = command.strip().lower()

        if clean in ["tail /etc/passwd", "tail -f /etc/passwd"]:
            say("Nice work. The terminal skips the old system accounts and shows us the latest users at the bottom.")
            break
        
        if not clean.startswith("tail"):
            if "head" in clean:
                error("That would show us 'root' and the system accounts created years ago! We need to look at the very bottom to see the newest ones.")
            elif "cat" in clean:
                error("If we 'cat' the password file, it'll dump everyone at once. We just need to check the last few lines.")
            else:
                error("Take a second. We're looking for the command that reads the 'tail' end of a document.")
        elif "/etc/passwd" not in clean:
            error("You have the right tool, but you didn't point it at the user file. Add '/etc/passwd' to the end.")
        else:
            error("Close! Just the command to check the bottom, a space, and then '/etc/passwd'.")

    pause()

    say(
        "No new accounts. They are being clever. \n\n"
        "Wait... I see network traffic. They are trying to open a backdoor on a standard port.\n"
        "Kali has a massive file called '/etc/services' that lists thousands of network ports.\n\n"
        "Let's build an assembly line to open that file and filter it for the word 'ftp'."
    )

    while True:
        command = prompt("Phase 3: 'cat' the file '/etc/services' and pipe it into 'grep ftp'")
        clean = command.strip().lower().replace('"', "'")

        if clean in ["cat /etc/services | grep ftp", "cat /etc/services | grep 'ftp'"]:
            say(
                "You nailed it.\n\n"
                "Thousands of lines flow across the pipe, but your filter catches exactly what\n"
                "we needed. You found the exact port they were targeting."
            )
            break
        
        if "|" not in clean:
            error("You're missing the bridge! We need to connect the two tools using the vertical pipe '|'.")
        elif not clean.startswith("cat"):
            error("Start the flow of data first. Use 'cat' to open the file on the left side of the pipe.")
        elif "/etc/services" not in clean.split("|")[0]:
            error("You started 'cat', but what file are we reading? Add '/etc/services' before the pipe.")
        elif "grep" not in clean.split("|")[1]:
            error("The pipe is flowing, but we need our filter tool on the other side. Add 'grep'.")
        elif "ftp" not in clean.split("|")[1]:
            error("The filter is ready, but it doesn't know what to catch! Tell it to look for 'ftp'.")
        else:
            error("Don't panic. Just piece it together: cat the file, add the pipe, then grep the word.")

    pause()

    say(
        "Got them. The sysadmins just locked them out of the network.\n\n"
        "Take a step back and look at what you just did. If you open a new terminal right now\n"
        "and type those exact same commands, they will actually work. You used real Linux files\n"
        "to run a real investigation.\n\n"
        "You aren't just surviving the terminal anymore. You're controlling it.\n\n"
        "Pull out your journal, Explorer. It's time to log a new achievement."
    )

    card(
        "🎖️ BADGE EARNED: THE LINUX DETECTIVE",
        "Write this down in your journal. You have mastered:\n\n"
        "[x] find & locate (System Searching)\n"
        "[x] grep (Text Filtering)\n"
        "[x] The Pipe | (Command Chaining)\n"
        "[x] head & tail (File Inspection)"
    )

    success(
        "Congratulations on earning your Detective Badge.\n\n"
        "Take a break, stretch, and return when you are ready for Campaign 3."
    )

    return True
