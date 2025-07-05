from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_state = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
profit = 0
while machine_state:
    user_coffee = input("Enter Your Coffee:\n1.Espresso\n2.Latte\n3.Cappuccino\n").lower()
    if user_coffee == "off":
        machine_state = False
    elif user_coffee == "report":

        coffee_maker.report()
        money_machine.report()
    elif user_coffee != "espresso" and user_coffee != "latte" and user_coffee != "cappuccino":
        print("Invalid Input")
    else:
        drink = menu.find_drink(user_coffee)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
