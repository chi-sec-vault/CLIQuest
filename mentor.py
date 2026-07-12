from ui import card, pause


def say(message):
    """
    Display a mentor message.
    """
    card("🧙 MENTOR", message)
    pause()


def congratulate(message):
    """
    Display a congratulatory message.
    """
    card("🎉 MENTOR", message)
    pause()


def hint(message):
    """
    Give the Explorer a helpful hint.
    """
    card("💡 HINT", message)
    pause()


def warning(message):
    """
    Display a safety warning.
    """
    card("⚠️ WARNING", message)
    pause()
