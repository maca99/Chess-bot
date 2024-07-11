from abc import ABC


class Game(ABC):
    def __init__(self):
        pass

    def get_board(self):
        pass

    def make_a_move(self, move):
        pass

    def reset_game(self):
        pass