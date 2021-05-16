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


def check_resources(selection_user):
    water_machine = resources["water"]
    milk_machine = resources["milk"]
    coffee_machine = resources["coffee"]
    if selection_user == 'expresso':
        if water_machine < int(MENU['espresso']['ingredients']['water']):
            print("Sorry, there is not enough water. ")
        elif coffee_machine < int(MENU['espresso']['ingredients']['coffee']):
            print("Sorry, there is not enough coffee. ")

    if selection_user == 'latte':
        if water_machine < int(MENU['latte']['ingredients']['water']):
            print("Sorry, there is not enough water. ")
        elif coffee_machine < int(MENU['latte']['ingredients']['coffee']):
            print("Sorry, there is not enough coffee. ")
        elif milk_machine < int(MENU['latte']['ingredients']['milk']):
            print("Sorry, there is not enough milk. ")
    
    if selection_user == 'cappuccino':
        if water_machine < int(MENU['cappuccino']['ingredients']['water']):
            print("Sorry, there is not enough water. ")
        elif coffee_machine < int(MENU['cappuccino']['ingredients']['coffee']):
            print("Sorry, there is not enough coffee. ")
        elif milk_machine < int(MENU['cappuccino']['ingredients']['milk']):
            print("Sorry, there is not enough milk. ")

def money_comparison(total_coins, product_selected):
    if product_selected == 'expresso':
        price = int(MENU['expresso']['cost'])
    elif product_selected == 'latte':
        price = int(MENU['latte']['cost'])
    elif product_selected == 'cappucchino':
        price = int(MENU['cappucchino']['cost'])
    
    if price > float(total_coins):
        print("Sorry, that's not enough money. money refunded")
    elif float(total_coins) > int(price):
        print(f"Here is ${float(total_coins) - int(price)} dollars in change.")

    else:
        print(f"Here is your {product_selected}. Enjoy!")
        if product_selected == 'expresso':
            resources["money"] = resources["money"] + MENU['espresso']['cost']
        elif product_selected == 'latte':
            resources["money"] = resources["money"] + MENU['latte']['cost']
        elif product_selected == 'cappucchino':
            resources["money"] = resources["money"] + MENU['cappuccino']['cost']      

def update_resources(selection_user):
    if selection_user == 'expresso':
        resources["water"]  = resources["water"] - int(MENU['espresso']['ingredients']['water'])
        resources["coffee"]  = resources["coffee"] - int(MENU['espresso']['ingredients']['coffee'])
    
    elif selection_user == 'latte':
        resources["water"]  = resources["water"] - int(MENU['latte']['ingredients']['water'])
        resources["milk"]  = resources["milk"] - int(MENU['latte']['ingredients']['milk'])
        resources["coffee"]  = resources["coffee"] - int(MENU['latte']['ingredients']['coffee'])

    elif selection_user == 'cappuccino':
        resources["water"]  = resources["water"] - int(MENU['cappuccino']['ingredients']['water'])
        resources["milk"]  = resources["milk"] - int(MENU['latte']['ingredients']['milk'])
        resources["coffee"]  = resources["coffee"] - int(MENU['cappuccino']['ingredients']['coffee'])
    
def last_function():
    check_resources(choose)

    print("Please, insert coins. ")

    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    nickles = int(input("how many nickles? "))
    pennies = int(input("how many pennies? "))

    total = str(round((quarters*0.25)+(dimes*0.1)+(nickles*5/100)+(pennies*1/100),2))
    print(total)

    money_comparison(total, choose)

    update_resources(choose)

is_finished = False

# creating a new dict. value on the resources dict. 
resources["money"] = 0

while is_finished == False :
    total = 0
    choose = input("What would you like? (espresso/latte/cappuccino):  ").lower()

    if choose == 'espresso':
        print("espresso")
        last_function()
    elif choose == 'latte':
        print('latte')
        last_function()
    elif choose == 'cappucchino':
        print('cappuchino')
        last_function()
    elif choose == 'off':
        print('off')
        is_finished = True
    elif choose == 'report':
        print("Water: ", resources["water"])
        print("Milk: ", resources["milk"])
        print("Coffee: ", resources["coffee"])
        print("Money: $", resources["money"])
    else:
        print('wrong selection')
    