from replit import clear

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
    },
    "macchiato": {
        "ingredients": {
            "water": 200,
            "milk": 75,
            "coffee": 1800,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.00


def report(register):
    clear()
    print("Generating report:")
    for i in resources:
        print(f"    {i.title()}:  {resources[i]}ml")
    print(f"    Money: ${register}")


def check(beverage):
    """ cycles through beverages and checks to see if resources are available to create beverage. if the resources
    are available returns '1', if they are not available returns '0'"""
    for ingredient, amount in beverage["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return 0
    return 1


def make_drink(option):
    global resources
    for ingredient in MENU[option]['ingredients']:
        resources[ingredient] -= MENU[option]['ingredients'][ingredient]
    print(f"Here is your {option}, enjoy!")


def process_coins(option):
    global money
    print(f"Processing coins. {option} costs ${MENU[option]['cost']}")
    paying = True
    while paying:
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickels = int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))
        total_cents = (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies
        payment = total_cents / 100
        if payment < MENU[option]['cost']:
            print(f"Sorry, not enough money. ${payment} refunded.")
            return 0
        change = payment - MENU[option]['cost']
        print(f"Here is ${change} in change.")
        paying = False
    money += MENU[option]['cost']
    make_drink(option)
    return


def drink(ingredients, selection):
    if check(ingredients) == 0:
        return 0
    elif check(ingredients) == 1:
        return process_coins(option=selection)


def machine_on():
    menu_items = []
    prompt = ""
    for i in MENU:
        menu_items.append(i)
    while prompt != "off" or prompt not in MENU:
        prompt = input(f"What would you like? ({'/'.join(menu_items)}): ").lower()
        if prompt == "off":
            return
        elif prompt == "report":
            report(money)
        elif prompt in MENU:
            drink(ingredients=MENU[prompt], selection=prompt)
        else:
            print("Select again.")


clear()
machine_on()
