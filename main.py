from Recipes import MENU, resources
import time


def choice_coffee():
    if choice == '1':
        cafe = "espresso"
        return cafe
    if choice == '2':
        cafe = "latte"
        return cafe
    if choice == '3':
        cafe = "cappuccino"
        return cafe
    if choice == 'report':
        cafe = 'report'
        return cafe
    if choice == "off":
        cafe = 'off'
        return cafe


def check_resources(recurse):
    for key in MENU[recurse]['ingredients']:
        if resources[key] < MENU[recurse]['ingredients'][key]:
            return key
    return 'OK'


def check_money(cafe):
    t_money = quarter + dimes + nickles + pennies
    if t_money < MENU[cafe]["cost"]:
        return False
    else:
        global change
        change = t_money - MENU[cafe]["cost"]
        return True


def process(item):
    profit = (quarter + dimes + nickles + pennies) - change
    resources['money'] += profit
    if change > 0:
        print(f"Your change is: ${round(change, 2)}")
    Make_Coffee(item)
    print(f"Here is you {item}. Enjoy!")


def Make_Coffee(item):
    for key in MENU[item]['ingredients']:
        resources[key] -= MENU[item]['ingredients'][key]


# CONSTANTS
quarter = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
change = 0

while True:
    print("PRESS '1' for espresso. Cost $1.5\n"
          "PRESS '2' for latte. Cost $2.5\n"
          "PRESS '3' for cappuccino. Cost $3")
    choice = input("------>")
    cafe = choice_coffee()

    if cafe != 'report' and cafe != 'off':
        recurso = check_resources(cafe)
        if recurso == "OK":
            print("Insert coins.")
            quarter *= float(input("How many quarters?:----->"))
            dimes *= float(input("How many dimes?:----->"))
            nickles *= float(input("How many nickles?:----->"))
            pennies *= float(input("How many pennies?:----->"))
            # print(cafe)
            if check_money(cafe):
                process(cafe)
            else:
                print("Sorry that's not enough money. Money refunded")
        else:
            print(f"Sorry there is not enough {recurso}")
    elif cafe == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif cafe == 'off':
        exit()



