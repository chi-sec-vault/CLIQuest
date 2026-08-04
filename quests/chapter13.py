from ui import card, success, error, prompt, pause
from mentor import say

def quest_c2_q1():

    card(
        "🧭 CAMPAIGN 2: QUEST 1 — THE BREADCRUMB TRAIL",
        "A rogue agent hid a critical configuration file somewhere in the system.\n\n"
        "You could use 'ls' and 'cd' to look through thousands of folders, but that\n"
        "would take weeks. You need a way to search the entire system at once."
    )

    pause()

    say(
        "Welcome back, Explorer.\n\n"
        "In your first campaign, you learned how to survive and navigate.\n"
        "Now, you must learn how to hunt.\n\n"
        "We are looking for a hidden file named 'secret.txt'."
    )

    card(
        "🎯 MISSION",
        "Search your current directory and all its sub-folders to find a specific file."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : find\n\n"
        "Full Meaning : Find files\n\n"
        "Simple Explanation:\n"
        "It acts like a search dog. You give it a starting location and a name,\n"
        "and it hunts through every folder and sub-folder until it finds a match."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Format: find [starting_location] -name [filename]\n\n"
        "Example: find . -name 'secret.txt'\n"
        "(Note: The '.' means 'start looking right here in my current folder'.)"
    )

    pause()

    say(
        "Let's test your instincts in the simulator before we go into the field.\n"
        "Type the command to search your current directory (.) for a file named 'secret.txt'."
    )

    # Interactive Prompt for find - KIND & GENTLE (No Spoon-feeding)
    while True:
        command = prompt("Type the command to find 'secret.txt'")
        clean_command = command.strip().replace('"', "'")

        # Success condition
        if clean_command in ["find . -name 'secret.txt'", "find . -name secret.txt"]:
            say(
                "Target acquired.\n\n"
                "The system immediately prints the exact path to the hidden file."
            )
            break
        
        # Guided Error Handling
        if not clean_command.startswith("find"):
            if "search" in clean_command or "locate" in clean_command:
                error("You have the right mindset! But Linux uses a different word for this kind of hunt. Take a peek at the 'COMMAND' card.")
            else:
                error("Not quite the right tool for the job. Which command helps us hunt for files?")
        
        elif "." not in clean_command:
            error("Every search needs a starting point. Do you remember the tiny symbol we use to say 'start right here'?")
            
        elif "-name" not in clean_command:
            error("You're getting closer! The command just needs to know how to filter the search. Check the format to see how we specify the file's name.")
            
        elif "secret.txt" not in clean_command:
            error("Almost perfect! You have the setup right, but the system is waiting for the target. What file are we hunting for?")
            
        else:
            error("You have all the right pieces, they just need to be in a slightly different order. Take a breath and check the 'HOW TO USE IT' card.")

    pause()

    say(
        "You understand the syntax perfectly. Now it is time to execute it in the real world.\n\n"
        "Your real machine doesn't have a 'secret.txt' file. Instead, we are going to search\n"
        "the main system folder ('/etc') for a famous Linux file called 'passwd'."
    )

    card(
        "🌍 FIELD MISSION",
        "Open your real terminal and unleash the search dog:\n\n"
        "Run: find /etc -name passwd\n\n"
        "Watch how fast it searches, then press Enter here when you see the file's location."
    )

    pause()

    success(
        "Mission accomplished!\n\n"
        "You can now hunt down any lost file in the entire filesystem."
    )

    return True
