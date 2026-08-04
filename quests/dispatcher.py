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

# --- CAMPAIGN 3 IMPORTS ---
from quests.chapter19 import quest_19  # ls -a
from quests.chapter20 import quest_20  # ls -la
from quests.chapter21 import quest_21  # sudo
from quests.chapter22 import quest_22  # su
from quests.chapter23 import quest_23  # id
from quests.chapter24 import quest_24  # chmod
from quests.chapter25 import quest_25  # chown
from quests.guardian_of_linux import challenge_3  # Lockdown Boss Fight

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

# --- CAMPAIGN 2: LINUX DETECTIVE ---
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

# --- CAMPAIGN 3: GUARDIANS OF LINUX ---
    elif current == 21: return quest_19()
    elif current == 22: return quest_20()
    elif current == 23: return quest_21()
    elif current == 24: return quest_22()
    elif current == 25: return quest_23()
    elif current == 26: return quest_24()
    elif current == 27: return quest_25()
    elif current == 28: return challenge_3()

    print("\n🚧 More quests coming soon!")

    return False
