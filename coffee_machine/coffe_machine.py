import time


class CoffeeMachine:
    ingredients = {
        "water": 200,
        "milk": 50,
        "coffee_beans": 15,
    }
    status_list = [
        'Starting to make a coffee', 'Grinding coffee beans', 'Boiling water',
        'Mixing boiled water with crushed coffee beans', 'Pouring coffee into the cup ',
        'Pouring some milk into the cup', 'Coffee is ready!'
    ]
    coffees = {"espresso": {"water": 250, "beans": 16, "cups": 1, 'money': -4},
               "latte": {"water": 350, "milk": 75, "beans": 20, "cups": 1, 'money': -7},
               "cappuccino": {"water": 200, "milk": 100, "beans": 12, "cups": 1, 'money': -6}}

    def __init__(self, water=0, milk=0, beans=0, cups=0, money=0):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def ingredients_amount(self):
        cups = int(input('Write how many cups of coffee you will need:\n'))
        for i in self.ingredients:
            self.ingredients[f"{i}"] = self.ingredients.get(i) * cups
        string = f"For {cups} cups of coffee you will need:\n" \
                 f"{self.ingredients.get('water')} ml of water\n" \
                 f"{self.ingredients.get('milk')} ml of milk\n" \
                 f"{self.ingredients.get('coffee_beans')} g of coffee beans"
        return string

    def cups_availability(self):
        self.water = int(input("Write how many ml of water the coffee machine has:\n"))
        self.milk = int(input("Write how many ml of milk the coffee machine has:\n"))
        self.beans = int(input("Write how many ml of beans the coffee machine has:\n"))
        cups = int(input('Write how many cups of coffee you will need:\n'))

        available_water = int(self.water // 200)
        available_milk = int(self.milk // 50)
        available_beans = int(self.beans // 15)
        possible_cups = int(min(available_water, available_milk, available_beans))
        extra_cups = possible_cups - cups
        answers = [f"Yes,I can make that amount of coffee (and even {extra_cups} more than that)",
                   "Yes, I can make that amount of coffee",
                   f"No, I can make only {possible_cups} cups of coffee"]
        if possible_cups == cups:
            return answers[1]
        elif possible_cups < cups:
            return answers[2]
        elif possible_cups > cups:
            return answers[0]

    def about_coffee_machine(self):
        return f'''\nThe coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
{self.money} of money'''

    def check_capacity(self, which_coffee):
        for i in self.__dict__.keys():
            if self.__dict__.get(f'{i}') < which_coffee.get(f'{i}', 0):
                print(f"Sorry, not enough {i}")
                break
            self.__dict__[f'{i}'] -= which_coffee.get(f'{i}', 0)
            if self.__dict__.get(f'{i}') >= which_coffee.get(f'{i}', 0):
                print("I have enough resources, making you a coffee! ")
                break

    def buyer(self):
        which_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:\n")
        if which_coffee == '1':
            # espresso = {"water": 250, "beans": 16, "cups": 1, 'money': -4}
            self.check_capacity(self.coffees.get('espresso'))
        elif which_coffee == '2':
            latte = {"water": 350, "milk": 75, "beans": 20, "cups": 1, 'money': -7}
            self.check_capacity(latte)
        elif which_coffee == '3':
            cappuccino = {"water": 200, "milk": 100, "beans": 12, "cups": 1, 'money': -6}
            self.check_capacity(cappuccino)
        elif which_coffee == 'back':
            self.action()

    def filler(self):
        try:
            water = int(input("Write how many ml of water you want to add:\n"))
            milk = int(input("Write how many ml of milk you want to add:\n"))
            beans = int(input("Write how many grams of coffee beans you want to add:\n"))
            cups = int(input("Write how many disposable coffee cups you want to add:\n"))
        except ValueError:
            print('Wrong value was entered!')
            return self.filler()
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    def seller(self):
        print(f"I gave you {self.money}\n")
        self.money = 0

    def action(self):
        while True:
            your_side = str(input("\nWrite action (buy, fill, take, remaining, exit):\n"))
            if your_side == 'exit':
                quit()
            elif your_side == 'buy':
                self.buyer()
            elif your_side == 'fill':
                self.filler()
            elif your_side == 'take':
                self.seller()
            elif your_side == 'remaining':
                print(self.about_coffee_machine())
            return self.action()


if __name__ == '__main__':
    # my_coffee = CoffeeMachine()
    # print("===========Phase 1==============\n")
    # time.sleep(1)
    # for coffee_state in my_coffee.status_list:
    #     time.sleep(1)
    #     print(coffee_state)
    # print("\n===========Phase 2==============\n")
    # print(my_coffee.ingredients_amount())
    # print("\n===========Phase 3==============\n")
    # print(my_coffee.cups_availability())
    # print("\n===========Phase 4-6==============\n")
    my_coffee2 = CoffeeMachine(400, 540, 120, 9, 550)
    print(my_coffee2.action())
