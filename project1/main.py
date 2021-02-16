"""
pirple/python/project1/main.py
Project #1

Create a Connect 4 game
"""

def draw_board(board):
    print('_______________')
    print(' 1 2 3 4 5 6 7')
    for row in board:
        print('|', end='')
        for col in row:
            print(col + '|', end='')
        print()
    print('~~~~~~~~~~~~~~~')


def full_board(board):
    for r in range(6):
        for c in range(7):
            if board[r][c] == ' ':
                return False
    return True


def drop_marker(board, player, column):
    r = -1
    valid_move = True
    for row in board:
        if row[column] == ' ':
            marker_row = r + 1
            r += 1
        else:
            break

    if r == -1:
        print('Column {} is full. Choose a different column.'.format(column + 1))
        valid_move = False
    else:
        board[marker_row][column] = player

    return valid_move, board


def vertical_4(board, marker):
    for col in range(7):
        curr_row = 0
        last_row = -1
        continuous = 0
        for row in board:
            if row[col] == marker:
                if (last_row == -1) or (curr_row == (last_row + 1)):
                    last_row = curr_row
                    continuous += 1
                if continuous == 4:
                    return True
            curr_row += 1

    return False


def horizontal_4(board, marker):
    for row in board:
        curr_col = 0
        last_col = -1
        continuous = 0
        for col in range(7):
            if row[col] == marker:
                if (last_col == -1) or (curr_col == (last_col + 1)):
                    last_col = curr_col
                    continuous += 1
                if continuous == 4:
                    return True
            curr_col += 1

    return False


def diagonal_4(board, marker):
    for row in range(3):
        for col in range(7):
            if board[row][col] == marker:
                if check_diagonals(board, marker, row, col):
                    return True
    return False


def check_diagonals(board, marker, row, col):
    forward_diagonal = [[row, col]]
    backward_diagonal = [[row, col]]
    if col >= 3:
        for i in range(1, 4):
            forward_diagonal.append([row + i, col - i])

    if col <= 3:
        for i in range(1, 4):
            backward_diagonal.append([row + i, col + i])

    forward_count = 0
    backward_count = 0
    if len(forward_diagonal) == 4:
        for coords in forward_diagonal:
            if board[coords[0]][coords[1]] == marker:
                forward_count += 1

    if len(backward_diagonal) == 4:
        for coords in backward_diagonal:
            if board[coords[0]][coords[1]] == marker:
                backward_count += 1

    if (forward_count == 4) or (backward_count == 4):
        return True
    else:
        return False


def check_for_winner(board):
    winner = 'N'
    for marker in ['\u2606', '\u263E']:
        if vertical_4(board, marker) or horizontal_4(board, marker) or diagonal_4(board, marker):
            winner = marker
        elif full_board(board):
            winner = 'T'
    return winner


def exit_program(winner):
    if winner == 'N':
        print('Goodbye!')
        return 1
    elif winner == 'T':
        print('It\'s a tie!! Well played.')
    else:
        print('Nice win, player {}!!'.format(winner))

    yn = False
    while not yn:
        replay = input('Do you want to play again (y/n)? ')
        if replay.upper() not in ('Y', 'N'):
            print('You must enter a y or n.  Try again.')
        else:
            if replay.upper() == 'N':
                print('OK. Come back and play again soon.')
                return 1
            else:
                print('OK, let\'s play again!\n')
                return 0


def reset_game():
    return 0, 'N', '\u2606', 1, [[' '] * 7, [' '] * 7, [' '] * 7, [' '] * 7, [' '] * 7, [' '] * 7]


def main():
    print('Hi! Ready to play some Connect 4?  Let\'s go!!')
    print('\u2606 and \u263E are used as markers in this version.  \u2606 goes first.')
    print('Enter X at any time to exit the game.\n')

    done, winner, player, turn, board = reset_game()
    while not done:
        draw_board(board)
        choice = input('Player {}, into which column do you want to drop your marker? '.format(player))

        if choice.upper() == 'X':
            done = exit_program(winner)
        elif choice in ('1', '2', '3', '4', '5', '6', '7'):
            valid_move, board = drop_marker(board, player, int(choice) - 1)
            if not valid_move:
                done = 0
            else:
                winner = check_for_winner(board)
                if winner != 'N':
                    draw_board(board)
                    done = exit_program(winner)
                    if not done:
                        done, winner, player, turn, board = reset_game()
                else:
                    if turn%2 == 0:
                        player = '\u2606'
                    else:
                        player = '\u263E'
                    turn += 1
        else:
            print('You must enter an X to exit, or choose a column number 1-7.')
            print('Try again.\n')
            done = 0


main()

