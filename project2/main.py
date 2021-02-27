"""
pirple/python/project2/main.py
Project #2

Create a hangman game
"""

from os import system, name
from time import sleep
from random import randint
import string


def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def reset_game():
    return False, 0, 'C'


def exit_program():
    print('Goodbye!')
    return True


def play_game(num_players):
    clear_screen()
    done, guesses_used, status = reset_game()

    while not done:
        secret_word, known_letters, guess_letters = set_secret_word(num_players)
        draw_board(guesses_used, known_letters, guess_letters)

        while(True):
            guesses_used, guess_letters, known_letters, status = take_a_guess(guesses_used, guess_letters, known_letters, secret_word)

            if status == 'C':
                draw_board(guesses_used, known_letters, guess_letters)
            else:
                break

        yn = input('Would you like to play again (y/n)? ')
        if yn.upper() == 'Y':
            clear_screen()
            done, guesses_used, status = reset_game()
        else:
            done = True


def set_secret_word(num_players):
    # The computer selects a word in the 1-player game
    if num_players == 1:
        secret_word = auto_select_secret_word()

    # Otherwise one of the players chooses a word
    else:
        secret_word = input_secret_word()

    blank_list = []
    for i in range(len(secret_word)):
        blank_list.append('_ ')

    return secret_word, blank_list, []


def auto_select_secret_word():
    r = randint(0, len(auto_word_list))
    auto_word = auto_word_list[r]
    print('OK, the computer has picked a word. Let\'s play!')
    sleep(1)
    return auto_word


def input_secret_word():
    print('Player 1 will choose a word for player 2 to guess.')
    print('When you have one chosen, ask player 2 to look away, and stay that way until you give the OK.')
    print('Ready?\n')

    while(True):
        input_word = input('Player 1, enter your word:\n').upper()

        yn = input('You have chosen {}. Is that correct (y/n)? '.format(input_word))
        if yn.upper() != 'Y':
            print('Oops! All right, try again.\n')
            continue
        else:
            print('OK, let\'s play!!')
            break

    return input_word


def draw_board(guesses_used, known_letters, guess_letters):
    gallows = [['  |````', '  |````|'],
               ['  |', '  |    |'], #1 guess
               ['  |', '  |    O'], #2
               ['  |', '  |   /', '  |   /|', '  |   /|\\'], #3, 4, 5
               ['  |', '  |    |'], #6
               ['  |', '  |   /', '  |   / \\'], # 7, 8
               ['  |'],
               ['`````']
              ]

    guess_codes = [[0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 1, 0, 0, 0, 0, 0, 0],
                   [1, 1, 1, 0, 0, 0, 0, 0],
                   [1, 1, 1, 1, 0, 0, 0, 0],
                   [1, 1, 1, 2, 0, 0, 0, 0],
                   [1, 1, 1, 3, 0, 0, 0, 0],
                   [1, 1, 1, 3, 1, 0, 0, 0],
                   [1, 1, 1, 3, 1, 1, 0, 0],
                   [1, 1, 1, 3, 1, 2, 0, 0]
                   ]

    clear_screen()
    print()
    for i in range(8):
        print(gallows[i][guess_codes[guesses_used][i]])

    for k in known_letters:
        print(k, end=' ')
    print('\n')

    if len(guess_letters) > 0:
        print('Letters already guessed:')
        for g in guess_letters:
            print(g, end=' ')
        print('\n')


def take_a_guess(guesses_used, guess_letters, known_letters, secret_word):

    while(True):
        letter = input('Player 2, guess a letter: ')
        if letter not in string.ascii_letters:
            print('You must enter a letter. Try again.')
        else:
            repeat = False
            for k in known_letters:
                if (letter.upper() in k):
                    repeat = True

            if repeat:
                print('You already guessed {}! Guess again.'.format(letter.upper()))
            else:
                break

    found = False
    for i in range(len(secret_word)):
        if letter.upper() == secret_word[i]:
            blank_to_correct = known_letters[i].maketrans('_', letter.upper())
            known_letters[i] = known_letters[i].translate(blank_to_correct)
            found = True

    if not found:
        guess_letters, guesses_used, status = wrong_guess(letter.upper(), guess_letters, guesses_used, known_letters, secret_word)
    else:
        status = correct_guess(letter.upper(), known_letters, guesses_used, guess_letters)

    return guesses_used, guess_letters, known_letters, status


def wrong_guess(letter, guess_letters, guesses_used, known_letters, secret_word):

    if letter in guess_letters:
        print('You already guessed {}! Guess again.'.format(letter))
    else:
        print('Sorry! There\'s no {} in the word.'.format(letter))
        guess_letters.append(letter)
        guess_letters = list(set(guess_letters))
        guess_letters.sort()
        guesses_used += 1

    sleep(1)

    if guesses_used == 8:
        draw_board(guesses_used, known_letters, guess_letters)
        print('Oh, no! You\'re hanged! The secret word was:')
        print(secret_word)
        status = 'L'
    else:
        status = 'C'

    return guess_letters, guesses_used, status


def correct_guess(letter, known_letters, guesses_used, guess_letters):
    status = 'W'
    for known in known_letters:
        if '_' in known:
            status = 'C'

    if status == 'W':
        draw_board(guesses_used, known_letters, guess_letters)
        print('You got it! Well done!')
        sleep(1)
    else:
        print('Good guess!'.format(letter))
        sleep(1)

    return status


def create_auto_word_list():
    auto_word_list = []
    word_file = open('/usr/share/dict/words', 'r')
    words = word_file.read()
    word_list = words.splitlines()
    for word in word_list:
        if (word[0] not in string.ascii_uppercase) and (len(word) >= 6):
            auto_word_list.append(word.upper())
    return auto_word_list


def main():
    global auto_word_list
    print('Hey, there! Wanna play some Hangman?')

    done = False
    while not done:
        choice = input('Tell me the number of players (1 or 2), or enter an X to exit the game: ')

        if choice.upper() == 'X':
            done = exit_program()
        elif choice in ('1', '2'):
            auto_word_list = create_auto_word_list()
            play_game(int(choice))
            done = exit_program()
        else:
            print('Enter a 1, 2 or X only. Try again')
            done = False

if __name__ == '__main__':
    main()
