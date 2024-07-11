import chess
      
def H1(state:chess.Board):
    result = []
    white = black = 0
    pieces = state.piece_map().values()
    for piece in pieces:
        if piece.color == chess.BLACK and piece.piece_type == chess.PAWN:
            pos = find_piece_position(state,'p')
            if len(pos) > 1:
                if  pos[1] == 2:
                    black += 1  
                
        if piece.color == chess.WHITE and piece.piece_type == chess.PAWN:
            pos = find_piece_position(state,'p')
            if len(pos) > 1:
                if pos[1] == 7:
                    white += 1

    result.append(white)
    result.append(black)
    return result
    

def H2(state):
    result = []
    white = black = 0
    pieces = state.piece_map().values()
    for piece in pieces:
        if piece.color == chess.BLACK and piece.piece_type == chess.QUEEN:
            black = 1
        if piece.color == chess.WHITE and piece.piece_type == chess.QUEEN:
            white = 1

    result.append(white)
    result.append(black)
    return result
    
def H3(state):
    result = []
    white = black = 0
    pieces = state.piece_map().values()
    for piece in pieces:
        if piece.color == chess.BLACK and piece.piece_type == chess.BISHOP:
            black += 1
        if piece.color == chess.WHITE and piece.piece_type == chess.BISHOP:
            white += 1

    result.append(white)
    result.append(black)
    return result
    
def H4(state):
    result = []
    white = black = 0
    pieces = state.piece_map().values()
    for piece in pieces:
        if piece.color == chess.BLACK and piece.piece_type == chess.ROOK:
            black += 1
        if piece.color == chess.WHITE and piece.piece_type == chess.ROOK:
            white += 1
    
    result.append(white)
    result.append(black)
    return  result
    
def H5(state):
    result = []
    white = black = 0
    pieces = state.piece_map().values()
    for piece in pieces:
        if piece.color == chess.BLACK and piece.piece_type == chess.KNIGHT:
            black += 1
        if piece.color == chess.WHITE and piece.piece_type == chess.KNIGHT:
            white += 1
            
    result.append(white)
    result.append(black)
    return  result
        


def find_piece_position(board, piece_symbol):
    piece_positions = []
    for square in chess.SQUARES:
        if board.piece_at(square) and board.piece_at(square).symbol() == piece_symbol:
            piece_positions.append(chess.square_name(square))
    return piece_positions