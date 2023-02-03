black_pawn = 'b'
black_king = 'B'
open_space = 'o'
white_pawn = 'w'
white_king = 'W'

board = [['8', open_space, white_pawn, open_space, white_pawn, open_space, white_pawn, open_space, white_pawn],
         ['7', white_pawn, open_space, white_pawn, open_space, white_pawn, open_space, white_pawn, open_space],
         ['6', open_space, white_pawn, open_space, white_pawn, open_space, white_pawn, open_space, white_pawn],
         ['5', open_space, open_space, open_space, open_space, open_space, open_space, open_space, open_space],
         ['4', open_space, open_space, open_space, open_space, open_space, open_space, open_space, open_space],
         ['3', black_pawn, open_space, black_pawn, open_space, black_pawn, open_space, black_pawn, open_space],
         ['2', open_space, black_pawn, open_space, black_pawn, open_space, black_pawn, open_space, black_pawn],
         ['1', black_pawn, open_space, black_pawn, open_space, black_pawn, open_space, black_pawn, open_space],
         [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ]
         ]

x_coord_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
y_coord_dict = {'8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}
# white starts
White_Turn = True


def show_board():
    for x in range(len(board)):
        print()
        for y in range(len(board[x])):
            print(board[x][y], end=' ')
    print()

# def show_board():
#     for x in range(len(board)):
#         print(board[x])


def black_on_board():
    for x in range(len(board) - 1):
        for y in range(len(board[x])):
            if board[x][y] == black_pawn or board[x][y] == black_king:
                print('black on board')
                return True
    return False


def white_on_board():
    for x in range(len(board) - 1):
        for y in range(len(board[x])):
            if board[x][y] == white_pawn or board[x][y] == white_king:
                print('white on board')
                return True
    return False


def check_movable_w(x, y):
    print('check movable white', x, y, board[y][x])
    if y == 8:
        if board[y - 1][x - 1] == open_space:
            return True
    elif y == 1:
        if board[y - 1][x + 1] == open_space:
            return True
    elif board[y - 1][x - 1] == open_space or board[y - 1][x + 1] == open_space:
        return True

    # check jump move white
    if x == 1 or x == 2:
        if (board[y - 1][x + 1] == black_pawn or board[y - 1][x + 1] == black_king) and board[y - 2][x + 2] == open_space:
            return True
    elif x == 7 or x == 8:
        if (board[y - 1][x - 1] == black_pawn or board[y - 1][x - 1] == black_king) and board[y - 2][x - 2] == open_space:
            return True
    elif (board[y - 1][x - 1] == black_pawn or board[y - 1][x - 1] == black_king) and board[y - 2][x - 2] == open_space:
        return True
    elif (board[y - 1][x + 1] == black_pawn or board[y - 1][x + 1] == black_king) and board[y - 2][x + 2] == open_space:
        return True
    else:
        print("not movable", x, y)
        return False


def check_movable_W(x, y):
    print('check movable WHITE', x, y, board[y][x])
    if x == 8:
        if board[y + 1][x - 1] == open_space:
            return True
    elif x == 1:
        if board[y + 1][x + 1] == open_space:
            return True
    elif board[y + 1][x + 1] == open_space or board[y + 1][x - 1] == open_space:
        return True

    # check jump move
    if x == 1 or x == 2:
        if (board[y + 1][x + 1] == black_pawn or board[y + 1][x + 1] == black_king) and board[y + 2][x + 2] == open_space:
            return True
    elif x == 7 or x == 8:
        if (board[y + 1][x - 1] == black_pawn or board[y + 1][x - 1] == black_king) and board[y + 2][x - 2] == open_space:
            return True
    elif (board[y + 1][x - 1] == black_pawn or board[y + 1][x - 1] == black_king) and (board[y + 2][x - 2] == open_space):
        return True
    elif (board[y + 1][x + 1] == black_pawn or board[y + 1][x + 1] == black_king) and board[y + 2][x + 2] == open_space:
        return True
    else:
        print("not movable", x, y)
        return False


def check_movable_b(x, y):
    print('check movable black', x, y, board[y][x])
    if x == 8:
        if board[y + 1][x - 1] == open_space:
            return True
    elif x == 1 and board[y + 1][x + 1] == open_space:
        return True
    elif board[y + 1][x + 1] == open_space or board[y + 1][x - 1] == open_space:
        return True

    # check jump move
    if x == 1 or x == 2:
        if (board[y + 1][x + 1] == white_pawn or board[y + 1][x + 1] == white_king) and board[y + 2][x + 2] == open_space:
            return True
    elif x == 7 or x == 8:
        if (board[y + 1][x - 1] == white_pawn or board[y + 1][x - 1] == white_king) and board[y + 2][x - 2] == open_space:
            return True
    elif (board[y + 1][x - 1] == white_pawn or board[y + 1][x - 1] == white_king) and (board[y + 2][x - 2] == open_space):
        return True
    elif (board[y + 1][x + 1] == white_pawn or board[y + 1][x + 1] == white_king) and board[y + 2][x + 2] == open_space:
        return True
    else:
        print("not movable", x, y)
        return False


def check_movable_B(x, y):
    print('check movable BLACK', x, y, board[y][x])
    if y == 8:
        if board[y - 1][x - 1] == open_space:
            return True
    elif y == 1:
        if board[y - 1][x + 1] == open_space:
            return True
    elif board[y - 1][x - 1] == open_space or board[y - 1][x + 1] == open_space:
        return True

    # print('check jump move white')
    if x == 1 or x == 2:
        if (board[y - 1][x + 1] == white_pawn or board[y - 1][x + 1] == white_king) and board[y - 2][x + 2] == open_space:
            return True
    elif x == 7 or x == 8:
        if (board[y - 1][x - 1] == white_pawn or board[y - 1][x - 1] == white_king) and board[y - 2][x - 2] == open_space:
            return True
    elif (board[y - 1][x - 1] == white_pawn or board[y - 1][x - 1] == white_king) and board[y - 2][x - 2] == open_space:
        return True
    elif (board[y - 1][x + 1] == white_pawn or board[y - 1][x + 1] == white_king) and board[y - 2][x + 2] == open_space:
        return True
    else:
        print("not movable", x, y)
        return False


def check_move_w(x1, y1, x2, y2):
    print("validating white's move. . .", x1, y1, ' - ', x2, y2)
    moved_x = (list(x_coord_dict.keys())[list(x_coord_dict.values()).index(x2)])
    moved_y = (list(y_coord_dict.keys())[list(y_coord_dict.values()).index(y2)])
    if board[y_coord_dict[moved_y]][x_coord_dict[moved_x]] == open_space:
        print('****', moved_x, moved_y)
        if board[y1][x1] == white_pawn or board[y1][x1] == black_king:
            print("it's a white pawn")
            if y1 - y2 == 1 and abs(x1 - x2) == 1:
                print('moved 1 space')
                return True
            elif y1 - y2 == 2 and abs(x1 - x2) == 2:
                print('moved 2 spaces')
                if x1 < x2:
                    board[y2+1][x2-1] = open_space
                else:
                    board[y2+1][x2+1] = open_space
                return True
            else:
                return False
        elif board[y1][x1] == white_king:
            print("it's a white king")
            if abs[y1 - y2] == 1:
                print("moved 1 space")
                return True
            elif abs(y1 - y2) == 2:
                print('moved 2 spaces')
                if x1 < x2:
                    board[y2 + 1][x2 - 1] = open_space
                else:
                    board[y2 + 1][x2 + 1] = open_space
                return True
            else:
                return False
        else:
            return False


def check_move_b(x1, y1, x2, y2):
    print("validating black's move. . .", x1, y1, ' - ', x2, y2)
    moved_x = (list(x_coord_dict.keys())[list(x_coord_dict.values()).index(x2)])
    moved_y = (list(y_coord_dict.keys())[list(y_coord_dict.values()).index(y2)])
    if board[y_coord_dict[moved_y]][x_coord_dict[moved_x]] == open_space:
        print('****', moved_x, moved_y)
        if board[y1][x1] == black_pawn or board[y1][x1] == white_king:
            print("it's a black pawn")
            if y2 - y1 == 1 and abs(x2 - x1) == 1:
                print('moved 1 space')
                return True
            elif y2 - y1 == 2 and abs(x2 - x1) == 2:
                print('moved 2 spaces')
                if x1 < x2:
                    board[y2 - 1][x2 - 1] = open_space
                else:
                    board[y2 - 1][x2 + 1] = open_space
                return True
            else:
                return False
        elif board[y1][x1] == black_king:
            print("it's a black king")
            if abs[y2 - y1] == 1:
                print("moved 1 space")
                return True
            elif abs(y2 - y1) == 2:
                print('moved 2 spaces')
                if x1 < x2:
                    board[y2 + 1][x2 - 1] = open_space
                else:
                    board[y2 + 1][x2 + 1] = open_space
                return True
            else:
                return False
        else:
            return False


def check_move_W(x1, y1, x2, y2):
    print("validating WHITE'S move. . .", x1, y1, ' - ', x2, y2)
    moved_x = (list(x_coord_dict.keys())[list(x_coord_dict.values()).index(x2)])
    moved_y = (list(y_coord_dict.keys())[list(y_coord_dict.values()).index(y2)])
    if board[y_coord_dict[moved_y]][x_coord_dict[moved_x]] == open_space:
        print('****', moved_x, moved_y)
        if board[y1][x1] == white_king:
            print("it's a white king")
            if abs(y2 - y1) == 1 and abs(x2 - x1) == 1:
                print('moved 1 space')
                return True
            elif abs(y2 - y1) == 2 and abs(x2 - x1) == 2:
                print('moved 2 spaces')
                if x1 < x2 and y1 < y2:
                    board[y2 - 1][x2 - 1] = open_space
                elif x1 > x2 and y1 < y2:
                    board[y2 - 1][x2 + 1] = open_space
                elif x1 < x2 and y1 > y2:
                    board[y2 + 1][x2 - 1] = open_space
                else:
                    board[y2 + 1][x2 + 1] = open_space
                return True
            else:
                return False


def check_move_B(x1, y1, x2,y2):
    print("validating BLACK'S move. . .", x1, y1, ' - ', x2, y2)
    moved_x = (list(x_coord_dict.keys())[list(x_coord_dict.values()).index(x2)])
    moved_y = (list(y_coord_dict.keys())[list(y_coord_dict.values()).index(y2)])
    if board[y_coord_dict[moved_y]][x_coord_dict[moved_x]] == open_space:
        print('****', moved_x, moved_y)
        if board[y1][x1] == black_king:
            print("it's a black king")
            if abs(y2 - y1) == 1 and abs(x2 - x1) == 1:
                print('moved 1 space')
                return True
            elif abs(y2 - y1) == 2 and abs(x2 - x1) == 2:
                print('moved 2 spaces')
                if x1 < x2 and y1 < y2:
                    board[y2 - 1][x2 - 1] = open_space
                elif x1 > x2 and y1 < y2:
                    board[y2 - 1][x2 + 1] = open_space
                elif x1 < x2 and y1 > y2:
                    board[y2 + 1][x2 - 1] = open_space
                else:
                    board[y2 + 1][x2 + 1] = open_space
                return True
            else:
                return False

def validate_first_input(piece):
    print("validating first input", piece)
    while True:
        try:
            user_input = piece.split(',')
            # check if input is a coordinate set
            if user_input[0] in x_coord_dict and user_input[1] in y_coord_dict:
                x, y = x_coord_dict[user_input[0]], y_coord_dict[user_input[1]]  # smaller var names

                if White_Turn:
                    print('it\'s white\'s turn')
                    if board[y][x] == white_pawn:
                        if check_movable_w(x, y):
                            return x, y
                        else:
                            print("This piece can't move")
                            return
                    elif board[y][x] == white_king:
                        if check_movable_W(x, y) or check_movable_w(x, y):
                            return x, y
                    elif board[y][x] == open_space:
                        print("There's no piece here!")
                        return
                    else:
                        print("This isn't your piece!White")
                        return
                if not White_Turn:
                    print('its blacks turn')
                    if board[y][x] == black_pawn:
                        if check_movable_b(x, y):
                            return x, y
                        else:
                            print("This piece can't move")
                            return
                    elif board[y][x] == black_king:
                        if check_movable_B(x, y) or check_movable_b(x, y):
                            return x, y
                    elif board[y][x] == open_space:
                        print("There's no piece here!")
                        return
                    else:
                        print("This isn't your piece!Black")
                        return

            else:
                print("else: Type the row and column of the piece you want to move separated by a comma (X,Y)")
                return
        except IndexError:
            print("error: Type the row and column of the piece you want to move separated by a comma (X,Y)")
            break


def validate_second_input(open_spot, x, y):
    print("validating second input", x, y, board[y][x])
    while True:
        try:
            user_input = open_spot.split(',')
            # check input vs proper coords
            if user_input[0] in x_coord_dict and user_input[1] in y_coord_dict:
                x_move, y_move = x_coord_dict[user_input[0]], y_coord_dict[user_input[1]]
                print("check second input", x_move, y_move, board[y_move][x_move])
                # must pick empty spot
                if board[y_move][x_move] == open_space:
                    if White_Turn:
                        if board[y][x] == white_pawn:
                            if check_move_w(x, y, x_move, y_move):
                                return x_move, y_move
                            else:
                                print("Can't move there. Try again.")
                                return False
                        elif board[y][x] == white_king:
                            if check_move_W(x, y, x_move, y_move):
                                return x_move, y_move
                        else:
                            print("can't move there")
                            return False
                    elif not White_Turn:
                        if board[y][x] == black_pawn:
                            if check_move_b(x, y, x_move, y_move):
                                return x_move, y_move
                            else:
                                return False
                        elif board[y][x] == black_king:
                            if check_move_B(x, y, x_move, y_move):
                                return x_move, y_move
                        else:
                            print("can't move there")
                            return False
                    else:
                        return False
                else:
                    print("Pick an empty spot.")
                    raise IndexError
            else:
                print("Try again.")
                return
        except IndexError:
            print("Type the row and column.")
            break


def check_for_kings():
    print('checking for kings - ')
    for i in range(len(board[0])):
        # print(board[0][i])
        if board[0][i] == white_pawn:
            board[0][i] = white_king
    for i in range(len(board[7])):
        if board[7][i] == black_pawn:
            board[7][i] = black_king


def move_piece(x1, y1, x2, y2):
    board[y1][x1], board[y2][x2] = board[y2][x2], board[y1][x1]


while black_on_board() and white_on_board():
    if White_Turn:
        print("IT'S WHITE'S TURN")
    else:
        print("IT'S BLACK'S TURN")
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
    check_for_kings()
    if White_Turn:
        White_Turn = False
    else:
        White_Turn = True

if white_on_board():
    print(""" 
              **************
              * WHITE WINS *
              **************  """)
    show_board()
else:
    print("""
              **************
              * BLACK WINS *
              **************  """)
    show_board()