import chess
import numpy as np
import pandas as pd
from Heuristics.observations import *

from fen_to_numeric import fen_to_numeric

class RegressorHeuristic():

    def __init__(self,regressor):
        self.regression = regressor

    def evaluate(self, state: chess.Board):
        h1, h2 = H1(state)
        h3, h4 = H2(state)
        h5, h6 = H3(state)
        h7, h8 = H4(state)
        h9, h10 = H5(state)

        features = {'H1': h1, 'H2': h2, 'H3': h3, 'H4': h4, 'H5': h5, 'H6': h6, 'H7': h7, 'H8': h8, 'H9': h9, 'H10': h10}

        # Convert the list to a numpy array and reshape it to be 2D
        #features_array = np.array(features).reshape(1, -1)
        features_df = pd.DataFrame([features])

        # Make prediction
        prediction = self.regression.predict(features_df)
        return prediction
    