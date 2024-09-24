# Day 5: Create a Hangman Game

### Goal: Learning how to use for and while logic; adding character to a string and find whether or not a character is in a string

Demo: Link (https://appbrewery.github.io/python-day7-demo/)

```python
import random
import hangman_words
import hangman_art

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words.word_list

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_list = ""

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************You have {lives}/6 lives left****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in correct_list:
        print(f"You've already guessed a {guess}. Try again.")

    display = ""

    for letter in chosen_word:

        if letter == guess:
            correct_list= f'{correct_list}{guess}'

        if letter in correct_list:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.


    if guess not in chosen_word:
        lives -= 1
        print (f"You have guessed {guess}, which is not in the word. You lose a life")
        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"YOU LOSE! It was {chosen_word}.")

    if "_" not in display:
        game_over = True
        print("YOU WIN!")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    stages = hangman_art.stages
    print(stages[lives])

```
