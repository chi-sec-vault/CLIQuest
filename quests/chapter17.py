from ui import card, success, error, prompt, pause
from mentor import say

def quest_c2_q5():

    card(
        "🧭 CHAPTER 17 — THE SNEAK PEEK",
        "As a Linux detective, you will constantly encounter massive log files.\n\n"
        "You already know how to search inside them using 'grep', but sometimes you\n"
        "just want to take a quick peek at a file to see what kind of data it holds."
    )

    pause()

    say(
        "Let's be real for a second.\n\n"
        "If you use 'cat' on a massive 10,000-line server log, it will completely flood\n"
        "your screen. You'll lose your place, and it's just annoying to scroll through.\n\n"
        "Instead, we use a precision tool. Something that just grabs the first few lines\n"
        "so we can see what we're dealing with."
    )

    card(
        "🎯 MISSION",
        "Inspect the beginning of a massive file without opening the whole thing."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : head\n\n"
        "Full Meaning : Print the top (head) of a file\n\n"
        "Simple Explanation:\n"
        "It prints exactly the first 10 lines of a file and then stops. It's the perfect\n"
        "way to take a 'sneak peek' at a file's structure."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Format: head [filename]\n\n"
        "Example: head database.csv"
    )

    pause()

    say(
        "Let's try it out.\n"
        "Imagine you just stumbled across a massive file called 'server.log'.\n"
        "You just want to see how it starts."
    )

    # Interactive Prompt for head - HUMAN & CONVERSATIONAL
    while True:
        command = prompt("Type the command to read the top of 'server.log'")
        clean_command = command.strip().lower()

        if clean_command == "head server.log":
            say(
                "Nice.\n\n"
                "You instantly see the first 10 lines. No flooding, no mess. Just what you needed."
            )
            break
        
        # Conversational, human error handling
        if not clean_command.startswith("head"):
            if "cat" in clean_command:
                error("Oof, if we use 'cat' on a server log, it'll dump thousands of lines and take over your screen. We just want a quick peek at the top.")
            elif "grep" in clean_command:
                error("We'd use 'grep' if we knew exactly what word we were looking for. But right now, we're just exploring. Let's check the top few lines instead.")
            elif "tail" in clean_command:
                error("You're thinking of the bottom! That's actually coming up next. For now, let's start at the very beginning of the file.")
            else:
                error("Terminals can be picky. We just need the specific command that reads the top of a file.")
        
        elif "server.log" not in clean_command:
            error("You nailed the command itself, but we forgot to tell it *what* file to look at. Just add 'server.log' at the end.")
            
        else:
            error("Looks like a typo. No worries, it happens. Just type the command to read the top, a space, and then 'server.log'.")

    pause()

    say(
        "This tool saves so much time when you're digging through new systems.\n"
        "Let's test it on your real machine."
    )

    card(
        "🌍 FIELD MISSION",
        "Let's check the very top of your system's user database.\n\n"
        "Open your real Kali terminal and run:\n"
        "head /etc/passwd\n\n"
        "Notice how 'root' is at the very top, because it was the very first user created on the system.\n"
        "Press Enter here when you've seen it."
    )

    pause()

    success(
        "Mission accomplished!\n\n"
        "You can now safely peek at the largest files on the system."
    )

    return True
