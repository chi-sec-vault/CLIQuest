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
        command = prompt("Phase 1: Query the system's pre-built index database for 'sshd_config'")
        clean = command.strip().lower()

        if clean == "locate sshd_config":
            say("Got it. The database points us straight to '/etc/ssh/sshd_config'.")
            break
        
        if not clean.startswith("locate"):
            if "find" in clean:
                error("Normally 'find' is great, but we don't have time to crawl the live hard drive right now. We need the tool that checks the pre-built index.")
            else:
                error("We need the specific command that queries the system's file index. Think 'librarian'.")
        elif "sshd_config" not in clean:
            error("You've got the database tool ready, but you didn't tell it what file to look for.")
        else:
            error("Just a small typo. Type the command to query the index, a space, and then the target file.")

    pause()

    say(
        "Okay, they haven't touched the SSH config yet. But what if they created a hidden\n"
        "user account for themselves?\n\n"
        "Remember, every time a new user is created, they get added to the very *bottom*\n"
        "of the '/etc/passwd' file. Let's check the newest entries."
    )

    while True:
        command = prompt("Phase 2: Print only the bottom (tail end) of '/etc/passwd' to see the newest users")
        clean = command.strip().lower()

        if clean in ["tail /etc/passwd", "tail -f /etc/passwd"]:
            say("Nice work. The terminal skips the old system accounts and shows us the latest users at the bottom.")
            break
        
        if not clean.startswith("tail"):
            if "head" in clean:
                error("That would show us 'root' and the system accounts created years ago! We need to look at the very bottom to see the newest ones.")
            elif "cat" in clean:
                error("If we read the entire file at once, it'll dump everyone on the screen. We just need to check the last few lines.")
            else:
                error("Take a second. We're looking for the command that reads the trailing end of a document.")
        elif "/etc/passwd" not in clean:
            error("You have the right tool, but you didn't point it at the user file. Add the full path to the password file.")
        else:
            error("Check your spacing: command, space, file path.")

    pause()

    say(
        "No new accounts. They are being clever. \n\n"
        "Wait... I see network traffic. They are trying to open a backdoor on a standard port.\n"
        "Kali has a massive file called '/etc/services' that lists thousands of network ports.\n\n"
        "Let's build an assembly line to open that file and filter it for the word 'ftp'."
    )

    while True:
        command = prompt("Phase 3: Output '/etc/services' to the screen, but send the data across a pipe to filter it for 'ftp'")
        clean = command.strip().lower().replace('"', "'")

        if clean in ["cat /etc/services | grep ftp", "cat /etc/services | grep 'ftp'"]:
            say(
                "You nailed it.\n\n"
                "Thousands of lines flow across the bridge, but your filter catches exactly what\n"
                "we needed. You found the exact port they were targeting."
            )
            break
        
        if "|" not in clean:
            error("You're missing the bridge! We need to connect the reading tool and the filtering tool using the vertical pipe character.")
        elif not clean.startswith("cat"):
            error("Start the flow of data first. Use the command to open/read a file on the left side of the pipe.")
        elif "/etc/services" not in clean.split("|")[0]:
            error("You started the flow, but what file are we reading? Specify '/etc/services' before the pipe.")
        elif "grep" not in clean.split("|")[1]:
            error("The data is flowing, but we need our text filter tool on the other side of the pipe.")
        elif "ftp" not in clean.split("|")[1]:
            error("The filter is ready, but it doesn't know what to catch! Tell it to look for 'ftp'.")
        else:
            error("Don't panic. Just piece it together: read the file, add the pipe, then filter the word.")

    pause()

    say(
        "Got them. The sysadmins just locked them out of the network.\n\n"
        "Take a step back and look at what you just did. If you open a real terminal right now\n"
        "and type those exact same commands, they will actually work. You used real Linux files\n"
        "to run a real investigation.\n\n"
        "In fact, let's prove it right now from memory."
    )

    card(
        "🌍 FIELD MISSION: REAL-WORLD DETECTIVE",
        "Open your real Kali terminal and execute your investigation using what you've learned:\n\n"
        "1. Query the database index for 'sshd_config'.\n"
        "2. Print the bottom 10 lines of the '/etc/passwd' file.\n"
        "3. Output the contents of '/etc/services' and pipe it into a text filter looking for 'ftp'.\n\n"
        "Notice how incredibly fast the pipe (|) filters through thousands of lines of text to give you exactly what you asked for.\n\n"
        "Press Enter here once you've run your investigation in the real terminal."
    )

    pause()

    say(
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
