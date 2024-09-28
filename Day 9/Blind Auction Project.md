# Day 9: Build a Blind Auction Program

### Goal: Learn Python Dictionary, Key, and assign Value to Key

Demo: Link(https://appbrewery.github.io/python-day9-demo/)

```python
from art import logo

play = True
print(logo)
bid_record = {}

while play == True:
    # TODO-1: Ask the user for input
    bidder_name = input("What is your name? ")
    bidder_price = int(input("What is your price? $"))

    # TODO-2: Save data into dictionary {name: price}
    bid_record[bidder_name] = bidder_price

    # TODO-3: Whether if new bids need to be added
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    # TODO-4: Compare bids in dictionary

    if continue_bidding == "no":
        play = False
        max_bid = 0
        winner = ""
        tight = False

        for bidder_name in bid_record:
            if bid_record[bidder_name] > max_bid:
                tight = False
                max_bid = bid_record[bidder_name]
                winner = bidder_name
            elif bid_record[bidder_name] == max_bid:
                tight = True

        if tight:
            print("There was a tight, try again!")
        else:
            print(f"The winner is {winner} with a bid of ${max_bid}.")
    else:
        play = True
        print("\n" * 20)

```
