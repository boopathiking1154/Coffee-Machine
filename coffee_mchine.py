water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550

def print_stock():
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(coffee_beans, "of coffee beans")
    print(disposable_cups, "of disposable cups")
    print("${} of money".format(money))

def buy():
    global water
    global milk
    global money
    global coffee_beans
    global disposable_cups
    choice_of_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
    if choice_of_coffee == 'back':
        return
    choice_of_coffee = int(choice_of_coffee)
    if choice_of_coffee == 1:
        if water >= 250 and coffee_beans >=16:
            print("I have enough resources, making you a coffee!")
            water = water - 250
            coffee_beans = coffee_beans - 16
            money = money + 4
            disposable_cups = disposable_cups - 1
        else:
            if water < 250:
                print("Sorry, not enough water!")
            if coffee_beans < 16:
                print("Sorry, not enough coffee beans")
    if choice_of_coffee == 2:
        if water >= 350 and coffee_beans >= 20 and milk >= 75:
            print("I have enough resources, making you a coffee!")
            water = water - 350
            milk = milk - 75
            coffee_beans = coffee_beans - 20
            money = money + 7
            disposable_cups = disposable_cups - 1
        else:
            if water < 350:
                print("Sorry, not enough water!")
            if coffee_beans < 20:
                print("Sorry, not enough coffee beans")
            if milk < 75:
                print("Sorry, not enough milk")

    if choice_of_coffee == 3:
        if water >= 200 and coffee_beans >= 12 and milk >= 100:
            print("I have enough resources, making you a coffee!")
            water = water - 200
            milk = milk - 100
            coffee_beans = coffee_beans - 12
            money = money + 6
            disposable_cups = disposable_cups - 1
        else:
            if water < 200:
                print("Sorry, not enough water!")
            if coffee_beans < 12:
                print("Sorry, not enough coffee beans")
            if milk < 100:
                print("Sorry, not enough milk")



def fill():
    global water
    global milk
    global coffee_beans
    global disposable_cups
    add_water = int(input("Write how many ml of water do you want to add:\n"))
    add_milk = int(input("Write how many ml of milk do you want to add:\n"))
    add_coffee_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
    add_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    water += add_water
    milk += add_milk
    coffee_beans += add_coffee_beans
    disposable_cups += add_cups

def take():
    global money
    print("I gave you $", money)
    money = 0

while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    print()
    if action == 'buy':
        buy()
        print()
    if action == 'fill':
        fill()
        print()
    if action == 'take':
        take()
        print()
    if action == 'remaining':
        print_stock()
        print()
    if action == 'exit':
        break
