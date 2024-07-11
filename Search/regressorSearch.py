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
            best_move = None
            max_eval = float('-inf')  # Inizializza max_eval con il valore negativo infinito
            neighbours = random.sample(list(state.legal_moves), len(list(state.legal_moves)))

            for neighbour in neighbours:
                state.push(neighbour)
                evaluation = self.minimax(state, neighbour, depth - 1, alpha, beta, not turn)[0]
                state.pop()

                if evaluation >= beta:
                    break

                alpha = max(alpha, max_eval)

            return [max_eval, best_move]
        else:
            best_move = None
            min_eval = float('inf')
            neighbours = random.sample(list(state.legal_moves), len(list(state.legal_moves)))

            for neighbour in neighbours:
                state.push(neighbour)
                evaluation = self.minimax(state, neighbour, depth - 1, alpha, beta, not turn)[0]
                state.pop()

                if evaluation <= alpha:
                    break

                beta = min(beta, min_eval)

            return [min_eval, best_move]



    def search(self, state, depth):
        self.count = 0
        all_moves = []
        k = 3;
        neighbours = random.sample(list(state.legal_moves), len(list(state.legal_moves)))
        for neighbour in neighbours:
            state.push(neighbour)
            evaluation = self.heuristic.evaluate(state)
            state.pop()
            all_moves.append((evaluation,neighbour))

        sorted_moves = sorted(all_moves, key=lambda x: x[0], reverse=True)[:k]
        list_of_moves = []

        for move in sorted_moves:
            state.push(move[1])
            list_of_moves.append((self.minimax(state,move[1],depth-1, float('-inf'), float('inf'), False)[0], move[1]))
            state.pop()

        return max(list_of_moves, key=lambda x: x[0])