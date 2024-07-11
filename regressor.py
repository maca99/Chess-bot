import pandas as pd
from sklearn.linear_model import LinearRegression


def get_regressor():
    # Carica il tuo set di dati
    data = pd.read_csv("positions.csv")

    # Combine the encoded positions with the other heuristic features
    X = data[['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10']]
    y = data['target']

    model = LinearRegression()
    # Addestra il modello
    model.fit(X, y)
    return model