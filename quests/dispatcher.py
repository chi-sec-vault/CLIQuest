from engine import load_progress
from quests.chapter1 import quest_1
from quests.chapter2 import quest_2
from quests.chapter3 import quest_3
from quests.chapter4 import quest_4
from quests.chapter5 import quest_5
from quests.chapter6 import quest_6

def start_adventure():

    progress = load_progress()
    current = progress["current_quest"]

    if current == 1:
        return quest_1()

    elif current == 2:
        return quest_2()

    elif current == 3:
        return quest_3()

    elif current == 4:
        return quest_4()

    elif current == 5:
        return quest_5()

    elif current == 6:
        return quest_6()

    print("🚧 More quests coming soon!")

    return False
