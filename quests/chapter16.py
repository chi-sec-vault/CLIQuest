from ui import card, success, error, prompt, pause
from mentor import say

def quest_c2_q4():

    card(
        "🧭 CHAPTER 16 — THE ASSEMBLY LINE",
        "You now have a toolkit of powerful commands.\n\n"
        "You can read files with 'cat'. You can filter text with 'grep'.\n"
        "But what if you want to do both at the exact same time?\n\n"
        "In Linux, you don't have to use tools one by one. You can connect them."
    )

    pause()

    say(
        "Welcome back, Explorer.\n\n"
        "Today we are going to learn one of the most beautiful concepts in Linux.\n\n"
        "Instead of reading a massive file, saving it, and then filtering it later,\n"
        "we can build a bridge. We can take the output of one tool and pour it\n"
        "directly into another."
    )

    card(
        "🎯 MISSION",
        "Connect two commands together so the output of the first becomes the input of the second."
    )

    pause()

    card(
        "📖 COMMAND",
        "Operator     : | (The Pipe)\n\n"
        "Full Meaning : Pipe output to another command\n\n"
        "Simple Explanation:\n"
        "Think of it as plumbing. It takes whatever answer the first command gives,\n"
        "and instead of printing it to your screen, it funnels it straight into the next command."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Format: [Command 1] | [Command 2]\n\n"
        "Example: ls | grep 'txt'\n"
        "(This lists all files, but funnels them into grep, so you only see the .txt files!)"
    )

    pause()

    say(
        "Let's build our first assembly line.\n"
        "Imagine you want to read a file named 'system.log' using 'cat', and\n"
        "instantly funnel that text into 'grep' to look for the word 'failed'."
    )

    # Interactive Prompt for the Pipe - EMPATHETIC & THEMATIC ERRORS
    while True:
        command = prompt("Type the command to 'cat' the file 'system.log' and pipe it into 'grep failed'")
        clean_command = command.strip().lower().replace('"', "'")

        if clean_command in ["cat system.log | grep failed", "cat system.log | grep 'failed'"]:
            say(
                "A perfect connection.\n\n"
                "The text flows out of 'cat', travels across your pipe, and 'grep' catches exactly what you need."
            )
            break
        
        # Empathetic, Thematic Error Handling
        if "|" not in clean_command:
            if ">" in clean_command or ">>" in clean_command:
                error("Great memory from our base-building days! But '>' sends text into a *file*. To send text into another *command*, we need to use the vertical pipe '|'.")
            else:
                error("It looks like the two commands are sitting next to each other, but the bridge is missing. Try placing the vertical bar '|' between them so the data can flow.")
        
        elif not clean_command.startswith("cat"):
            if "grep" in clean_command.split("|")[0]:
                error("It is so easy to mix up the order! Think of the flow of water. First, we need 'cat' to open the flow of text, and *then* we pipe it into 'grep' to filter it.")
            else:
                error("To start the assembly line, we first need to read the file. Let's make sure 'cat system.log' is on the left side of the pipe.")
                
        elif "system.log" not in clean_command.split("|")[0]:
            error("You've got the 'cat' tool ready, but it needs to know which file to open. Let's add 'system.log' before the pipe.")
            
        elif "grep" not in clean_command.split("|")[1]:
            error("The text is flowing perfectly across the pipe! Now we just need our filter tool on the other side. Try adding 'grep' after the pipe.")
            
        elif "failed" not in clean_command.split("|")[1]:
            error("The tools are all connected beautifully, but the filter doesn't know what word to catch. Let's tell grep to look for 'failed'.")
            
        else:
            error("Combining tools is like learning to play chords on a piano—it takes a little practice. Take your time. We want to 'cat system.log', then pipe it '|', then 'grep failed'.")

    pause()

    say(
        "You are thinking like a true Linux professional now.\n"
        "Let's go build a pipeline on your real machine."
    )

    card(
        "🌍 FIELD MISSION",
        "Let's combine two things you know well: listing files and filtering.\n\n"
        "Open your real Kali terminal and run:\n"
        "ls /etc | grep network\n\n"
        "Notice how instead of showing you hundreds of files, it only showed you the ones with 'network' in the name.\n"
        "Press Enter here when you've admired your handiwork."
    )

    pause()
    
    say(
        "Every command you learn from this day forward can be connected.\n"
        "The possibilities are now infinite."
    )

    success(
        "Mission accomplished!\n\n"
        "You have mastered the pipe."
    )

    return True
