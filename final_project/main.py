"""
pirple/python/final_project/main.py
Final Project

Create a Go Fish game
"""

from random import (shuffle, randint)
from time import sleep
from os import system, name

class Player:

    def __init__(self, name, computer = False):
        self.Name = name
        self.Computer = computer
        self.new_hand()

    def new_hand(self):
        self.Hand = {}
        self.HandCounts = {}
        self.Sets = []
        self.Wishes = []

    def hand_counts(self):
        for denom in self.Hand.keys():
            self.HandCounts.update({denom: len(self.Hand[denom])})

    def check_wishes(self):
        if set(self.Wishes) == set(self.Hand.keys()):
            self.Wishes = []
        elif len(self.Wishes) == 5:
            self.Wishes.pop(0)

    def print_hand(self):
        if self.Name.upper().endswith('S'):
            print('{}\' hand: '.format(self.Name), end=' ')
        else:
            print('{}\'s hand: '.format(self.Name), end=' ')

        for denom in sorted(self.Hand):
            for suit in self.Hand[denom]:
                if self.Computer:
                    print('\u2733', end=' ')
                else:
                    print(card_map[denom] + suit, end=' ')
        print()
        if self.Sets != []:
            self.print_sets()

    def print_sets(self):
        if self.Name.upper().endswith('S'):
            print('{}\' sets: '.format(self.Name), end=' ')
        else:
            print('{}\'s sets: '.format(self.Name), end=' ')

        for denom in sorted(self.Sets):
            print(card_map[denom] + 's', end=' ')
        print()

    def cast(self, opp_hand, card_deck, wish):
        if wish in opp_hand.keys():
            print('Fish, fish, you got your wish!')
            opp_cards = opp_hand.pop(wish)

            if wish in self.Hand.keys():
                for card in opp_cards:
                    self.Hand[wish].append(card)
            else:
                self.Hand.update({wish: opp_cards})

            return True
        else:
            print('Nope! Go fish.')
            sleep(2)
            got_wish = self.fish(card_deck, wish)
            return got_wish

    def fish(self, card_deck, wish):
        draw_card = card_deck.pop()

        if draw_card[0] in self.Hand.keys():
            self.Hand[draw_card[0]].append(draw_card[1])
        else:
            self.Hand.update({draw_card[0]: [draw_card[1]]})

        if draw_card[0] == wish:
            print('Fish, fish, you got your wish!')
            return True
        else:
            print('Booooo, you didn\'t get your wish.')
            sleep(3)
            return False

    def lay_set(self):
        new_set = -1
        for card, suits in self.Hand.items():
            if len(suits) == 4:
                new_set = card

        if new_set != -1:
            self.Hand.pop(new_set)
            self.Sets.append(new_set)

        if len(self.Hand) == 0:
            return True
        else:
            return False


def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def create_deck():
    deck = []
    map = {}

    card_denominations = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    #suits = [hearts, diamonds, spades, clubs]
    suits = ['\u2665', '\u2666', '\u2660', '\u2663']

    for card in range(13):
        map.update({card: card_denominations[card]})
        for suit in suits:
            deck.append([card, suit])
    shuffle(deck)

    return deck, map


def choose_dealer(new_game, winner):
    if new_game or winner == 2:
        r = randint(1, 100)
        if r <= 50:
            dealer = 0
        else:
            dealer = 1
    else:
        if winner == 0:
            dealer = 1
        else:
            dealer = 0

    return dealer


def deal_hand(deck, players, new_game=True, winner=None):
    hands = []
    hands.append({})
    hands.append({})

    for card in range(10):
        for hand in range(2):
            top_card = deck.pop()
            if top_card[0] in hands[hand].keys():
                hands[hand][top_card[0]].append(top_card[1])
            else:
                hands[hand].update({top_card[0]: [top_card[1]]})

    dealer = choose_dealer(new_game, winner)
    if dealer == 0:
        print('{} is the dealer. {} goes first. Dealing the hands . . .'.format(players[0].Name, players[1].Name))
        sleep(2)
        return dealer, hands[1], hands[0]
    else:
        print('{} is the dealer. {} goes first. Dealing the hands . . .'.format(players[1].Name, players[0].Name))
        sleep(2)
        return dealer, hands[0], hands[1]


def start_new_game():
    while(True):
        player_name = '--help'
        while player_name.upper() == '--HELP':
            player_name = input('Please enter your name (or --help for the rules): ')
            if player_name.upper() == '--HELP':
                print_rules()

        yn = input('You\'ve chosen {} for your name. Is that correct (y/n)? '.format(player_name))
        if yn.upper() == 'Y':
            print('OK, then let\'s play!')
            break
        else:
            print('Oops! Try again.')

    players = [Player(player_name), Player('Computer', True)]
    card_deck, card_map = create_deck()
    dealer, players[0].Hand, players[1].Hand = deal_hand(card_deck, players)

    return players, dealer, card_deck, card_map


def play_again(players, winner):
    players[0].new_hand()
    players[1].new_hand()
    card_deck, card_map = create_deck()
    dealer, players[0].Hand, players[1].Hand = deal_hand(card_deck, players, False, winner)

    return dealer, card_deck, card_map


def display_current_status(players, card_deck):
    break_line = '\u274C' * 25
    cards_left = len(card_deck)

    clear_screen()
    print(break_line + '\n')
    players[1].print_hand()
    print()
    print('Draw pile: {} cards'.format(cards_left))
    print()
    players[0].print_hand()
    print('\n' + break_line)


def determine_winner(players, card_deck):
    display_current_status(players, card_deck)

    sets0 = len(players[0].Sets)
    sets1 = len(players[1].Sets)
    if sets0 > sets1:
        print('{} wins, {} sets to {}'.format(players[0].Name, sets0, sets1))
        winner = 0
    elif sets1 > sets0:
        print('{} wins, {} sets to {}'.format(players[1].Name, sets1, sets0))
        winner = 1
    else:
        print('It\'s a tie!')
        winner = 2

    print('Good game!')
    return winner


def play_game(players, dealer, card_deck):
    game_over = False

    if dealer == 0:
        current_player = 1
    else:
        current_player = 0

    while not game_over:
        game_over = play_hand(players, current_player, card_deck, card_map)

        if players[current_player].Computer:
            while True:
                wait = input('Enter a C to continue . . .')
                if wait.upper() == 'C':
                    break

        if current_player == 0:
            current_player = 1
        else:
            current_player = 0

    return determine_winner(players, card_deck)


def play_hand(players, current_player, card_deck, card_map):
    got_wish = True
    game_over = False

    card_map_keys = list(card_map.keys())
    card_map_values = list(card_map.values())

    if current_player == 0:
        opp_hand = players[1].Hand
        opp_sets = players[1].Sets
    else:
        opp_hand = players[0].Hand
        opp_sets = players[0].Sets

    display_current_status(players, card_deck)
    player = players[current_player]
    print('Your turn, {}.'.format(player.Name))
    if player.Computer:
        player.HandCounts = {}

    while got_wish and not game_over:
        if player.Computer:
            player.hand_counts()
            wish = generate_wish(player, opp_sets, card_map)
        else:
            wish = request_wish(player, card_map, card_map_values)

        got_wish = player.cast(opp_hand, card_deck, card_map_keys[wish])

        if card_deck == []:
            game_over = True
        else:
            game_over = player.lay_set()

        if got_wish and not game_over and not player.Computer:
            player.print_hand()

    return game_over


def request_wish(player, card_map, card_map_values):
    while True:
        wish = input('What is your wish? ')
        if wish.upper() not in card_map.values():
            print('You must wish for a valid card value (2-10, J, Q, K, A)')
        else:
            value_position = card_map_values.index(wish.upper())
            if value_position not in player.Hand.keys():
                print('You must wish for a card value in your hand.')
            else:
                break

    return value_position


def generate_wish(player, opp_sets, card_map):
    player.check_wishes()
    highest_count = 0
    most_cards = -1

    while most_cards == -1:
        for denom, count in player.HandCounts.items():
            if (count > highest_count) and (denom not in player.Wishes)\
                    and (denom not in opp_sets) and (denom not in player.Sets):
                most_cards = denom
                highest_count = count

        if most_cards == -1:
            player.Wishes = []
            player.HandCounts = {}
            player.hand_counts()

    player.Wishes.append(most_cards)
    print('{} is wishing for a {}.'.format(player.Name, card_map[most_cards]))
    return most_cards


def print_rules():
    clear_screen()
    with open('data/rules.txt', 'r') as rules:
        rules_text = rules.read()
        print(rules_text)

    while True:
        wait = input('Enter an R to return to the game . . .')
        if wait.upper() == 'R':
            clear_screen()
            break


def main():
    global card_deck, card_map
    clear_screen()
    print('Welcome to JFL Go Fish! This is a one-player game against the Computer.')

    players, dealer, card_deck, card_map = start_new_game()

    play = True
    while play:
        winner = play_game(players, dealer, card_deck)

        yn = input('Would you like to play again (y/n)? ')
        if yn.upper() != 'Y':
            play = False
        else:
            dealer, card_deck, card_map = play_again(players, winner)

    print('Goodbye!')

if __name__ == '__main__':
    main()
