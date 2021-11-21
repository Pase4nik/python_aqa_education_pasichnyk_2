"""Tic Tac Toe main module"""

import logging
import sys
import time
from pathlib import Path
from board import Board
from player import Player


Path("logs").mkdir(parents=True, exist_ok=True)
FILENAME = 'logs/game_log.log'


def configure_logger():
    """Configure logger for terminal"""
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler(FILENAME)
    file_handler.setLevel(logging.WARNING)
    file_format = logging.Formatter('%(asctime)s %(message)s', "%d-%b-%Y %H:%M:%S")
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler(sys.stdout)

    stream_handler.setLevel(logging.WARNING)
    console_format = logging.Formatter('%(message)s')
    stream_handler.setFormatter(console_format)
    logger.addHandler(stream_handler)
    return logger


log = configure_logger()


def timer(func):
    """Decorator for counting game time and displaying it in logs"""
    def wrapper(*args_for_function):
        start = time.time()
        func(*args_for_function)
        end = time.time()
        total_time = (end - start)
        log.warning(f'Game duration time was: {total_time.__round__(2)}')

    return wrapper


class MainMenu:
    """Class with main menu options"""
    def __init__(self):
        self.main_menu()

    def main_menu(self):
        """Main menu method"""
        options = {'1': 'Play game', '2': 'Show Logs', '3': 'Clear Logs', '0': 'Exit'}
        actions = {'1': self.play_game, '2': self.show_logs, '3': self.clear_logs, '0': exit}
        for i in options:
            print(f"{i}: {options.get(i)}", sep="\n")
        try:
            user_choice = input('> ')
            actions[user_choice]()
        except KeyError:
            print("This option does not exist.\nPlease try again")
        return self.main_menu()

    @staticmethod
    def play_game():
        """Starting the game"""
        player_one = Player('X')
        player_two = Player('O')
        game = TicTacToe(player_one, player_two)
        game.game_process()

    @staticmethod
    def show_logs():
        """Showing logs"""
        try:
            with open(FILENAME, "r") as log_file:
                print(log_file.read())
        except OSError:
            log.critical('File not found')
        else:
            log_file.close()

    @staticmethod
    def clear_logs():
        """Clearing logs"""
        try:
            with open(FILENAME, "w") as log_file:
                log_file.truncate()
        except OSError:
            log.critical('File not found')
        else:
            log_file.close()


class TicTacToe:
    """Controls the game play"""
    def __init__(self, player_one, player_two):
        self.board = Board()
        self.player_one = player_one
        self.player_two = player_two
        self.current_player = self.player_one
        self.winner = None

    def game_process(self):
        """Full game process"""
        self.one_round()
        self.ask_again()

    @timer
    def one_round(self):
        """One round method"""
        self.board.create_board()
        while True:
            self.board.display_board()
            coordinates = self.current_player.get_coordinates()
            current_token = self.current_player.token
            if not self.board.add_token_to_board(coordinates, current_token):
                print("You can't go there!")
                self.flip_players()
            if self.check_game_over():
                break
            self.flip_players()
        if self.winner is not None:
            log.warning(f'{self.winner} wins')
        elif self.winner is None:
            log.warning(f'Draw between {self.player_one.name} and {self.player_two.name}')
        self.board.display_board()

    def ask_again(self):
        """Asking player about rematch"""
        ask_again = input("Wanna play again? (Enter 'yes' or 'no'):\n")
        if ask_again.lower() == 'yes':
            self.current_player = self.player_one
            self.board = Board()
            self.game_process()

    def check_game_over(self):
        """Check if it is a game over"""
        if self.board.check_if_win():
            self.winner = self.current_player.name
            return True
        elif self.board.check_if_tie():
            self.winner = None
            return True

    def flip_players(self):
        """Changing current player turn"""
        if self.current_player == self.player_one:
            self.current_player = self.player_two
        else:
            self.current_player = self.player_one


def main():
    """main method"""
    game = MainMenu()
    game.main_menu()


if __name__ == '__main__':
    main()
