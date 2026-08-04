from ui import card, success, error, prompt, pause
from mentor import say

def quest_23():

    card(
        "🧭 CAMPAIGN 3: GUARDIANS OF LINUX — CHAPTER 23",
        "The Watchtower\n\n"
        "Power is useless if you don't know who is wielding it.\n"
        "Before you change any system rules, you must verify your exact security clearance."
    )

    pause()

    say(
        "Think about it, Explorer.\n\n"
        "If you sit down at a terminal that's already logged in, you need to know who you are before you touch anything.\n"
        "Earlier, we used 'whoami' to get a simple name. But Linux runs deeper than names—it runs on math.\n\n"
        "The system identifies you by a User ID (UID), a primary Group ID (GID), and a list of secondary groups that grant you specific permissions."
    )

    card(
        "🎯 MISSION",
        "Display your precise numerical identity and group clearances."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : id\n\n"
        "Full Meaning : Print User and Group Identity\n\n"
        "Simple Explanation:\n"
        "It outputs the raw data of how the operating system sees you. It tells you your UID, GID, and every single group your account belongs to."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Format: id\n\n"
        "Example: id\n\n"
        "Pro-Tip: A UID of 0 always means 'root'. A UID of 1000 usually means the first normal human user created on the system."
    )

    pause()

    say(
        "Let's consult the watchtower and check our standing in the simulator."
    )

    # Interactive Prompt for id
    while True:
        command = prompt("Type the command to check your full numerical identity")
        clean_command = command.strip().lower()

        if clean_command == "id":
            say(
                "Look at that readout.\n\n"
                "You see 'uid=1000' and a string of group memberships. That is the actual blueprint of your permissions. You aren't just a name anymore—you're a set of keys."
            )
            break
        
        if clean_command.startswith("whoami"):
            error("That's a good instinct! But 'whoami' just gives us a friendly name. We want the deeper command that shows our numerical IDs and groups.")
        elif clean_command.startswith("su"):
            error("Careful! That changes who we are. Right now, we just want to *look* at who we currently are.")
        elif not clean_command.startswith("id"):
            error("Not quite. Think of a very short, two-letter abbreviation for the word 'identity'.")
        else:
            error("Almost! You just need the base command itself to check your clearance.")

    pause()

    say(
        "Now for the real magic. We are going to tie this together with what you learned in the last chapter."
    )

    card(
        "🌍 FIELD MISSION",
        "Let's prove how your identity changes on your real Kali machine.\n\n"
        "Open your real terminal and do this sequence:\n"
        "1. Run 'id' (Notice your UID is probably 1000).\n"
        "2. Run 'su' (Enter your password to become root).\n"
        "3. Run 'id' again (Notice your UID is now 0! You are officially the system creator).\n"
        "4. Type 'exit' to return to normal.\n\n"
        "Press Enter here once you've watched your clearance transform before your eyes."
    )

    pause()

    success(
        "Mission accomplished!\n\n"
        "You now know how to take power, and exactly how to verify you have it. Next, we use that power to change file locks with 'chmod'."
    )

    return True
