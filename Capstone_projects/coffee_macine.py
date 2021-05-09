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
            "water": 2500,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coffee_bill(order):
    for i in MENU:
        if i == order:
            a = MENU[i]
    return a["cost"]


def report(order):
    for i in MENU:
        if i == order:
            a = MENU[i]
    water = resources["water"]
    milk = resources["milk"]
    coffe = resources["coffee"]
    for i in range(3):

        order_water = a["ingredients"]["water"]
        order_milk = a["ingredients"]["milk"]
        order_coffee = a["ingredients"]["coffee"]

        resources["water"] -= order_water
        resources["milk"] -= order_milk
        resources["coffee"] -= order_coffee
    print(
        f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}"
    )




def total_money(quarters_input, dimes_input, nickles_input, pennies_input):
    dimes = 0.10
    quarters = 0.25
    nickles = 0.05
    pennies = 0.01
    total_bill = (
        quarters_input * quarters
        + dimes * dimes_input
        + nickles * nickles_input
        + pennies * pennies_input
    )
    return total_bill


of = False
while of == False :
    coffee = input("What coffee would you like: ")
    if coffee == "report":
        resources = report(coffee)
        print(resources)
    quarters_input = int(input("how many quarters?: "))
    dimes_input = int(input("how many dimes: "))
    nickles_input = int(input("how many nickles: "))
    pennies_input = int(input("how many pennies: "))
    total_money = total_money(quarters_input, dimes_input, nickles_input, pennies_input)
    actual_bill = coffee_bill(coffee)   
    if total_money < actual_bill:
        print("Sorry that's not enough money. Money refunded.")
    )

    else:
        total_bill = total_money - actual_bill
        print(f"Here is ${total_bill} in change.")


    



