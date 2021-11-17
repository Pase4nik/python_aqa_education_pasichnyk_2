class Account:
    def __init__(self):
        self.balance = 0

    def account_menu(self):
        options = {1: 'Balance', 2: 'Log out', 0: 'Exit'}
        actions = {1: self.show_balance, 2: self.log_out, 0: exit}
        for i in options:
            print(f"{i}: {options.get(i)}", sep="\n")
        user_choice = int(input('> '))
        if user_choice not in options.keys():
            print("This option does not exist.\nPlease try again")
        else:
            actions[user_choice]()

    def show_balance(self):
        print('Balance:', self.balance)
        return self.account_menu()

    def log_out(self):
        print("You have successfully logged out!")