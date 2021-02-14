"""
pirple/python/hw6/main.py
Homework Assignment #6

Create a functipn that takes rows and columns as inputs,
 and draws a rows x columns sized playing board
"""

def draw_gameboard(rows, columns):
    if rows != int(rows) or columns != int(columns) or rows <= 0 or columns <= 0:
        print('Your rows and columns inputs must be positive integers')
        return False
    else:
        print('Generating a {}x{} gameboard . . .'.format(rows, columns))
        for r in range(rows):
            for c in range(columns):
                if c != (columns - 1):
                    print(' |', end='')
                else:
                    print()

            if r != (rows - 1):
                print('-' * (columns*2 - 1))

        print()
        return True

def generate_gameboard(rows, columns):

    if not draw_gameboard(rows, columns):
        print('Your gameboard will not be generated!')
        print()
        return False
    else:
        return True


generate_gameboard(2, 3)
generate_gameboard(7.5, 10)
generate_gameboard(7, 10)
generate_gameboard(-8, 5)
generate_gameboard(8, 5)
