"""
pirple/python/final_project/main.py
Final Project

Create a gin rummy game
"""

from random import (shuffle, randint)
from os import system, name


class Player:

    def __init__(self, name, computer = False):
        self.Name = name
        self.Computer = computer
        self.Hand = {}
        self.Match = 0
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

    def score(self, hand):
        pass
        #return self.Score, self.Round, self.Deadwood

    def draw(self, hand):
        pass
        #return self.Hand

    def discard(self, hand):
        pass
        #return self.Hand

    def knock(self):
        pass


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


def choose_dealer(new_match, winner):
    if new_match:
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


def deal_hand(deck, new_match=True, winner=None):
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

    dealer = choose_dealer(new_match, winner)
    if dealer == 0:
        return dealer, hands[1], hands[0]
    else:
        return dealer, hands[0], hands[1]


def start_new_match():
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
    dealer, players[0].Hand, players[1].Hand = deal_hand(card_deck)
    discard_pile = [card_deck.pop()]

    return players, dealer, card_deck, card_map, discard_pile


def display_current_status(players, dealer):
    clear_screen()
    pass

def play_round(players, dealer):
    display_current_status(players, dealer)



def main():
    global card_deck, card_map, discard_pile
    print('Welcome to JFL Gin Rummy! This is a one-player game against the Computer.')

    players, dealer, card_deck, card_map, discard_pile = start_new_match()
    play_round(players, dealer)
    x = 1


if __name__ == '__main__':
    main()


