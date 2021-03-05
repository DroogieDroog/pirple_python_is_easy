"""
pirple/python/final_project/main.py
Final Project

Create a gin rummy game
"""

from random import (shuffle, randint)
from time import sleep
from os import system, name


class Player:

    def __init__(self, name, computer = False):
        self.Name = name
        self.Computer = computer
        self.Hand = {}
        self.Game = 0
        self.Round = 0
        self.Deadwood = 0
        self.Groups = {}

    def new_hand(self, hand, round=0, deadwood=0, groups={}):
        self.Hand = hand
        self.Round = round
        self.Deadwood = deadwood
        self.Groups = groups

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

    def draw(self, source):
        draw_card = source.pop()
        if draw_card[0] in self.Hand.keys():
            self.Hand[draw_card[0]].append(draw_card[1])
        else:
            self.Hand.update({draw_card[0]: [draw_card[1]]})
        self.print_hand()

    def discard(self, hand):
        pass
        #return self.Hand

    def knock(self):
        pass

    def score(self, hand):
        pass
        #return self.Score, self.Round, self.Deadwood


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
    if new_game:
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
        game_target = input('Would you like to play each round to 100 or 200 points? ')
        if int(game_target) not in (100, 200):
            print('You must enter 100 or 200.  Enter again.')
        else:
            break

    while(True):
        player_name = input('Please enter your name: ')
        yn = input('You\'ve chosen {} for your name. Is that correct (y/n)? '.format(player_name))
        if yn.upper() == 'Y':
            print('OK, then let\'s play!')
            break
        else:
            print('Oops! Try again.')

    players = [Player(player_name), Player('Computer', True)]
    card_deck, card_map = create_deck()
    dealer, players[0].Hand, players[1].Hand = deal_hand(card_deck, players)
    discard_pile = [card_deck.pop()]

    return players, dealer, card_deck, card_map, discard_pile, int(game_target)


def display_current_status(players, card_deck, discard_pile):
    break_line = '\u274C' * 25
    cards_left = len(card_deck)
    if len(discard_pile) > 0:
        top_discard = card_map[discard_pile[-1][0]] + discard_pile[-1][1]
    else:
        top_discard = '<Empty>'

    clear_screen()
    print(break_line + '\n')
    players[1].print_hand()
    print()
    print('Draw pile: {} cards   Discard: {}'.format(cards_left, top_discard))
    print()
    players[0].print_hand()
    print('\n' + break_line)


def play_game(players, dealer, card_deck, discard_pile, game_target):
    round_complete = False

    if dealer == 0:
        current_player = 1
    else:
        current_player = 0

    while not round_complete:
        display_current_status(players, card_deck, discard_pile)
        round_complete = play_hand(players[current_player], card_deck, discard_pile)

        if current_player == 0:
            current_player = 1
        else:
            current_player = 0


def play_hand(player, card_deck, discard_pile):
    if len(discard_pile) > 0:
        print('{}, would you like to draw from the deck (D) or discard pile (P)?'.format(player.Name))
        while(True):
            draw_source = input('Make your choice: ')
            if draw_source.upper() not in ('D', 'P'):
                print('You must choose either the (D)eck or discard (P)ile to draw from.')
            else:
                break
    else:
        print('Discard pile is empty. Automatically drawing from the deck for {}.'.format(player.Name))
        draw_source = 'D'

    if draw_source.upper() == 'D':
        player.draw(card_deck)
    else:
        player.draw(discard_pile)

    return False


def main():
    global card_deck, card_map, discard_pile
    clear_screen()
    print('Welcome to JFL Gin Rummy! This is a one-player game against the Computer.')

    players, dealer, card_deck, card_map, discard_pile, game_target = start_new_game()
    play_game(players, dealer, card_deck, discard_pile, game_target)
    x = 1


if __name__ == '__main__':
    main()


