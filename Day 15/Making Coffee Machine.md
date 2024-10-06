# Day 15: Making a Coffee Machine

## Goal: practice using dictionary, while loop

```python
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# FUNCTION: check if having enough resources to make the order
def check_resource (required_amount, remaining_resource):
    ingredient_list = list(required_amount.keys())

    for ingredient in ingredient_list:
        need = required_amount[ingredient]
        have = remaining_resource[ingredient]
        if need > have :
            print (f"Sorry there is not enough {ingredient}!")
            return False

    return True

# FUNCTION: calculate total money in dollar amount from coins
def coin_converter (coin_count):
    rate = {"quarter": 0.25, "dime": 0.10, "nickle":0.05, "penny": 0.01}
    total = 0

    for coin_type in rate:
        total += coin_count[coin_type] * rate[coin_type]

    return total

is_on = True
money = 0

while is_on:
    order = input("What would you like? (espresso/latte/cappuccino)? (^0^) ")
    coin_list = ["quarter","dime","nickle", "penny"]

    # TO-DO: if "off", stop making coffee completely
    if order.lower() == "off":
        is_on = False
    # TO-DO: if "report", prin the amount of remaining resources and money earned
    elif order.lower() == "report":
        print(f"""
        Water: {resources["water"]}ml
        Milk: {resources["milk"]}ml
        Coffee: {resources["coffee"]}g
        Money: ${money}\n"""
        )
    else:
        #TO-DO: check to see if having enough resources using check_resources function
        resources_needed = MENU[order]["ingredients"]
        have_enough = check_resource(resources_needed, resources)

        if have_enough:
            order_price = MENU[order]["cost"]

            # TO-DO: ask customer for the number of coins
            coin_record = {}
            print("Please insert coins.")

            for coin in coin_list:
                coin_record[coin] = int(input(f"How many {coin}s?: "))

            total_money = coin_converter(coin_record)

            #TO-DO: Check to see if customer has enough money for the order
            if order_price > total_money:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = round(total_money - order_price, 2)
                if change > 0:
                    print(f"Here is the ${change} dollar in change.")

                #TO-DO: Subtract used ingredient from resource & add money earned from order
                ingredient_used = list(MENU[order]["ingredients"])

                for item in ingredient_used:
                    used_amount = MENU[order]["ingredients"][item]
                    resources[item] -= used_amount

                money += order_price

                #TO-DO: Give order to customer:
                print(f"Here is your {order}. Enjoy!")

```
