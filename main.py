black_pawn = 'b'
black_king = 'B'
open_space = 'o'
white_pawn = 'w'
white_king = 'W'

board = [['8', black_pawn, open_space, black_pawn, open_space, black_pawn, open_space, black_pawn, open_space],
         ['7', open_space, black_pawn, open_space, black_pawn, open_space, black_pawn, open_space, black_pawn],
         ['6', black_pawn, open_space, black_pawn, open_space, black_pawn, open_space, black_pawn, open_space],
         ['5', open_space, open_space, open_space, open_space, open_space, open_space, open_space, open_space],
         ['4', open_space, open_space, open_space, open_space, open_space, open_space, open_space, open_space],
         ['3', open_space, white_pawn, open_space, white_pawn, open_space, white_pawn, open_space, white_pawn],
         ['2', white_pawn, open_space, white_pawn, open_space, white_pawn, open_space, white_pawn, open_space],
         ['1', open_space, white_pawn, open_space, white_pawn, open_space, white_pawn, open_space, white_pawn],
         [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ]
         ]

x_coord_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
y_coord_dict = {'8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}


def show_board():
    for x in range(len(board)):
        print(board[x])


def black_on_board():
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == black_pawn or black_king:
                return True


def white_on_board():
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == white_pawn or white_king:
                return True


def validate_first_input(piece):
    while True:
        try:
            user_input = piece.split(',')
            if user_input[0] in x_coord_dict and user_input[1] in y_coord_dict:
                x, y = x_coord_dict[user_input[0]],  y_coord_dict[user_input[1]]
                if board[y][x] != 'o':
                    return x, y
                else:
                    print("Pick spot with a piece on it.")
                    return
            else:
                print("Type the row and column of the piece you want to move separated by a comma (X,Y)")
                return
        except IndexError:
            print("Type the row and column of the piece you want to move separated by a comma (X,Y)")
            break

def validate_second_input(open_spot, x, y):
    while True:
        try:
            user_input = open_spot.split(',')
            if user_input[0] in x_coord_dict and user_input[1] in y_coord_dict:
                x, y = x_coord_dict[user_input[0]], y_coord_dict[user_input[1]]
                if board[y][x] == 'o':
                    return x, y
                else:
                    print("Pick an empty spot.")
                    raise IndexError
            else:
                print("Try again.")
                return
        except IndexError:
            print("Type the row and column.")
            break


def move_piece(x1, y1, x2, y2):
    board[y1][x1], board[y2][x2] = board[y2][x2], board[y1][x1]


while black_on_board() and white_on_board():
    show_board()
    declared_piece = input("Type the row and column of the piece you want to move: ")
    try:
        declared_piece_x, declared_piece_y = validate_first_input(declared_piece)
    except TypeError:
        continue
    declared_spot = input("Type the row and column of the open spot to move that piece: ")
    try:
        declared_spot_x, declared_spot_y = validate_second_input(declared_spot, declared_piece_x, declared_piece_y)
    except TypeError:
        continue
    move_piece(declared_piece_x, declared_piece_y, declared_spot_x, declared_spot_y)


