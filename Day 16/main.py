from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_continue = True

# TO-DO: create objects
menu_control = Menu()

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

option_string = menu_control.get_items()

#this is the list of drink, name, their ingredients, cost
drink_list = menu_control.menu #menu is the attribute to the object created by the Menu() class

while is_continue:
    # TO-DO: ask for customer's order
    order = input(f"What would you like? {option_string}")

    # TO-DO: check input value
    '''
    if off, stop immediately
    if report, return value
    
    '''
    if order.lower() == "off":
        is_continue = False
    elif order.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        for drink in drink_list:
            if drink.name == order:
                # TO-DO: Check to see if the coffee maker has enough resources to make the order
                price = drink.cost
                enough_resource = coffee_maker.is_resource_sufficient(drink)
                if enough_resource:
                   enough_money = money_machine.make_payment(price)

                   # TO-DO: If enough resource, check to see if customer can pay for the cost
                   if enough_money:
                       coffee_maker.make_coffee(drink)




