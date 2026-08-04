from ui import card, success, error, prompt, pause
from mentor import say

def quest_c2_q6():

    card(
        "🧭 CHAPTER 18 — THE STAKEOUT",
        "You now know how to check the beginning of a file.\n\n"
        "But as a sysadmin or a detective, the top of a log file is usually old news.\n"
        "Systems append new events to the *bottom* of the file. If you want to see what\n"
        "just happened, you need to skip straight to the end."
    )

    pause()

    say(
        "Alright, let's talk about logs for a second.\n\n"
        "When someone tries to log into a server, the system writes that event at the very\n"
        "bottom of the log file. If you want to catch someone in the act, you don't read\n"
        "from chapter one. You flip to the last page.\n\n"
        "Let's look at how we check the bottom."
    )

    card(
        "🎯 MISSION",
        "Read the most recent entries at the end of a log file."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : tail\n\n"
        "Full Meaning : Print the bottom (tail) of a file\n\n"
        "Simple Explanation:\n"
        "It prints exactly the last 10 lines of a file. It's the standard way to check\n"
        "the most recent activity on any Linux machine."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Format: tail [filename]\n\n"
        "Example: tail server.log\n\n"
        "Pro-Tip: If you add '-f' (like 'tail -f server.log'), it keeps the file open\n"
        "and updates your screen live as new text is added. It's literally a stakeout."
    )

    pause()

    say(
        "Let's practice pulling the latest records.\n"
        "Imagine we have a security file called 'auth.log'. We want to see who logged in last."
    )

    # Interactive Prompt for tail - HUMAN & CONVERSATIONAL
    while True:
        command = prompt("Type the command to read the bottom of 'auth.log'")
        clean_command = command.strip().lower()

        if clean_command in ["tail auth.log", "tail -f auth.log"]:
            say(
                "Exactly.\n\n"
                "The terminal skips the first 10,000 lines and just hands you the newest events."
            )
            break
        
        # Conversational, human error handling
        if not clean_command.startswith("tail"):
            if "head" in clean_command:
                error("Ah, you used 'head'. That gives us the very first events from when the server was built. To see what just happened today, we need to check the bottom.")
            elif "cat" in clean_command:
                error("If we 'cat' a live log file, it's going to dump so much text it'll make your head spin. We just want the last few lines.")
            elif "grep" in clean_command:
                error("Using 'grep' makes sense if we are looking for a specific username. But right now, we just want to see *everything* that happened recently. Let's just read the bottom.")
            else:
                error("It's easy to blank on the exact word. We're just looking for the opposite of 'head'.")
        
        elif "auth.log" not in clean_command:
            error("You've got the command itself! Now just tell it which file to look at. Add 'auth.log' to the end.")
            
        else:
            error("Looks like a small typo. No rush. Just the command to read the bottom, a space, and then the filename.")

    pause()

    say(
        "You're going to use this command every single day if you work in tech.\n"
        "Let's run a real stakeout on your Kali machine."
    )

    card(
        "🌍 FIELD MISSION",
        "We are going to attach a live wire to your system logs.\n\n"
        "Open your real Kali terminal and run:\n"
        "tail -f /var/log/syslog\n\n"
        "Notice how it doesn't give you your prompt back? It's waiting. It's watching.\n"
        "While it's running, open a new tab or click around your desktop. You might actually see new logs pop up live!\n\n"
        "(Press Ctrl+C in your Kali terminal to stop watching when you're done.)\n\n"
        "Press Enter here once you've felt like a real hacker watching live logs."
    )

    pause()

    success(
        "Mission accomplished!\n\n"
        "You can now monitor live system activity like a pro."
    )

    return True
