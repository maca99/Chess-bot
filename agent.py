from Games.game import Game
from Search.search import SearchAlgorithm


class Agent:
    def __init__(self, game: Game, algorithm: SearchAlgorithm, depth):
        self.game: Game = game
        self.algorithm: SearchAlgorithm = algorithm
        self.depth = depth

    def play(self, state):
        return self.algorithm.search(state, self.depth)
