from engine import load_progress
from quests.chapter1 import quest_1
from quests.chapter2 import quest_2
from quests.chapter3 import quest_3
from quests.chapter4 import quest_4
from quests.chapter5 import quest_5
from quests.chapter6 import quest_6
from quests.chapter7 import quest_7  # <--- Import Chapter 7
from quests.chapter8 import quest_8  # <--- Import Chapter 8
from quests.chapter9 import quest_9  # <--- Import Chapter 9
from quests.chapter10 import quest_10  # <--- Import Chapter 10
from quests.chapter11 import quest_11  # <--- At the top
from quests.chapter12 import quest_12
from quests.linux_survivor import survivor_challenge  # <--- Import the survivor trial

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

    elif current == 7:  # <--- Handle Chapter 7 dispatch
        return quest_7()

    elif current == 8:
        return quest_8()  # <--- Handle Chapter 8

    elif current == 9:
        return quest_9()  # <--- Handle Chapter 9

    elif current == 10:
        return quest_10()

    elif current == 11:
        return quest_11()

    elif current == 12:
        return quest_12()

    elif current == 13:
        return survivor_challenge()  # <--- Trigger the final trial!

    print("🚧 More quests coming soon!")

    return False
