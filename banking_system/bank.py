from account import Account


class Bank:
    def __init__(self):
        pass

    def main_menu(self):
        options = {1: 'Create an account', 2: 'Log into account', 0: 'Exit'}
        actions = {1: self.new_account, 2: self.log_in, 0: exit}
        for i in options:
            print(f"{i}: {options.get(i)}", sep="\n")
        user_choice = int(input('> '))
        if user_choice not in options.keys():
            print("This option does not exist.\nPlease try again")
        else:
            actions[user_choice]()
        return self.main_menu()

    def new_account(self):
        print("\nYour card has been created")

    def log_in(self):
        print("Enter your card number:")
        card_number = input("> ")
        if card_number.isdigit():
            print("Enter your PIN:")
            pin_code = input(">").strip()
            if pin_code.isdigit():
                print("You have successfully logged in!")
                account = Account()
                account.account_menu()
                return
        print("Wrong card number or PIN!")


def main():
    bank = Bank()
    bank.main_menu()


if __name__ == '__main__':
    main()