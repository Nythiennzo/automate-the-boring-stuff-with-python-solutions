def isValidChessBoard(chess_board_dict):
    try:
        pieces_count = {}
        for piece in ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king'):
            pieces_count['b' + piece] = 0
            pieces_count['w' + piece] = 0

        if chess_board_dict == {}:
            return False

        for key in chess_board_dict.keys():
            if len(key) != 2:
                return False
            if key[0] < 'a' or key[0] > 'h':
                return False
            if key[1] < '1' or key[1] > '8':
                return False

            piece = chess_board_dict[key]
            if piece not in pieces_count.keys():
                return False
            
            pieces_count[piece] += 1
            if piece in ('bpawn', 'wpawn'):
                if pieces_count[piece] > 8:
                    return False
            else:
               if pieces_count[piece] > 2:
                    return False 
        return True
    except:
        return False

#Warning this does not take all the rules of chess into consideration
print(isValidChessBoard({}))
print(isValidChessBoard(1))
print(isValidChessBoard('Test'))
print(isValidChessBoard({'a2':'bking'}))
print(isValidChessBoard({'a2':'bking', '--':'wking'}))
print(isValidChessBoard({'a2':'bking', 'a3':'wking'}))
print(isValidChessBoard({'a2':'bking', 'a3':'wrook', 'b8':'bqueen', 'g8':'bpawn'}))
print(isValidChessBoard({'a2':'bking', 'a3':'wrook', 'b8':'bqueen', 'g1':'bpawn', 'g2':'bpawn','g3':'bpawn','g4':'bpawn','g5':'bpawn','g6':'bpawn','g7':'bpawn','g8':'bpawn'}))
print(isValidChessBoard({'a2':'bking', 'a3':'wrook', 'b8':'bqueen', 'g1':'bpawn', 'g2':'bpawn','g3':'bpawn','g4':'bpawn','g5':'bpawn','g6':'bpawn','g7':'bpawn','g8':'bpawn', 'f1':'bpawn'}))