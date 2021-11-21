"""Player module"""


class Player:
    """Manages all player-related functionality"""
    name = None
    token = None

    def __init__(self, token):
        self.name = self.ask_names()
        self.token = token

    def ask_names(self):
        """ask names"""
        self.name = input('Please, enter your name: ')
        if self.name == '':
            self.name = 'Mystery player'
        return self.name

    def get_coordinates(self):
        """Gets where to put token from player"""
        coordinates = input(f'{self.name}, enter your coordinates: \n')
        if coordinates not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid input. Choose a position from 1-9: ")
            coordinates = input(f'{self.name}, enter your coordinates: \n')
        coordinates = int(coordinates) - 1
        return coordinates
