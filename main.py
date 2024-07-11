import csv
from typing import List

import chess
import os
from Games.game_chess import ChessGame
from Heuristics import heuristic
from Heuristics.firstChessEuristic import FirstChessHeuristic
from Heuristics.regressorHeuristic import RegressorHeuristic
from Heuristics.secondChessEuristic import SecondChessHeuristic
from Heuristics.equalityChessEuristic import EqualityChessHeuristic
from Search.minimax import Minimax
from Search.minimaxHL import MinimaxHL
from Search.minimaxStatic import MinimaxStatic
from agent import Agent
from fen_to_numeric import fen_to_numeric
from regressor import get_regressor
from Heuristics.observations import *

def main():
    #create_dataset()
    regression = get_regressor()
    h1 = RegressorHeuristic(regression)
    h2 = FirstChessHeuristic()
    chess_test(h1,h2,3,5,10)

def create_dataset():
    depth_white = 3
    depth_black = 3
    size_test = 100
    game = ChessGame()
    hueristic1 = FirstChessHeuristic()
    hueristic2 = SecondChessHeuristic()
    minimax_black = Minimax(hueristic1)
    minimax_white = Minimax(hueristic2)
    agent1 = Agent(game, minimax_white, depth_white)
    agent2 = Agent(game, minimax_black, depth_black)

    agents: List[Agent] = []
    agents.append(agent1)
    agents.append(agent2)

    for _ in range(size_test):
        while not game.get_board().is_game_over():
            for agent in agents:
                if game.get_board().is_game_over():
                    break
                move = agent.play(game.get_board())
                hueristic1 = FirstChessHeuristic()
                h1,h2 = H1(game.get_board())[0],H1(game.get_board())[1]
                h3,h4 = H2(game.get_board())[0],H2(game.get_board())[1]
                h5,h6 = H3(game.get_board())[0],H3(game.get_board())[1]
                h7,h8 = H4(game.get_board())[0],H4(game.get_board())[1]
                h9,h10 = H5(game.get_board())[0],H5(game.get_board())[1]
                target = hueristic1.evaluate(game.get_board())
                write_position(h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,target)
                game.make_a_move(move)
        game.reset_game()

def write_position(h1:int,h2:int,h3:int,h4:int,h5:int,h6:int,h7:int,h8:int,h9:int,h10:int,target):
    filename = 'positions.csv'

    file_exists = os.path.isfile(filename)

     # Apri il file in modalità append (se non esiste, verrà creato)
    with open(filename, 'a', newline='') as csvfile:
        # Definisci i nomi delle colonne solo se il file non esiste
        fieldnames = [ 'H1', 'H2', 'H3', 'H4','H5','H6', 'H7', 'H8', 'H9', 'H10','target']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Se il file non esiste, scrivi l'intestazione
        if not file_exists:
            writer.writeheader()

        # Scrivi i dati passati al metodo
        writer.writerow({'H1': h1, 'H2': h2, 'H3': h3, 'H4':h4 , 'H5':h5,'H6':h6, 'H7':h7, 'H8':h8, 'H9':h9, 'H10':h10,'target':target})


def chess_test(heuristic_white, heuristic_black, depth_white, depth_black, size_test):
    game = ChessGame()
    minimax_white = MinimaxStatic(heuristic_white)
    minimax_black = MinimaxHL(heuristic_black)
    agent1 = Agent(game, minimax_white, depth_white)
    agent2 = Agent(game, minimax_black, depth_black)

    agents: List[Agent] = []
    agents.append(agent1)
    agents.append(agent2)

    white_winner = 0
    black_winner = 0
    for _ in range(size_test):
        while not game.get_board().is_game_over():
            for agent in agents:
                if game.get_board().is_game_over():
                    break
                move = agent.play(game.get_board())
                game.make_a_move(move)
        if game.get_the_winner() == chess.BLACK:
            black_winner += 1
        elif game.get_the_winner() == chess.WHITE:
            white_winner += 1
        game.reset_game()

    print('Vittorie Nero: ' + str((black_winner / size_test) * 100))
    print('Vittorie Bianco: ' + str((white_winner / size_test) * 100))
    print('Pareggi:' + str(((size_test - (black_winner + white_winner)) / size_test) * 100))
    print('__________________________________________________________')


main()