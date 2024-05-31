"""
Actual game logic
"""

from collections import Counter
from itertools import combinations
from deck import Deck, Card, DECK_SUITS, CARD_VALUES
from player import Player

class Game:
    def __init__(self, players: list[Player]) -> None:
        self.players = players
        self.deck = Deck()  # creates and shuffles a deck
        self.table_cards = []
        self.small_blind_idx = 0  # index to specfic player in players list
        self.big_blind_idx = (self.small_blind_idx + 1) % len(self.players)
        self.last_raise_idx = None
        self.pot = 0
        self.highest_stake = 0

        self.start_hand() # Start Game
    
    def start_hand(self):
        self.pot = 0
        self.deck.deal_player_hands(self.players)
        self.take_blinds()
        self.get_bets()
        self.table_cards.extend(self.deck.deal_flop())
        for _ in range(2):
            self.get_bets()
            self.table_cards.extend(self.deck.burn_turn())
        self.get_bets()
        self.evaluate_winner()

    def take_blinds(self):
        small_blind = 1
        big_blind = small_blind * 2

        self.players[self.small_blind_idx].chips -= small_blind
        self.players[self.big_blind_idx].chips -= big_blind
        self.players[self.small_blind_idx].stake += small_blind
        self.players[self.big_blind_idx].stake += big_blind

    def get_bets(self):
        current_player_idx = self.small_blind_idx   # not correct for pre flop betting'
        players = [p for p in self.players if not p.folded]

        while True: # TODO: revisit this
            player = players[current_player_idx]
            
            move: dict = player.make_move() # gets the dict from the player's AI
            if move['action'] == 'fold':
                player.folded = True
            elif move['action'] == 'raise':
                self.last_raise_idx = current_player_idx
                self.pot += move['amount']
                player.stake += move['amount']
                player.chips -= move['amount']
                self._get_highest_stake() # TODO: move validation
            elif move['action'] == 'call':
                amount_owed = self.highest_stake - player.stake
                self.pot += amount_owed
                player.chips -= amount_owed
                player.stake = self.highest_stake
            elif move['action'] == 'check':
                pass
            else:
                raise ValueError(f"Invalid action: {move['action']}")
        
            print(f"{player.name} {move['action']}s {move.get('amount', '')} chips\n{' '.join(str(card) for card in player.hand)} | {' '.join(str(card) for card in self.table_cards)}")

            current_player_idx = (current_player_idx + 1) % len(players)
            if (current_player_idx == self.last_raise_idx) or (self.last_raise_idx is None):
                break

    def evaluate_winner(self):
        hands = {}
        for player in self.players:
            if player.folded:
                continue

            hands[self._get_best_hand(player.hand, self.table_cards)] = player

        best = max(hands.keys())
        player = hands[best]
        print(f"{player.name} wins with score {best}!\n{' '.join(str(card) for card in player.hand)} | {' '.join(str(card) for card in self.table_cards)}")

        player.chips += self.pot - player.stake

    def _get_highest_stake(self):
        for player in self.players:
            if player.stake > self.highest_stake:
                self.highest_stake = player.stake

    def _get_best_hand(self, hole_cards, community_cards):
        all_cards = hole_cards + community_cards
        best_hand = None
        best_rank = None
        for combination in combinations(all_cards, 5):
            rank = self._rank_hand(combination)
            if best_rank is None or rank > best_rank:
                best_rank = rank
                best_hand = combination
        return best_rank

    def _rank_hand(self, hand):
        suits = DECK_SUITS
        values = CARD_VALUES
        value_counts = Counter(card.value for card in hand)
    
        is_flush = len(set(suits)) == 1
        is_straight = len(value_counts) == 5 and (max(card.value for card in hand) - min(card.value for card in hand) == 4)
        sorted_values = sorted(value_counts.keys(), key=lambda x: values[x], reverse=True)

        if is_straight and is_flush:
            return (8, sorted_values)  # Straight flush
        elif 4 in value_counts.values():
            return (7, self._get_rank_value(value_counts, 4, 1))  # Four of a kind
        elif 3 in value_counts.values() and 2 in value_counts.values():
            return (6, self._get_rank_value(value_counts, 3, 2))  # Full house
        elif is_flush:
            return (5, sorted_values)  # Flush
        elif is_straight:
            return (4, sorted_values)  # Straight
        elif 3 in value_counts.values():
            return (3, self._get_rank_value(value_counts, 3, 1))  # Three of a kind
        elif list(value_counts.values()).count(2) == 2:
            return (2, self._get_rank_value(value_counts, 2, 2))  # Two pair
        elif 2 in value_counts.values():
            return (1, self._get_rank_value(value_counts, 2, 1))  # One pair
        else:
            return (0, sorted_values)  # High card

    def _get_rank_value(self, values, value_counts, *counts):
        result = []
        for count in counts:
            for value, num in value_counts.items():
                if num == count:
                    result.append(value)
        result.sort(key=lambda x: values.index(x), reverse=True)
        return result


if __name__ == "__main__":
    pass