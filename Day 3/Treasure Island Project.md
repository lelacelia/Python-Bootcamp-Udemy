# Day 3 Project: Treasure Island Game

Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.
Use the flow chart linked here to create the game logic.
Once you've completed the project, you can always extend the game and make it more interesting!

View demo (https://appbrewery.github.io/python-day3-demo/)

***Key knowledge***: Logic, If/Nested If/Multiple If statements, using and/or/not
```python
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction_select = input("You're at a cross road. Where do you want to go?\n   " + 'Type "left" or "right" \n')

if direction_select.lower() == "left":
    print("You've come to a lake. There is an island in the middle of the lake")
    action_select = input('  Type "wait" to wait for a boat. Type "swim" to swim across.\n')

    if action_select.lower() == "wait":
        print("You arrive at the island unharmed. "
              "There is a house with 3 doors.")
        door_select = input("  One red, one yellow and one blue. "
                            "Which color do you choose?\n")

        if door_select.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif door_select.lower() == "blue":
            print("You have been eaten by beasts. Game Over.")
        elif door_select.lower() == "yellow":
            print("You Win!!!")
        else:
            print("Game Over.")
    else:
        #game ends
        print("You have been attacked by an angry trout. Game Over.")


else:
    #game ends
    print("You fell into a hole. Game Over.")

```

