from Heuristics import heuristic
from Heuristics.heuristic import Heuristic
from Search.search import SearchAlgorithm



class AStarSearch(SearchAlgorithm):

    def __init__(self, start_state, final_state, heuristic: Heuristic):
        self.startState = start_state
        self.finalState = final_state
        self.heuristic = heuristic
        self.h = []
        self.explored = []

    def search(self, state, depth):
        self.h.append(self.startState)
        while self.h:
            state = self.pick()
            if state == self.finalState:
                return self.backpath(state)
            self.explored.append(state)
            self.h.extend([s for s in state.neighbours() if s not in self.explored and s not in self.h])
        return False

    def pick(self):
        el = min(self.h, key=lambda x: x.cost + self.heuristic.evaluate(x))
        self.h.remove(el)
        return el

    def backpath(self, state):
        path = []
        while state:
            path.append(state)
            state = state.parent
        path.reverse()
        return path