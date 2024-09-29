# Day 11: Create a BlackJack game with the computer

### Game Details:
Our Blackjack Game House Rules
- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
  
Use the following list as the deck of cards: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
- The cards in the list have equal probability of being drawn.
- Cards are **not** removed from the deck as they are drawn.
- The computer is the dealer.

Demo: Link(https://appbrewery.github.io/python-day11-demo/)

```python
from random import choice
from art import logo

# Function to draw a random card from the remaining deck when player agree to do so
def draw_card(draw, deck):
    draw_result = 0
    if draw == "y":
        draw_result = choice(deck)
    return draw_result


# Function to sum cards on hand
def sum_hand (hand):
    player_score = sum(hand)

    if player_score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        player_score = sum(hand)

    return player_score


#Function to find out one lose:
def game_end (scores, your_choice):
    for player in scores:
        if scores[player] > 21:
            return True
    if your_choice == "n":
        return True

    return False


# Function to compare results
def compare(score_player, score_computer):
    if score_player > 21:
        if score_computer > 21:
            return "Both players lose."
        else:
            return "You went over. You lose 😭"
    if score_player == 21:
        if score_player == score_computer:
            return "Draw. Both players have a BlackJack"
        else:
            return "Win with a Blackjack 😎"
    else:
        if score_player == score_computer:
            return "Draw 🙃"
        elif score_player < score_computer:
            if score_computer > 21:
                return "Your opponent went over. You win 😁"
            elif score_computer == 21:
                return "Lose, opponent has Blackjack 😱"
            else:
                return "You lose 😤"
        else:
            return "You win 😁 "


def play_blackjack ():
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    game_over = False
    hand_record = {"You": [], "Computer": []}
    score_record = {"You": 0, "Computer": 0}
    choice_record = {"You": "y", "Computer": "y"}
    player_list = ["You", "Computer"]

    while not game_over:
        for player in player_list:
            new_card = 0
            new_card = draw_card(choice_record[player], cards)
            hand_record[player].append(new_card)
            score_record[player] = sum_hand(hand_record[player])

        if len(hand_record["You"]) >= 2:
            print(f"Your cards: {hand_record["You"]}, current score: {score_record["You"]}")
            print(f"Computer's first card: {hand_record["Computer"][0]}")

            choice_record["You"] = input("Type 'y' to get another card, type 'n' to pass: ")

            if score_record["Computer"] < 21:
                choice_record["Computer"] = choice(["y", "n"])

            for player in player_list:
                new_card = 0
                new_card = draw_card(choice_record[player], cards)
                hand_record[player].append(new_card)
                score_record[player] = sum_hand(hand_record[player])

            game_over = game_end(score_record,choice_record["You"])

            if game_over:
                print(f"Your final hand: {hand_record["You"]}, final score: {score_record["You"]} \n" +
                      f"Computer's final hand: {hand_record["Computer"]}, final score: {score_record["Computer"]}")

                print(compare(score_record["You"], score_record["Computer"]))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n'") == "y":
    print("\n" * 30)
    play_blackjack()
```
