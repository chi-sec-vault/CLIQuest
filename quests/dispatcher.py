from engine import load_progress
from quests.chapter1 import quest_1
from quests.chapter2 import quest_2


def start_adventure():

    progress = load_progress()
    current = progress["current_quest"]

    if current == 1:
        return quest_1()

    elif current == 2:
        return quest_2()

    print("🚧 More quests coming soon!")

    return False
