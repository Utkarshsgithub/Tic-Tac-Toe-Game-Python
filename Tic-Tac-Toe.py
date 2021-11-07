# FUNCTIONS - display board | play game | check_if_game_over | check_for_winner | check_rows | check_columns |
# check_diagonals | check_tie | handle_turn | switch_player

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

game_still_going = True

winner = 'X'

current_player = 'X'


def display_board():

    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def play_game():

    global winner

    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        switch_player()

    if winner != None:
        print(f'{winner} WON (0_o)')

    elif winner == None:
        print(f'TIE (-_-)')


def check_if_game_over():

    check_for_winner()

    check_tie()


def check_for_winner():

    global winner

    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None

    return


def check_rows():

    global game_still_going

    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1 or row_2 or row_2:
        game_still_going = False

    if row_1:
        return board[0]

    elif row_2:
        return board[3]

    elif row_3:
        return board[6]

    return


def check_columns():

    global winner

    global game_still_going

    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    if column_1 or column_2 or column_2:
        game_still_going = False

    if column_1:

        return board[0]

    elif column_2:

        return board[1]

    elif column_3:

        return board[2]


def check_diagonals():

    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[6] == board[4] == board[2] != '-'

    if diagonal_1 or diagonal_2 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0]

    elif diagonal_2:
        return board[6]

    return


def check_tie():

    global game_still_going

    if '-' not in board:
        game_still_going = False

    return


def handle_turn(player):

    print(player+"'s turn")

    position = (input('Choose a position from 1-9: '))

    valid = False

    while not valid:

        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:

            position = (input('Choose a position from 1-9: '))

        position = int(position) - 1

        if board[position] == '-':

            valid = True

        else:
            print('You can"t go there! Go Again.')

    board[position] = player

    display_board()


def switch_player():

    global current_player

    if current_player == 'X':
        current_player = 'O'

    elif current_player == 'O':
        current_player = 'X'

    return


play_game()
