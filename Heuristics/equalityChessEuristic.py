import chess

from Heuristics.heuristic import Heuristic


class EqualityChessHeuristic(Heuristic):

    def evaluate(self, state):
        white = black = 0
        value = {chess.KING: 1, chess.QUEEN: 1, chess.ROOK: 1, chess.BISHOP: 1, chess.KNIGHT: 1, chess.PAWN: 1}
        pieces = state.piece_map().values()
        for piece in pieces:
            if piece.color == chess.BLACK:
                black += value[piece.piece_type]
            else:
                white += value[piece.piece_type]
        return black - white