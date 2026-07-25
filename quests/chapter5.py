from ui import card, success, error, prompt, pause
from mentor import say

def quest_5():

    card(
        "🧭 QUEST 5 — BUILDING CAMP",
        "You know how to walk through doors, Explorer.\n\n"
        "Now, it's time to build your own."
    )

    pause()

    say(
        "Explorer...\n\n"
        "What happens when you reach the edge of the map?\n\n"
        "True explorers don't just wander through spaces built by others.\n"
        "They build their own."
    )

    card(
        "📜 STORY",
        "The Linux filesystem is not fixed in stone.\n"
        "It is a living world that you can shape.\n\n"
        "When you need a place to store your tools, your journals, or your secrets...\n"
        "You don't have to search for a room. You can build one out of thin air."
    )

    pause()

    card(
        "🎯 MISSION",
        "Construct a brand new directory called 'outpost'."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : mkdir\n\n"
        "Full Meaning : Make Directory\n\n"
        "Simple Explanation:\n"
        "The 'mkdir' command creates a brand new folder in your current location."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Just like 'cd', you must give it a name.\n\n"
        "Format: mkdir [name_of_new_folder]"
    )

    pause()

    card(
        "🖥️ DEMONSTRATION",
        "$ mkdir outpost\n\n"
        "Once again, Linux is quiet.\n"
        "No construction noises. No loading bars.\n"
        "The room is simply created instantly."
    )

    pause()

    say(
        "How do you know it actually worked?\n\n"
        "You use the command you learned in Quest 3.\n\n"
        "Run 'ls' after building a room, and you will see it standing right in front of you."
    )

    command = prompt("Type the command to create a directory named outpost")

    if command.strip().lower() == "mkdir outpost":

        say(
            "The ground shifts.\n\n"
            "A new path has been created."
        )

        card(
            "🌍 FIELD MISSION",
            "Open your Linux terminal.\n\n"
            "Since you used 'cd data' earlier, you are currently standing inside the data folder.\n\n"
            "Run this exact sequence:\n\n"
            "1. mkdir outpost   (To build your new room)\n"
            "2. ls              (To look around and verify it exists)\n"
            "3. cd outpost      (To walk inside the room you just built!)\n\n"
            "Press Enter when you're ready to continue."
        )

        pause()

        say(
            "Welcome to your new room, Explorer.\n\n"
            "A room that did not exist until you commanded it to.\n\n"
            "You are no longer just a traveler. You are an architect."
        )

        success(
            "Mission accomplished!\n\n"
            "You can now create new folders using the 'mkdir' command."
        )

        return True

    error(
        "Your construction failed.\n\n"
        "The command you are looking for is:\n\n"
        "mkdir outpost"
    )

    return False
