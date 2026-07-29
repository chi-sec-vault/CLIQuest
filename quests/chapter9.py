from ui import card, success, error, prompt, pause
from mentor import say

def quest_9():

    card(
        "🧭 CHAPTER 9 — THE STREAM DIRECTOR",
        "You know how to use nano to write files, and cat to read them.\n\n"
        "But what if you want to write a quick note without leaving the command line?"
    )

    pause()

    say(
        "Explorer...\n\n"
        "In Linux, everything is a stream of data. You can take words and\n"
        "literally 'redirect' them straight into a file using arrows.\n\n"
        "To do this, we use the 'echo' command to speak, and arrows (> or >>) to point."
    )

    card(
        "🎯 MISSION",
        "Learn how to Overwrite (>) and Append (>>) text into your journal."
    )

    pause()

    card(
        "📖 COMMANDS",
        "1. echo : Prints text to the screen.\n"
        "2. >    : Overwrites a file completely (Destructive!).\n"
        "3. >>   : Appends text to the bottom of a file (Safe!)."
    )

    pause()

    say(
        "Let's test the destructive one first.\n"
        "We are going to push a new sentence into your journal using a single arrow (>)."
    )

    # Part 1: Overwrite (>)
    while True:

        command = prompt("Type: echo \"System Restart\" > journal.txt")
        clean_command = command.strip().replace("'", '"')

        if "echo" in clean_command and "> journal.txt" in clean_command and ">>" not in clean_command:
            say(
                "Boom.\n\n"
                "You just forced the words 'System Restart' into 'journal.txt'.\n"
                "Because you used a single '>', everything you previously wrote in nano is now GONE."
            )
            break
        
        error("Check your syntax! Use a single > to point the text into journal.txt.")

    pause()

    say(
        "That is why the single arrow is dangerous.\n\n"
        "Now let's safely add a new line without destroying what we just wrote.\n"
        "We MUST use the double arrows (>>)."
    )

    # Part 2: Append (>>)
    while True:

        command = prompt("Type: echo \"Day 2: Learning redirection\" >> journal.txt")
        clean_command = command.strip().replace("'", '"')

        if "echo" in clean_command and ">> journal.txt" in clean_command:
            say(
                "Flawless.\n\n"
                "The terminal stays quiet, but the words were safely added to the bottom of your journal."
            )
            break
        
        if "> journal.txt" in clean_command and ">>" not in clean_command:
            error("Whoa! A single '>' will delete the 'System Restart' message! Use double '>>' to safely append.")
        else:
            error("Not quite! Make sure you use echo, your text, and >> to point it to journal.txt.")

    card(
        "🌍 FIELD MISSION",
        "Open your real terminal and try it yourself:\n\n"
        "1. Run: echo \"System Restart\" > journal.txt  (This wipes your old nano entry!)\n"
        "2. Run: cat journal.txt  (See? The old text is gone.)\n"
        "3. Run: echo \"Day 2: Learning redirection\" >> journal.txt\n"
        "4. Run: cat journal.txt  (Now both lines are there!)\n\n"
        "Press Enter when you're ready to continue."
    )

    pause()

    say(
        "Excellent work, Explorer.\n\n"
        "Experiencing data loss on a practice file is the best way to respect the single arrow.\n"
        "Redirection is a core superpower in Linux."
    )

    success(
        "Mission accomplished!\n\n"
        "You can now write to files instantly using echo and redirection (> and >>)."
    )

    return True
