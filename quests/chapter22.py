from ui import card, success, error, prompt, pause
from mentor import say

def quest_22():

    card(
        "🧭 CAMPAIGN 3: GUARDIANS OF LINUX — CHAPTER 22",
        "The Master Key\n\n"
        "Borrowing power for a quick fix is one thing.\n"
        "But when you're doing heavy maintenance, asking for permission before every single task gets exhausting."
    )

    pause()

    say(
        "It's a unique feeling the first time you do this, Explorer.\n\n"
        "Normally, Linux protects itself from you. But sometimes, you need to step out of your regular account "
        "and put on the administrator's suit completely. You stop asking for permission and start giving orders.\n\n"
        "Just remember: Linux assumes you know exactly what you are doing. If you tell it to delete everything, it won't ask 'Are you sure?'—it will just do it."
    )

    card(
        "🎯 MISSION",
        "Swap your current user session entirely over to the root administrator."
    )

    pause()

    card(
        "📖 COMMAND",
        "Command      : su (or su root)\n\n"
        "Full Meaning : Switch User\n\n"
        "Simple Explanation:\n"
        "This command logs you directly into another user's shoes. If you don't type a specific name, "
        "the system assumes you want to become 'root'—the all-powerful creator account."
    )

    pause()

    card(
        "💡 THE DANGER ZONE",
        "⚠️ Why admins respect the root shell:\n\n"
        "When you use 'su', you are living in God mode until you manually type 'exit'.\n"
        "If you walk away to grab coffee while a root shell is open, anyone who sits at your keyboard "
        "owns the entire system."
    )

    pause()

    say(
        "Alright, deep breath. Let's practice stepping into the administrator's shoes."
    )

    # Interactive Prompt for su
    while True:
        command = prompt("Type the command to switch your user session to root")
        clean_command = command.strip().lower()

        if clean_command in ["su", "su root", "su -"]:
            say(
                "And just like that, the walls come down.\n\n"
                "You are now running a full root shell. Every command you type from here carries absolute authority."
            )
            break
        
        if clean_command.startswith("sudo "):
            error("Ah, you reached for 'sudo'—that's actually a great habit for single tasks! But this time, we want to move past a temporary pass and take over the whole session.")
        elif not clean_command.startswith("su"):
            error("Not quite. We're looking for the specific, short command that lets you switch your user.")
        else:
            error("You've almost got it. Take a breath and double-check how you type the switch user command.")

    pause()

    say(
        "You handled that perfectly. Now, I want you to feel what it's like on a real system."
    )

    card(
        "🌍 FIELD MISSION",
        "Let's grab the master key on your real Kali machine.\n\n"
        "Open your real Kali terminal and run:\n"
        "su\n\n"
        "Enter your password when prompted. Now, look closely at the left side of your terminal.\n"
        "Did you see your prompt change from a dollar sign ($) to a hashtag (#)?\n"
        "That hashtag is Linux's universal symbol for: 'Caution, you are now root.'\n\n"
        "Crucial safety habit: Type 'exit' right now to step back down to your normal, safe account.\n\n"
        "Press Enter here once you've felt the shift and safely exited."
    )

    pause()

    success(
        "Mission accomplished!\n\n"
        "You've worn the suit and stepped back out safely. Next, we are going to use 'id' to prove exactly who we are."
    )

    return True
