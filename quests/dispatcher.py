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
# Import Campaign 2 chapters
from quests.chapter13 import quest_c2_q1  # find
from quests.chapter14 import quest_c2_q2  # locate
from quests.chapter15 import quest_c2_q3  # grep
from quests.chapter16 import quest_c2_q4  # Pipe |
from quests.chapter17 import quest_c2_q5  # head
from quests.chapter18 import quest_c2_q6  # tail
from quests.linux_detective import quest_c2_boss  # Final Exam

def start_adventure(replay_quest=None):
    # If a specific quest is passed via Replay Mode, use it!
    # Otherwise, load their saved progress.
    if replay_quest is not None:
        current = replay_quest
    else:
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

    elif current == 7:
        return quest_7()

    elif current == 8:
        return quest_8()

    elif current == 9:
        return quest_9()

    elif current == 10:
        return quest_10()

    elif current == 11:
        return quest_11()

    elif current == 12:
        return quest_12()

    elif current == 13:
        return survivor_challenge()

    elif current == 14:
        return quest_c2_q1()

    elif current == 15:
        return quest_c2_q2()

    elif current == 16:
        return quest_c2_q3()

    elif current == 17:
        return quest_c2_q4()

    elif current == 18:
        return quest_c2_q5()

    elif current == 19:
        return quest_c2_q6()

    elif current == 20:
        return quest_c2_boss()

    print("\n🚧 More quests coming soon!")

    return False
