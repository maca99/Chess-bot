from sklearn.base import BaseEstimator, TransformerMixin

class FENEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
def fen_to_numeric(fen):
    pieces_mapping = {'r': 4, 'n': 2, 'b': 3, 'q': 5, 'k': 6, 'p': 1,
                      'R': -4, 'N': -2, 'B': -3, 'Q': -5, 'K': -6, 'P': -1}

    try:
        # Divide il FEN nelle sue componenti
        fen_parts = fen.split()

        # Verifica che ci siano almeno due parti
        if len(fen_parts) < 2:
            return None  # o un valore di default a tua scelta

        # Codifica delle disposizioni dei pezzi sulla scacchiera
        board = []
        for row in fen_parts[0].split('/'):
            for char in row:
                if char.isdigit():
                    board.extend([0] * int(char))  # aggiunge il numero corretto di spazi vuoti
                else:
                    board.append(pieces_mapping.get(char, 0))

        # Codifica del lato di chi muove
        side_to_move = 0 if fen_parts[1] == 'w' else 1

        # Concatenazione di tutti i valori
        numeric_representation = board + [side_to_move]

        return numeric_representation
    except Exception as e:
        print(f"Errore nella conversione di {fen}: {e}")
        return None  # o un valore di default a tua scelta
