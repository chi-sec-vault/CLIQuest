from ui import card, success, error, prompt, pause
from mentor import say

def quest_c2_q2():

    card(
        "🧭 CHAPTER 14 — THE FILTER",
        "You successfully found the lost configuration file.\n\n"
        "But there's a problem: the file is 10,000 lines long. Reading it line-by-line\n"
        "using 'cat' would take hours. You need to extract only the lines that matter."
    )

    pause()

    say(
        "Explorer...\n\n"
        "In the real world, log files and configs are massive.\n"
        "A true Linux detective doesn't read the whole book to find one word.\n"
        "They use a filter."
    )

    card(
        "🎯 MISSION",
        "Search inside a massive file and extract only the lines containing a specific word."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : grep\n\n"
        "Full Meaning : Global Regular Expression Print\n\n"
        "Simple Explanation:\n"
        "It acts like an X-ray. It searches inside a file for a specific word\n"
        "or phrase and prints *only* the lines that match."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Format: grep [search_word] [filename]\n\n"
        "Example: grep 'password' config.txt"
    )

    pause()

    say(
        "Let's test your understanding.\n"
        "Imagine you have a file named 'server_logs.txt'. You want to find every line that contains the word 'ERROR'."
    )

    # Interactive Prompt for grep - STRICTLY THEMATIC ERRORS
    while True:
        command = prompt("Type the command to search for 'ERROR' inside 'server_logs.txt'")
        clean_command = command.strip()

        # Success condition (handling both with and without quotes)
        if clean_command in ["grep ERROR server_logs.txt", "grep 'ERROR' server_logs.txt", 'grep "ERROR" server_logs.txt']:
            say(
                "Perfect.\n\n"
                "The terminal instantly spits out only the lines containing 'ERROR'.\n"
                "The rest of the file is ignored."
            )
            break
        
        # Guided Error Handling
        if not clean_command.startswith("grep"):
            if "find" in clean_command:
                error("The 'find' command wanders the filesystem looking for files. We need the tool that looks INSIDE the text.")
            elif "cat" in clean_command:
                error("If you use 'cat', the terminal will print all 10,000 lines at once. Use the filter command instead.")
            else:
                error("That command will not filter text. Review the COMMAND card for the exact keyword.")
        
        elif "ERROR" not in clean_command:
            error("You powered on the X-ray, but you did not tell it what pattern to look for. Provide the target word.")
            
        elif "server_logs.txt" not in clean_command:
            error("You told the filter what to look for, but you did not point it at a file. Where should it look?")
            
        else:
            error("The filter jammed. It expects a specific sequence: the command, the target word, and then the file.")

    pause()

    say(
        "Now, let's take this X-ray vision to the real world.\n"
        "Every Linux system has a file that lists all the user accounts. It's located at '/etc/passwd'."
    )

    card(
        "🌍 FIELD MISSION",
        "Open your real Kali terminal. We are going to look for the main administrator account, known as 'root'.\n\n"
        "Run this command:\n"
        "grep root /etc/passwd\n\n"
        "Look at the output. Notice how it only printed the lines containing 'root'.\n"
        "Press Enter when you are done."
    )

    pause()

    success(
        "Mission accomplished!\n\n"
        "You can now sift through thousands of lines of text in milliseconds using 'grep'."
    )

    return True
