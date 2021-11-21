from termcolor import cprint
from bank import BankingSystem


class Account(BaseException):
    __CONNECTION = BankingSystem.CONNECTION
    __CURSOR = BankingSystem.CURSOR

    def __init__(self, data):
        self.id = data.id
        self.card = data.card
        self.pin = data.pin
        self.balance = data.balance

        self.ACCOUNT_ACTIONS = {1: self.show_balance, 2: self.add_income, 3: self.do_transfer,
                                4: self.close_account, 5: self.log_out, 0: self.exit}

    def show_balance(self):
        print('Balance:', self.balance)

    def add_income(self):
        print("Enter income:")
        try:
            income_amount = int(input("> "))
            self.balance += income_amount
            self.__CURSOR.execute(f'UPDATE CARD SET balance = {self.balance} WHERE id = {self.id}')
            self.__CONNECTION.commit()
            cprint('Income was added', 'green')
        except TypeError:
            cprint("Please, enter digits only", 'red')

    def do_transfer(self):
        print("Transfer:", "Enter card number:", sep="\n")
        card = input("> ")
        print("Enter how much money you want to transfer:")
        amount = input("> ")
        if self.check_valid(card, amount):
            amount = int(amount)
            self.balance -= amount
            self.__CURSOR.execute(f'UPDATE CARD SET balance = {self.balance} WHERE id = {self.id}')
            self.__CURSOR.execute(f'UPDATE CARD SET balance = balance + ({amount}) WHERE number = {card}')
            self.__CONNECTION.commit()
            cprint("\n Success!", 'green')

    def check_valid(self, card, amount):
        if self.check_valid_card(card):
            if self.check_valid_amount(amount):
                return True

    def check_valid_card(self, card):
        if len(card) != 16 or card.isdigit() is False:
            cprint("\n Probably you made mistake in the card number. Please try again!", 'red')
        elif card == self.card:
            cprint("\n You can't transfer money to the same account!", 'red')
        else:
            return True

    def check_valid_amount(self, amount):
        if amount.isdigit() is False or int(amount) < 0:
            cprint("\n Incorrect amount!", 'red')
        elif int(amount) > self.balance:
            cprint("\n Not enough money!", 'red')
        else:
            return True

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

    def exit(self):
        pass
