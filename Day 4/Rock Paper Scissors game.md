# Day 4: Build a Rock Paper Scissors game

### You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this.

Demo: Link (https://appbrewery.github.io/python-day4-demo/)
```python
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


options = [rock, paper, scissors]

#ask player to enter their choice:
you_choose_no = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))

if you_choose_no < 0 or you_choose_no >= 3:
    print("You have entered an invalid value!")

else:
    you_choose = options[you_choose_no]
    print(you_choose)

    #computer randomly select one number 0, 1, or 2
    rand_no = random.randint(0,2)

    #computer choice randomly selected from the options líst
    computer_choose = options[rand_no]
    print("Computer chooses:\n", computer_choose)


    #find who wins who loses
    if you_choose == rock and computer_choose == scissors:
        print("You win!")
    elif you_choose == scissors and computer_choose == paper:
        print("You win!")
    elif you_choose == paper and computer_choose == rock:
        print("You win!")
    elif you_choose == computer_choose:
        print("It's a tight!")
    else:
        print("You lose!")
```
