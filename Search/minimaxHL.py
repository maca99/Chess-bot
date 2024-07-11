from Search.search import SearchAlgorithm
import random

from Heuristics.heuristic import Heuristic


class MinimaxHL(SearchAlgorithm):

    def __init__(self, heuristic: Heuristic):
        self.count = 0
        self.heuristic = heuristic

    def minimax(self, state, move, depth, alpha, beta, turn):
        self.count = self.count + 1
        if depth == 0:
            return self.heuristic.evaluate(state), move , state
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
            return [max_eval, best_move,state]
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
            return [min_eval, best_move, state]

    def search(self, state, depth):
        self.count = 0
        all_moves = []
        i=1
        k=1
        neighbours = random.sample(list(state.legal_moves), len(list(state.legal_moves)))
        for neighbour in neighbours:
            state.push(neighbour)
            evaluation = self.minimax(state,None, i-1, float('-inf'), float('inf'), False)
            state.pop()
            if evaluation[1] is not None:
                all_moves.append((evaluation [0],evaluation[1], neighbour))

        if k <= len(all_moves):
            all_moves.sort(key=lambda x: x[0])
            sorted_moves = random.sample(all_moves, k)
        else:
            sorted_moves = all_moves

        list_of_moves = []

        for move in sorted_moves:
            state.push(move[1])
            list_of_moves.append(
                (self.minimax(state, None, depth - 1, float('-inf'), float('inf'), False)[0], move[1]))
            state.pop()

        print(self.count)
        if list_of_moves is  None:
            return max(list_of_moves, key=lambda x: x[0])
        else:
            return [-9999,None]