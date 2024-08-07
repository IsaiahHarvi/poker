"""
Deck Module containing the Deck and Card classes
"""

import numpy as np
from poker.player import Player
from poker.teams.example.ai import AI

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
        
    def build(self) -> None:
        """
        Builds a deck of shuffled cards
        """
        self.cards = [Card(suit, value) for suit in self.deck_suits for value in list(self.card_values)[1:]]
        self.shuffle()
        return

    def shuffle(self) -> None:
        """
        Shuffles the deck according to a seed provided to the Deck class
        """
        np.random.seed(self.seed) 
        np.random.shuffle(self.cards)
        return
    
    def draw(self, count: int = 1) -> list[Card]:
        """
        Draws n (count) cards from the deck
        """
        return [self.cards.pop() for _ in range(count)]
    
    def burn(self) -> None:
        """
        Removes the top card from the deck
        """
        self.cards.pop()
        return
    
    def deal_player_hands(self, players: list[Player]) -> None:
        """
        Deals two cards to each player in the list of players
        """
        for player in players:
            player.hand = self.draw(count=2)
        return

    def deal_flop(self):
        """
        Returns the first three cards
        """
        return self.draw(count=3)

    def burn_turn(self) -> list[Card]:
        self.burn()
        return self.draw()
    
    def __str__(self) -> list[str]:
        """
        Prints the cards in the deck
        """
        return [c.__str__() for c in self.cards]


if __name__ == "__main__":
    import warnings
    warnings.warn("This module is not meant to be run directly, but does contain a simple test.")

    deck = Deck()
    for _ in range(1000):
        test_deck = Deck()
        assert np.all(test_deck.__str__() != deck.__str__())
        assert len(test_deck.__str__()) == len(deck.__str__()) == 52
    print("Passed! (deck.py)")