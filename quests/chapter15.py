from ui import card, success, error, prompt, pause
from mentor import say

def quest_c2_q3():

    card(
        "🧭 CHAPTER 15 — THE LIBRARIAN'S INDEX",
        "The 'find' command is incredibly thorough, but searching a massive server live takes time.\n\n"
        "What if someone already mapped out the entire system for you? You wouldn't need to hunt;\n"
        "you could just ask for the index."
    )

    pause()

    say(
        "Explorer...\n\n"
        "A good detective knows when to do a thorough grid search, and when it's better to just check the archives.\n\n"
        "Let's look at a tool that sacrifices a tiny bit of up-to-the-second accuracy for lightning speed."
    )

    card(
        "🎯 MISSION",
        "Look up a file instantly by querying the system's pre-built file database."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : locate\n\n"
        "Full Meaning : Locate files by name\n\n"
        "Simple Explanation:\n"
        "Instead of walking through the hard drive directly, 'locate' quickly looks up the file\n"
        "in a background database. It's just like checking the index at the back of a textbook."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Format: locate [filename]\n\n"
        "Example: locate ssh_config"
    )

    pause()

    say(
        "Let's consult the archives together.\n"
        "Try querying the database for a file named 'auth.log'."
    )

    # Interactive Prompt for locate - EMPATHETIC & THEMATIC ERRORS
    while True:
        command = prompt("Type the command to instantly look up 'auth.log'")
        clean_command = command.strip().lower()

        if clean_command == "locate auth.log":
            say(
                "Flash of insight.\n\n"
                "The database returns the exact paths in milliseconds. Beautifully done."
            )
            break
        
        # Empathetic, Thematic Error Handling
        if not clean_command.startswith("locate"):
            if "find" in clean_command:
                error("It is so natural to reach for 'find' since we just learned it! But since we want lightning speed this time, let's try querying the index instead.")
            elif "grep" in clean_command:
                error("Great instinct to use 'grep' for filtering! But right now we are trying to find where the file lives, rather than looking inside it. Let's try the database tool.")
            else:
                error("Linux has so many commands, it is easy to mix them up. Take a gentle look at the COMMAND card to find the one that checks the index.")
        
        elif "auth.log" not in clean_command:
            error("You've got the command perfectly! The database is just waiting to know what to look up. Let's add the filename to your command.")
            
        else:
            error("The structure got a little tangled, which happens to everyone. It's just two words: the tool itself, followed by the file you want to look up.")

    pause()

    say(
        "You've got a wonderful grasp of how this works.\n"
        "Now, let's try it on your real machine.\n\n"
        "Let's look up the location of the very first command you ever learned: whoami."
    )

    card(
        "🌍 FIELD MISSION",
        "Let's see how fast the index is.\n\n"
        "Whenever you are ready, open your real Kali terminal and try running:\n"
        "locate whoami\n\n"
        "Notice how it instantly prints out the exact path to the 'whoami' program.\n"
        "Press Enter here once you've successfully tested it."
    )

    pause()
    
    say(
        "A true detective knows their tools and when to use them.\n"
        "Use 'find' when you need absolute precision on a live system. Use 'locate' when you need speed."
    )

    success(
        "Mission accomplished!\n\n"
        "You have mastered the system's file index."
    )

    return True
