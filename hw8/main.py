"""
pirple/python/hw8/main.py
Homework Assignment #8

Create a note-taking program that allows you to do the following
 to files of notes:
    1) Create a new one
    2) Read one
    3) Replace one completely
    4) Append to one
    5) Replace a single line in one
"""

import os.path as path

def create_new_file(new_file):
    new_note = input('Enter the note you wish to save: ')
    with open('data/' + new_file, "w") as note_file:
        note_file.write(new_note + '\n')


def read_file(file_name, full_path):
    print('Current contents of file {}.:'.format(file_name))
    with open(full_path, 'r') as note_file:
        print(note_file.read(), end='')
    print('\b<END OF {}>\n'.format(file_name.upper()))


def replace_file(file_name):
    print('Replacing file {} completely with newly entered notes.'.format(file_name))
    create_new_file(file_name)
    print('File {} has been replaced with new notes\n'.format(file_name))


def append_file(file_name, full_path):
    print('Appending to file {}.'.format(file_name))
    new_note = input('Enter the note you wish to append: ')
    with open(full_path, 'a') as note_file:
        note_file.write(new_note + '\n')
    print('Note added to file {}\n'.format(file_name))


def replace_line(file_name, full_path):
    with open(full_path, 'r') as note_file:
        curr_notes = note_file.readlines()

        line_choice = int(input('Enter the line number you want to replace in file {}: '.format(file_name)))
        print('The current note on line {} of file {} is:'.format(str(line_choice), file_name))
        print(curr_notes[line_choice - 1])

        new_note = input('Enter the new note: ')
        curr_notes[line_choice - 1] = new_note + '\n'

    with open(full_path, 'w') as note_file:
        for note in curr_notes:
            note_file.write(note)
        print('New note replaced line {} in file {}\n'.format(line_choice, file_name))


def process_existing_file(file_name, full_path):
    print('File {} already exists'.format(file_name))

    exit_menu = False
    bad_choice = True
    while bad_choice:
        choice = input('Would you like to (1) Read the file\n'
                       '                  (2) Replace the file\n'
                       '                  (3) Add to the file\n'
                       '                  (4) Change a line in the file\n'
                       '                  (x) Exit\n?: ')

        if choice.upper() == 'X':
            exit_menu = True
            bad_choice = False
        elif choice not in ('1', '2', '3', '4'):
            print('Your choice needs to be 1-4 or x\n')
            bad_choice = True
        elif choice == '1':
            read_file(file_name, full_path)
            bad_choice = False
        elif choice == '2':
            replace_file(file_name)
            bad_choice = False
        elif choice == '3':
            append_file(file_name, full_path)
            bad_choice = False
        elif choice == '4':
            replace_line(file_name, full_path)
            bad_choice = False

        if not exit_menu and not bad_choice:
            correct_choice = False
            while not correct_choice:
                yn = input('Do you wish to process file {} further (y/n)? '.format(file_name))
                if yn.upper() not in ('Y', 'N'):
                    print('Please respond with with a y or n.')
                    correct_choice = False
                elif yn.upper() == 'Y':
                    correct_choice = True
                    bad_choice = True
                else:
                    correct_choice = True

    return exit_menu


def exit_program():
    print('Goodbye!')
    return 1


def main():
    done = 0
    while not done:
        choice = input('Enter the file you wish to work on, or an x to Exit: ')

        if choice.upper() == 'X':
            done = exit_program()
        elif path.isfile('data/' + choice):
            exit_menu = process_existing_file(choice, 'data/' + choice)
            if exit_menu:
                done = exit_program()
        else:
            print('Creating a new file named', choice)
            create_new_file(choice)
            print('File {} has been updated and saved!'.format(choice))
            print()
            done = exit_program()

main()