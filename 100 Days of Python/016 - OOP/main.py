from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
register = MoneyMachine()

while True:
    options = menu.get_items()
    prompt = input(f"What would you like? ({options}): ").lower()
    drink = menu.find_drink(prompt)
    if prompt == "off":
        break
    if prompt == "report":
        coffee_machine.report()
        register.report()
        continue
    if not drink:
        continue
    if not coffee_machine.is_resource_sufficient(drink):
        continue
    if register.make_payment(drink.cost):
        coffee_machine.make_coffee(drink)
    else:
        continue
