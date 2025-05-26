print("prajwal BR\nUSN:1AY24AI083\nSec:O")
def is_valid_chess_board(board):
    """
    Validate a chess board dictionary according to standard rules.
    
    Args:
        board: A dictionary with keys as positions (e.g., '1h') and values as pieces (e.g., 'wpawn')
    
    Returns:
        bool: True if valid, False otherwise
    """
    
    valid_positions = {f'{rank}{file}' for rank in '12345678' for file in 'abcdefgh'}
    
    valid_pieces = {
        'wking': 1, 'bking': 1,        
        'wqueen': 1, 'bqueen': 1,     
        'wrook': 2, 'brook': 2,        
        'wbishop': 2, 'bbishop': 2,    
        'wknight': 2, 'bknight': 2,
        'wpawn': 8, 'bpawn': 8         
    }
    
    for position in board.keys():
        if position not in valid_positions:
            return False
    
    piece_counts = {}
    for piece in board.values():
        if piece not in valid_pieces:
            return False
        piece_counts[piece] = piece_counts.get(piece, 0) + 1
    
    for piece, max_count in valid_pieces.items():
        if piece_counts.get(piece, 0) > max_count:
            if piece in ['wqueen', 'bqueen'] and piece_counts.get(piece, 0) <= (max_count + 8):
                continue
            return False
    
    if piece_counts.get('wking', 0) != 1 or piece_counts.get('bking', 0) != 1:
        return False
    
    for position, piece in board.items():
        rank = position[0]
        if 'pawn' in piece and rank in ('1', '8'):
            return False
    
    white_pieces = sum(count for piece, count in piece_counts.items() if piece.startswith('w'))
    black_pieces = sum(count for piece, count in piece_counts.items() if piece.startswith('b'))
    if white_pieces > 16 or black_pieces > 16:
        return False
    
    return True


if __name__ == "__main__":
    valid_board = {
        '1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wqueen',
        '1e': 'wking', '1f': 'wbishop', '1g': 'wknight', '1h': 'wrook',
        '2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn',
        '2e': 'wpawn', '2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn',
        '8a': 'brook', '8b': 'bknight', '8c': 'bbishop', '8d': 'bqueen',
        '8e': 'bking', '8f': 'bbishop', '8g': 'bknight', '8h': 'brook',
        '7a': 'bpawn', '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn',
        '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn', '7h': 'bpawn',
    }
    
    invalid_board = {
        '1a': 'wking', '2a': 'wking', 
        '8e': 'bking'
    }
    
    print("Valid board check:", is_valid_chess_board(valid_board))    
    print("Invalid board check:", is_valid_chess_board(invalid_board)) 
