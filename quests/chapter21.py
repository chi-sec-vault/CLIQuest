from ui import card, success, error, prompt, pause
from mentor import say

def quest_21():

    card(
        "🧭 CAMPAIGN 3: GUARDIANS OF LINUX — CHAPTER 21",
        "The Key to the Kingdom\n\n"
        "Some doors are locked for a reason.\n"
        "When your regular account hits a brick wall, you need administrative power."
    )

    pause()

    say(
        "Let's set the scene, Explorer.\n\n"
        "You're investigating a secure system file—say, '/etc/shadow', where user credentials live.\n"
        "You type your command, full of confidence, and what do you get?\n\n"
        "...\n"
        "bash: /etc/shadow: Permission denied.\n\n"
        "The system slammed the door right in your face. To get past this, you have to step into the shoes of the administrator."
    )

    card(
        "🎯 MISSION",
        "Execute a restricted command using temporary administrative privileges."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : sudo\n\n"
        "Full Meaning : SuperUser DO\n\n"
        "Simple Explanation:\n"
        "It prefixes any command with root-level authority, allowing you to execute tasks\n"
        "that ordinary users cannot touch, without having to change your entire user session."
    )

    pause()

    card(
        "💡 HOW TO USE IT",
        "Format: sudo [command]\n\n"
        "Example: sudo cat /etc/shadow\n\n"
        "⚠️ Mentor Warning: With great power comes great responsibility.\n"
        "A single careless sudo command can permanently break system files. Use it with intention."
    )

    pause()

    say(
        "Let's practice making a safe, surgical strike with our primary administrative tool."
    )

    # Interactive Prompt for sudo (Strictly 1 command focus)
    while True:
        command = prompt("Type a command using temporary administrative privileges")
        clean_command = command.strip().lower()

        if clean_command.startswith("sudo "):
            say(
                "Notice what just happened?\n\n"
                "You prefixed your command with 'sudo'.\n"
                "The system checks your credentials, executes the task safely, and keeps your safety net intact."
            )
            break
        
        if "shadow" in clean_command and not clean_command.startswith("sudo"):
            error("Remember that permission wall? Without administrative power, the system blocks you. What prefix do we add?")
        elif not clean_command.startswith("sudo"):
            error("Try prefixing your command with the temporary administrator command ('sudo').")
        else:
            error("Make sure you include 'sudo' followed by a space and the command you want to run.")

    pause()

    say(
        "You've held the keys to the kingdom safely. Let's test it on your machine."
    )

    card(
        "🌍 FIELD MISSION",
        "Let's test administrative access on your real Kali machine.\n\n"
        "Open your real Kali terminal and run:\n"
        "sudo cat /etc/shadow\n\n"
        "Notice how it asks for your password? (Your keystrokes are hidden for security).\n"
        "Once entered, you'll see system secrets ordinary users can never reach.\n\n"
        "Press Enter here once you've experienced root power."
    )

    pause()

    success(
        "Mission accomplished!\n\n"
        "You understand the weight of administrative power. Next, we check our identity with 'id'."
    )

    return True
