"""
pirple/python/hw7/main.py
Homework Assignment #7

Create a dictionary for attributes of the song "American Pie",
 and use an interactive function to allow for them to be printed
 out or guessed
"""

song_dict = {
                "title": ["Song title", "American Pie"],
                "album": ["Album title", "American Pie"],
                "genre": ["Song music genre", "Folk Rock"],
                "artist": ["Song artist", "Don McLean"],
                "year_released": ["Year song was released", 1971],
                "writer": ["Song writer", "Don McLean"],
                "producer": ["Song producer", "Ed Freeman"],
                "label": ["Record label of the album", "United Artists"],
                "production_co": ["Production company", "The Rainbow Collection, Ltd."],
                "duration_minutes": ["Song duration in minutes", 8.51],
                "gold_record": ["Boolean flag indicating the song received a gold record", True],
                "platinum_record": ["Boolean flag indicating the song received a platinum record", True],
                "us_bb_hot100_high": ["Highest rank in the US Billboard Hot 100 chart", 3],
                "us_bb_hot100_all": ["All-time US Billboard Hot 100 chart rank", 210],
                "piano": ["Piano player", "Paul Griffin"],
                "vocals": ["Lead vocals", "Don McLean"],
                "backup_vocals": ["Backup vocals", "Bob Rothstein"],
                "chorus": ["Chorus", "West Forty-Fourth Street Rhythm and Noise Choir"],
                "acoustic_guitar": ["Acoustic guitar player", "Don McLean"],
                "electric_guitar": ["Electric guitar player", "David Spinozza"],
                "bass": ["Bass player", "Bob Rothstein"],
                "drums": ["Drum player", "Roy Markowitz"],
                "tambourine": ["Tambourine player", "Roy Markowitz"]
            }

def print_dict(dict):
    for k, v in dict.items():
        print(dict[k][0] + ':  ', end='')
        print(dict[k][1])
    print()

def guess_is_correct(key, guess):
    global song_dict
    if key in song_dict.keys():
        if str(song_dict[key][1]) == guess:
            return True
        else:
            print('Sorry! {} is not the {} of the song'.format(guess, song_dict[key][0]))
            print()
            return False
    else:
        print('Your key {} does not exist in the song dictionary'.format(key))
        print()
        return False

done = 0
while not done:
    bad_input = 0
    print('Would you like to: (1) guess an attribute of American Pie or (2) list all attributes?')
    while not bad_input:
        choice = input('Enter a 1, 2 or x to Exit: ')
        if choice not in ('1', '2', 'x'):
            print('You must enter a 1, 2 or x. Please try again.')
        else:
            bad_input = 1

    if choice == 'x':
        print('Goodbye!')
        done = 1
    elif choice == '2':
        print()
        print_dict(song_dict)
    else:
        print()
        print('OK! These are the attributes to choose from:')
        for k in song_dict.keys():
            print('\t' + k)

        key = input('Choose an attribute: ')
        guess = input('Enter your guess for the value of that attribute: ')

        if guess_is_correct(key, guess):
            print("You're right!")
            print()

    bad_choice = 0
    while not bad_choice:
        if not done:
            choice = input('Would you like to continue (y/n)? ')
            if choice in ('N', 'n'):
                done = 1
                bad_choice = 0
                print('Goodbye!')
            elif choice not in ('Y', 'y'):
                print('You must enter a y or n')
            else:
                bad_choice = 1
        else:
            break

    print()

