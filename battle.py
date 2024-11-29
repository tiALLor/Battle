from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import random
import sys

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def make_52_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):\
        return f"{self.rank}{self.suit}"
    
    def value(self):
        return RANKS.index(self.rank)
    
@dataclass
class PlayingDeck:
    cards: list[PlayingCard] = field(default_factory=make_52_deck)

    def add_card(self, card):
        self.cards.append(card)

    def draw_card(self):
        return self.cards.pop(0)
    
    def shuffle_deck(self):
        random.shuffle(self.cards)

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'


def deal_the_cards(deck):
    deck_of_player1 = PlayingDeck([])
    deck_of_player2 = PlayingDeck([])
    while deck.cards:
        deck_of_player1.add_card(deck.draw_card())
        deck_of_player2.add_card(deck.draw_card())
    return deck_of_player1, deck_of_player2

def turn(won_cards=PlayingDeck([])):
    try:
        # global deck_p1
        # global deck_p2
        card1 = deck_p1.draw_card()
        card2 = deck_p2.draw_card()
        won_cards.add_card(card1)
        won_cards.add_card(card2)
        print(f"Player1 has drawn {card1}")
        print(f"Player2 has drawn {card2}")
        if card1.value() > card2.value():
            print(f"\nPlayer1 won the turn and adds {won_cards} to his deck!\n")
            deck_p1.cards += won_cards.cards
        elif card1.value() < card2.value():
            print(f"\nPlayer2 won the turn and adds {won_cards} to his deck!\n")
            deck_p1.cards += won_cards.cards
        else:
            print("Battle!!!\n")
            for _ in range (3):
                won_cards.add_card(deck_p1.draw_card())
                won_cards.add_card(deck_p2.draw_card())
            turn(won_cards)
        won_cards.cards.clear()
    except IndexError:
        print("We have a winner!")
        win_report()
    

def win_report():
    # global deck_p1
    # global deck_p2
    if deck_p1:
        sys.exit("Player1 has won!")
    elif deck_p2:
        sys.exit("Player2 has won!")
    

if __name__ == "__main__":

    initial_deck = PlayingDeck()
    initial_deck.shuffle_deck()
      
    deck_p1, deck_p2 = deal_the_cards(initial_deck)
    print(deck_p1)
    print(deck_p2)

    while deck_p1 and deck_p2:
        turn()
        print()
        print(f"Player1: {deck_p1}")
        print(f"Player2: {deck_p2}")
        # input("Press ENTER!")
        print()
        
    win_report()    
    initial_deck.shuffle_deck()
      
    deck_p1, deck_p2 = deal_the_cards(initial_deck)
    print(deck_p1)
    print(deck_p2)

    while deck_p1 and deck_p2:
        turn()
        print()
        print(f"Player1: {deck_p1}")
        print(f"Player2: {deck_p2}")
        # input("Press ENTER!")
        print()
        

    win_report()    