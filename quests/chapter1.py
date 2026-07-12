from ui import card, success, error, prompt, pause


def quest_1():

    card(
        "🧭 QUEST 1 — WHO AM I?",
        "Welcome to your first quest!\n\n"
        "Today you'll learn your very first Linux command."
    )

    pause()

    card(
        "📜 STORY",
        "You've just logged into a Linux machine.\n\n"
        "Before touching any files or running any commands,\n"
        "you need to know who Linux thinks you are."
    )

    pause()

    card(
        "🎯 MISSION",
        "Discover your current Linux username."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : whoami\n\n"
        "Full Meaning : Who Am I\n\n"
        "Explanation  : Displays the username of the person currently logged into Linux."
    )

    pause()

    command = prompt("Type the command exactly as shown")

    if command.strip() == "whoami":
        success(
            "Excellent!\n\n"
            "Now open your Linux terminal and run:\n\n"
            "whoami"
        )
        return True

    error(
        "Not quite.\n\n"
        "The correct command is:\n\n"
        "whoami"
    )

    return False
