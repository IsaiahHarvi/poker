"""
Deck Module containing the Deck and Card classes
"""

import numpy as np
import warnings
from player import Player


DECK_SUITS = {
    'Hearts': "♥",
    'Diamonds': "♦",
    'Clubs': "♣",
    'Spades': "♠"
}

CARD_VALUES = {
    1: 'A',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '10',
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A' # NOTE: ace high or low, this logic may need revisited
}

class Card():
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value
        self.deck_suits = DECK_SUITS
        self.card_values = CARD_VALUES

    def __str__(self) -> str:
        return f"{self.card_values[self.value]}{self.deck_suits[self.suit]}"


class Deck():
    def __init__(self, seed: int | None = None) -> None:
        self.deck_suits = DECK_SUITS
        self.card_values = CARD_VALUES
        self.seed: int | None = seed
        self.build()
        
    def build(self) -> list[Card]:
        """
        Builds a deck of shuffled cards
        """
        self.cards = [Card(suit, value) for suit in self.deck_suits for value in list(self.card_values)[1:]]
        self.shuffle()

    def shuffle(self) -> list[Card]:
        """
        Shuffles the deck according to a seed provided to the Deck class
        """
        np.random.seed(self.seed) 
        np.random.shuffle(self.cards)
    
    def draw(self, count: int = 1) -> list[Card]:
        return [self.cards.pop() for _ in range(count)]
    
    def burn(self) -> Card:
        return self.cards.pop()
    
    def deal_player_hands(self, players: list[Player]) -> None:
        for player in players:
            player.hand = self.draw(count=2)

    def deal_flop(self):
        return self.draw(count=3)

    def burn_turn(self):
        self.burn()
        return self.draw()
    
    def cards_(self):
        return [c.__str__() for c in self.cards]


if __name__ == "__main__":
    warnings.warn("This module is not meant to be run directly, but does contain a simple test.")

    deck_ = Deck()
    for _ in range(10_000):
        assert np.all((c_deck := Deck().cards_()) == deck_.cards_()), print(f"{c_deck}\n\n\n{deck_.cards_()}")
        assert len(deck_.cards_()) == len(c_deck) == 52
    print("Passed! (deck.py)")