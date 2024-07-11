from Search.search import SearchAlgorithm
import random

from Heuristics.heuristic import Heuristic


class Minimax(SearchAlgorithm):

    def __init__(self, heuristic: Heuristic):
        self.heuristic = heuristic
        self.count = 0

    def minimax(self, state, move, depth, alpha, beta, turn):
        self.count = self.count + 1
        if depth == 0:
            return self.heuristic.evaluate(state), move
        if turn:
            max_eval = -999999
            best_move = None
            neighbours = random.sample(list(state.legal_moves), len(list(state.legal_moves)))
            for neighbour in neighbours:
                state.push(neighbour)
                evaluation = self.minimax(state, neighbour, depth - 1, alpha, beta, False)[0]
                state.pop()
                max_eval = max(max_eval, evaluation)
                if evaluation >= beta:
                    break
                if max_eval == evaluation:
                    best_move = neighbour
                alpha = max(alpha, max_eval)
            return [max_eval, best_move]
        else:
            min_eval = 999999
            best_move = None
            neighbours = random.sample(list(state.legal_moves), len(list(state.legal_moves)))
            for neighbour in neighbours:
                state.push(neighbour)
                evaluation = self.minimax(state, neighbour, depth - 1, alpha, beta, not turn)[0]
                state.pop()
                min_eval = min(min_eval, evaluation)
                if evaluation <= alpha:
                    break
                if min_eval == evaluation:
                    best_move = neighbour
                beta = min(beta, min_eval)
            return [min_eval, best_move]

    def search(self, state, depth):
        self.count = 0
        result = self.minimax(state, None, depth, float('-inf'), float('inf'), True)
        print(self.count)
        return result

