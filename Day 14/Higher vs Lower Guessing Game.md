# Day 14: Build a Higher-Lower Guessing Game
### Goal: practice debugging, step into, namespaces aka scope of a variable

Demo: Link(https://appbrewery.github.io/python-day14-demo/)

```python
# import random choice
# import game_data

from game_data import data
import random
from art import vs, logo


# TO-DO: Function to compare followers of celebA and celebB
def compare_follower (celebA, celebB):
    if celebA["follower_count"] > celebB["follower_count"]:
        return celebA
    elif celebA["follower_count"] < celebB["follower_count"]:
        return celebB

# T0-DO: Function to play game, take input and print results and play again
def play_highlow (who_win, score):
    raw_data = data
    playerA = who_win

    if who_win == {}:
        print(logo)
        playerA = random.choice(raw_data)

    playerB = random.choice(raw_data)

    if playerA == playerB:
        playerB = random.choice(raw_data)

    print(f"Compare A: {playerA['name']}, a {playerA['description']}, from {playerA['country']}")

    print(f"\n{vs}\n")

    print(f"Against B: {playerB['name']}, a {playerB['description']}, from {playerB['country']}")

    player_list = {"a":playerA, "b":playerB}
    who_win = compare_follower(playerA, playerB)
    print(who_win)

    #ask player to input choice
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    who_chosen = player_list[choice]

    if who_win == who_chosen:
        playerA = who_win
        score += 1
        print(f"You are right! Current score: {score}")
        play_highlow(who_win, score)

    else:
        print(f"\n" * 20)
        print(logo)
        print(f"Sorry that's wrong. Final score: {score}")
        score = 0
        who_win = {}

current_score = 0
winner = {}
play_highlow(winner, current_score)
```
