from engine import load_progress
from quests.chapter1 import quest_1


def start_adventure():

    progress = load_progress()

    current = progress["current_quest"]

    if current == 1:
        return quest_1()

    print("🚧 More quests coming soon!")

    return False
