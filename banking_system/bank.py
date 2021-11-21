from account import Account
from card import generate_card_number, generate_account_number, generate_pin
from termcolor import cprint
import sqlite3
from collections import namedtuple


class Bank:
    Account = namedtuple('Account', 'id, card, pin, balance')
    __connection = sqlite3.connect('card.s3db')
    __cursor = __connection.cursor()

    def __init__(self):
        self.sql = self.__cursor.executescript('''CREATE TABLE IF NOT EXISTS CARD(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT NOT NULL,
        pin_code TEXT NOT NULL,
        balance INTEGER NOT NULL DEFAULT 0
        )''')
        self.__connection.commit()
        self.main_menu()

    def main_menu(self):
        options = {'1': 'Create an account', '2': 'Log into account', '0': 'Exit'}
        actions = {'1': self.new_account, '2': self.log_in, '0': self.exit}
        for i in options:
            print(f"{i}: {options.get(i)}", sep="\n")
        try:
            user_choice = input('> ')
            actions[user_choice]()
        except KeyError:
            cprint("This option does not exist.\nPlease try again", "red")
        return self.main_menu()

    def new_account(self):
        cprint("\n Your card has been created", 'green')
        accounts = self.get_all_accounts()
        while True:
            new_number = generate_account_number()
            card = generate_card_number(new_number)
            if card not in accounts.keys():
                break
        pin_code = generate_pin()
        print("\nYour card number:", card, "Your card PIN:", pin_code, sep="\n")
        self.__cursor.execute(f'''INSERT INTO CARD(number, pin_code) VALUES ({card}, {pin_code})''')
        self.__connection.commit()

    @staticmethod
    def get_all_accounts():
        accounts = {}
        for acc in accounts:
            accounts[acc.card] = acc.pin_code
        return accounts

    def log_in(self):
        self.__cursor.execute('''SELECT * from CARD''')
        result = self.__cursor.fetchall()
        print(result)
        try:
            print("Enter your card number:")
            card_number = int(input("> "))
            print("Enter your PIN:")
            pin_code = int(input())
            account = self.get_account(card_number, pin_code)
            if account:
                account = Account(account)
                cprint("\n You have successfully logged in!", "green")
                account.account_menu()
                return
            cprint("\n Wrong card number or PIN!", "red")
        except ValueError:
            cprint("\n Wrong card number or PIN!", "red")

    def get_account(self, account_number, pin_code):
        self.__cursor.execute(f'''SELECT * FROM CARD WHERE NUMBER = {account_number} AND pin_code = {pin_code}''')
        f = self.__cursor.fetchone()
        return self.Account._make(f) if f else None

    def exit(self):
        print("\nBye!")
        self.__connection.close()
        exit()


def main():
    bank = Bank()
    bank.main_menu()


if __name__ == '__main__':
    main()
