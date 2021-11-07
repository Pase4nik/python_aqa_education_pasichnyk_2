def ask_action():
    actions = {"buy": 'buy', "fill": 'fill', "take": 'take', "exit": 'exit', "remaining": 'remaining'}
    all_actions = ', '.join(actions.values())
    while True:
        answer = input(f"Write action ({all_actions}):\n")
        return answer


def ask_coffee_option():
    coffee_options = {1: "espresso", 2: "latte", 3: "cappuccino", 'back': "to main menu"}
    all_options = ', '.join(f"{key} - {value}" for key, value in coffee_options.items())
    answer = str(input(f"What do you want to buy? {all_options}\n"))
    return answer


def ask_fill_quantity(message):
    answer = int(input(message + '\n'))
    try:
        if answer >= 0:
            return answer
        else:
            print("You cannot fill negative")
    except ValueError:
        print("It's not a number!")


class CoffeeMachine:
    coffees = {"espresso": {"water": 250, "beans": 16, "cups": 1, 'money': -4},
               "latte": {"water": 350, "milk": 75, "beans": 20, "cups": 1, 'money': -7},
               "cappuccino": {"water": 200, "milk": 100, "beans": 12, "cups": 1, 'money': -6}}

    def __init__(self, water=0, milk=0, beans=0, cups=0, money=0):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def coffee_machine_status(self):
        return f'The coffee machine has:\n' \
               f'{self.water} of water\n' \
               f'{self.milk} of milk\n' \
               f'{self.beans} of coffee beans\n' \
               f'{self.cups} of disposable cups\n' \
               f'{self.money} of money'

    def check_capacity(self, which_coffee):
        if self.__dict__.get('water') < which_coffee.get(f'water', 0):
            print(f"Sorry, not enough water")
        elif self.__dict__.get('milk') < which_coffee.get(f'milk', 0):
            print(f"Sorry, not enough milk")
        elif self.__dict__.get('beans') < which_coffee.get(f'beans', 0):
            print(f"Sorry, not enough coffee beans")
        elif self.__dict__.get('cups') < which_coffee.get(f'cups', 0):
            print(f"Sorry, not enough coffee beans")
        else:
            for i in self.__dict__.keys():
                self.__dict__[f'{i}'] -= which_coffee.get(f'{i}', 0)
            return True

    def buyer(self):
        which_coffee = ask_coffee_option()
        if which_coffee == 'back':
            return
        elif which_coffee == '1':
            if self.check_capacity(self.coffees.get('espresso')):
                print("I have enough resources, making you an espresso! ")
        elif which_coffee == '2':
            if self.check_capacity(self.coffees.get('latte')):
                print('I have enough resources, making you a latte! ')
        elif which_coffee == '3':
            if self.check_capacity(self.coffees.get('cappuccino')):
                print('I have enough resources, making you a cappuccino! ')

    def filler(self):
        self.water += ask_fill_quantity("Write how many ml of water you want to add:")
        self.milk += ask_fill_quantity("Write how many ml of milk you want to add:")
        self.beans += ask_fill_quantity("Write how many grams of coffee beans you want to add:")
        self.cups += ask_fill_quantity("Write how many disposable coffee cups you want to add:")

    def seller(self):
        print(f"I gave you {self.money}\n")
        self.money = 0

    def action(self):
        while True:
            your_side = ask_action()
            if your_side == 'exit':
                quit()
            elif your_side == 'buy':
                self.buyer()
            elif your_side == 'fill':
                self.filler()
            elif your_side == 'take':
                self.seller()
            elif your_side == 'remaining':
                print(self.coffee_machine_status())
            return self.action()


def main():
    machine = CoffeeMachine(400, 540, 120, 9, 550)
    machine.action()


if __name__ == '__main__':
    main()
