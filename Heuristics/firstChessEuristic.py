import chess

from Heuristics.heuristic import Heuristic


class FirstChessHeuristic(Heuristic):

    def evaluate(self, state):
        white = black = 0
        value = {chess.KING: 100, chess.QUEEN: 9, chess.ROOK: 5, chess.BISHOP: 3, chess.KNIGHT: 3, chess.PAWN: 1}
        pieces = state.piece_map().values()
        for piece in pieces:
            if piece.color == chess.BLACK:
                black += value[piece.piece_type]
            else:
                white += value[piece.piece_type]
            if state.turn == chess.WHITE:
                if state.is_check():
                    if state.is_checkmate():
                        return 99999
                    else:
                        return 99999
                else:
                    return white - black
            else:
                if state.is_check():
                    if state.is_checkmate():
                        return -99999
                    else:
                        return -99999
                else:
                    return black - white
