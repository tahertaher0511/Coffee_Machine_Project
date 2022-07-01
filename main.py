from data_file import menu

# user_choice = input("What would you like?: ('espresso'/'latte'/'cappuccino')\n")

machine_off = False

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def is_sufficient_ingredient(order_ingredients):
    """Returned true when order can be made and false if ingredients are insufficient."""
    for key in order_ingredients:
        if order_ingredients[key] >= resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def process_coins():
    """Returned calculated from coins inserted"""
    print("Please insert coins?: ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return true if payment is accepted or false if money is insufficient."""
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for key in order_ingredients:
        resources[key] -= order_ingredients[key]
    print(f"Here is your {drink_name}")


def check_user_input(user_input):
    if user_input not in ["espresso","latte","capuccino", "report"]:
        return False
    return True


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/capuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice != check_user_input(choice):
        print("Choose you drink to continue, or report, or off to shut down your coffee machine.")
    else:
        drink = menu[choice]
        if is_sufficient_ingredient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
