from Games.game import Game
from Games.boardTiles import Board


class Tiles(Game):
    def __init__(self,complexity):
        self.board = Board(complexity)
        self.check_solvable(complexity)

    def check_solvable(self,complexity):
        while not self.board.is_solvable():
            self.board = Board(complexity)

    def solvate(self):
        return self.board.is_solvable()

    def get_goal_state(self):
        return self.board.get_goal_state()

    def get_board(self):
        return self.board

    def reset_game(self):
        size = self.board.get_size()
        self.board = Board(size)
        self.check_solvable(size)