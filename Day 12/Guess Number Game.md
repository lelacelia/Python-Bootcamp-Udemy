# Day 12: Guessing Number Game

### Goal: Practice using function, global variable (did not use this in my code)

Demo: Link (https://appbrewery.github.io/python-day12-demo/)

```python
from random import randint
from art import logo

def guessing_game(attempt_count, answer, guess):
    if guess < answer:
        print ("Too low.\nGuess again.")
        attempt_count -= 1
    elif guess > answer:
        print ("Too high.\nGuess again.")
        attempt_count -= 1
    else:
        print (f"You got it! The answer was {answer}")
        attempt_count = 0 #use this to end the while loop that call this function

    if attempt_count == 0 and not guess == answer:
        print ("You've run out of guesses, you lose.")

    return attempt_count

print(logo)
print("Welcome to the Number Guessing Game! \n" +
      "I'm thinking of a number between 1 and 100.")
computer_choice = randint(1, 101)
print(f"computer chooses {computer_choice}")

game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if game_level == "easy":
    attempts = 10
else:
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess_input = int(input("Make a guess:"))
    attempts = guessing_game(attempts, computer_choice, guess_input)
```
