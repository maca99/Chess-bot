import chess

from Heuristics.heuristic import Heuristic


class SecondChessHeuristic(Heuristic):

    def evaluate(self, state):
        white = black = 0
        value = {chess.KING: 7, chess.QUEEN: 23, chess.ROOK: 15, chess.BISHOP: 9, chess.KNIGHT: 9, chess.PAWN: 2}
        pieces = state.piece_map().values()
        for piece in pieces:
            if piece.color == chess.BLACK:
                black += value[piece.piece_type]
            else:
                white += value[piece.piece_type]
            if state.turn == chess.WHITE:
                if state.is_check():
                    if state.is_checkmate():
                        return 9999
                    else:
                        return 9999
                else:
                    return white - black
            else:
                if state.is_check():
                    if state.is_checkmate():
                        return -9999
                    else:
                        return -9999
                else:
                    return black - white
