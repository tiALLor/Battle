from abc import ABC, abstractmethod
from dataclasses import dataclass
import random

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


@dataclass
class Playingcard:
    rank: str
    suit: str

    def __str__(self):\
        return f"{self.rank}{self.suit}"
    
    def value(self):
        print(self.rank)
        return RANKS.index(self.rank)
    
@dataclass
class PlayingDeck:
    deck = []

    def add_card(self, card):
        self.deck.append(card)

    def draw_card(self):
        return self.deck.pop(0)
    
    def make_deck(self):
        self.deck = []
        for r in RANKS:
            for s in SUITS:
                self.deck.append(Playingcard(rank=r, suit=s))

        
   

if __name__ == "__main__":
    card = Playingcard("7", "♡")

    initial_deck = PlayingDeck()
    initial_deck.make_deck()

    print(initial_deck.draw_card())

    