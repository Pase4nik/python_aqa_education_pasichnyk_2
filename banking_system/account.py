import sqlite3
from termcolor import cprint


class Account(BaseException):
    __CONNECTION = sqlite3.connect('card.s3db')
    __CURSOR = __CONNECTION.cursor()

    def __init__(self, data):
        self.id = data.id
        self.card = data.card
        self.pin = data.pin
        self.balance = data.balance

    def account_menu(self):
        options = {1: 'Balance', 2: 'Add Income', 3: 'Do Transfer', 4: 'Close Account', 5: 'Log Out', 0: 'Exit'}
        actions = {1: self.show_balance, 2: self.add_income, 3: self.do_transfer,
                   4: self.close_account, 5: self.log_out, 0: exit}
        for i in options:
            print(f"{i}: {options.get(i)}", sep="\n")
        try:
            user_choice = int(input('> '))
            actions[user_choice]()
        except KeyError:
            cprint("This option does not exist.\nPlease try again", "red")
        return self.account_menu()

    def show_balance(self):
        print('Balance:', self.balance)
        return self.account_menu()

    def add_income(self):
        print("Enter income:")
        try:
            income_amount = input("> ")
            self.balance += income_amount
            self.__CURSOR.execute(f'UPDATE CARD SET balance = {self.balance} WHERE id = {self.id}')
            self.__CONNECTION.commit()
            print('Income was added')
        except TypeError:
            cprint("Please, enter digits only", 'red')
        return self.account_menu()

    def do_transfer(self):
        print("Transfer:", "Enter card number:", sep="\n")
        card = input("> ")
        if len(card) == 16 and card.isdigit():
            if card != self.card:
                other_id = self.get_account_id(card)
                if other_id:
                    other_id = other_id[0]
                    print("Enter how much money you want to transfer:")
                    amount = input("> ")
                    if amount.isdigit() and int(amount) > 0:
                        amount = int(amount)
                        if amount <= self.balance:
                            self.balance -= amount
                            self.__CURSOR.execute(f'UPDATE CARD SET balance = {self.balance} WHERE id = {self.id}')
                            self.__CURSOR.execute(f'UPDATE CARD SET balance = '
                                                  f'balance + ({amount}) WHERE id = {other_id}')
                            self.__CONNECTION.commit()
                            cprint("\n Success!", 'green')
                        else:
                            cprint("\n Not enough money!", 'red')
                    else:
                        cprint("\n Incorrect amount!", 'red')
                else:
                    cprint("\n Such a card does not exist.", 'red')
            else:
                cprint("\n You can't transfer money to the same account!", 'red')
        else:
            cprint("\n Probably you made mistake in the card number. Please try again!", 'red')
        return self.account_menu()

    def get_account_id(self, card):
        self.__CURSOR.execute(f'''SELECT id FROM CARD WHERE NUMBER = {card}''')
        account_id = self.__CURSOR.fetchone()
        return account_id

    def close_account(self):
        self.__CURSOR.execute(f'DELETE FROM CARD WHERE id = {self.id}')
        cprint("The account has been closed!", 'green')
        self.__CONNECTION.commit()

    @staticmethod
    def log_out():
        cprint(" You have successfully logged out!", "green")
