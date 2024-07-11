import chess

from Games.game import Game


class ChessGame(Game):

    def __init__(self):
        self.board = chess.Board()

    def get_board(self):
        return self.board

    def make_a_move(self, move):
        move = move[1]
        if move is not None:
            self.board.push(move)

    def get_the_winner(self):
        if self.board.outcome().winner == chess.WHITE:
            return chess.WHITE
        elif self.board.outcome().winner == chess.BLACK:
            return chess.BLACK
        else:
            return "DRAW"

    def reset_game(self):
        self.board.reset()
