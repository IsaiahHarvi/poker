import sys
import os
import pytest
from poker.deck import Deck, Card, DECK_SUITS, CARD_VALUES
from poker.player import Player, construct_players


def test_init():
    deck = Deck()
    assert len(deck.cards) == 52, "Deck should contain 52 cards"
    assert {card.suit for card in deck.cards} == set(DECK_SUITS.keys()), "Deck should contain all four suits"
    assert {card.value for card in deck.cards} == set(CARD_VALUES.keys()) - {1}, "Deck should contain all card values except ace (low)"

def test_card_representation():
    card = Card('Hearts', 1)
    assert str(card) == 'A♥', "Card representation should be 'A♥'"

def test_shuffle_deck():
    deck1 = Deck(seed=69)
    deck2 = Deck(seed=69)
    assert deck1.cards_() == deck2.cards_(), "Decks with same seed should be shuffled identically"

def test_draw_cards():
    deck = Deck()
    initial_count = len(deck.cards)
    drawn_cards = deck.draw(count=5)
    assert len(drawn_cards) == 5, "Should draw 5 cards"
    assert len(deck.cards) == initial_count - 5, "Deck should have 5 fewer cards after drawing"

def test_burn_card():
    deck = Deck()
    initial_count = len(deck.cards)
    deck.burn()
    assert len(deck.cards) == initial_count - 1, "Deck should have 1 fewer card after burning"

def test_deal_player_hands():
    deck = Deck()
    players = construct_players(debug=True)
    deck.deal_player_hands(players)
    for player in players:
        assert len(player.hand) == 2, "Each player should have 2 cards in hand"
    assert len(deck.cards) == 52 - (2 * len(players)), f"Deck should have {2*len(players)} fewer cards after dealing hands to {len(players)} players"

def test_deal_flop():
    deck = Deck()
    flop = deck.deal_flop()
    assert len(flop) == 3, "Flop should contain 3 cards"
    assert len(deck.cards) == 52 - 3, "Deck should have 3 fewer cards after dealing the flop"

def test_burn_turn():
    deck = Deck()
    initial_count = len(deck.cards)
    deck.burn_turn()
    assert len(deck.cards) == initial_count - 2, "Deck should have 2 fewer cards after burning and drawing"

if __name__ == "__main__":
    pytest.main()
