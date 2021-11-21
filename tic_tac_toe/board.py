"""Board module"""


class Board:
    """Maintains game board state"""
    def __init__(self):
        """initialize board"""
        self.board = []

    def create_board(self):
        """Creates empty board"""
        for i in range(0, 9):
            self.board.extend('-')
        return self.board

    def display_board(self):
        """Displays board in terminal"""
        print("""
         {} | {} | {}
        ---+---+---
         {} | {} | {}
        ---+---+---
         {} | {} | {}
        """.format(*self.board))

    def add_token_to_board(self, position, token):
        """Adding players token to the board 'X' or 'O'"""
        if self.board[position] != '-':
            return False
        else:
            self.board[position] = token
        return True

    def check_if_win(self):
        """Check winning combinations"""
        combs = [[0, 3, 6], [0, 1, 2], [0, 2]]
        for j in combs[0]:
            if self.check_rows(self.board[j:j+3]):
                return True
        for j in combs[1]:
            if self.check_columns(self.board[j:j+7:3]):
                return True
        for j in combs[2]:
            if self.check_diagonals(self.board[j:j+9:4]):
                return True

    @staticmethod
    def check_rows(row):
        """Checks rows"""
        if all([i == 'X' for i in row]) or all([i == 'O' for i in row]):
            return True

    @staticmethod
    def check_columns(column):
        """Checks columns"""
        if all([i == 'X' for i in column]) or all([i == 'O' for i in column]):
            return True
        return

    @staticmethod
    def check_diagonals(diagonal):
        """Check diagonals"""
        if all([i == 'X' for i in diagonal]) or all([i == 'O' for i in diagonal]):
            return True
        return

    def check_if_tie(self):
        """Check if tie"""
        if '-' not in self.board:
            return True
