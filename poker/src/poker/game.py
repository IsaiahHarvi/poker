"""
Actual game logic and driver for the AI to play aganist each other.
"""

import numpy as np
from collections import Counter
from itertools import combinations
from poker.deck import Deck, Card, DECK_SUITS, CARD_VALUES
from poker.player import Player

class Game:
    def __init__(self, players: list[Player]) -> None:
        self.players = players
        self.deck = Deck()  # creates and shuffles a deck
        self.table_cards = []
        self.small_blind = 1 # TODO: increment as the game progresses
        self.small_blind_idx = 0  # index to specfic player in players list
        self.big_blind_idx = (self.small_blind_idx + 1) % len(self.players)
        self.last_raise_idx = None
        self.pot = 0
        self.highest_stake = 0
    
    def start_hand(self):
        self.pot = 0
        self.deck.deal_player_hands(self.players)
        self._take_blinds(self.small_blind)
        self._get_bets()
        self.table_cards.extend(self.deck.deal_flop())
        for _ in range(2):
            self._get_bets()
            self.table_cards.extend(self.deck.burn_turn())
        self._get_bets()
        self._evaluate_winner()

    def _take_blinds(self, small_blind: int = 1):
        big_blind = small_blind * 2

        self._update_stake_chips(self.small_blind_idx, small_blind)
        self._update_stake_chips(self.big_blind_idx, big_blind)

    def _update_stake_chips(self, idx: int, amount: int):
        self.players[idx].chips -= amount
        self.players[idx].stake += amount
        self.pot += amount

    def _get_bets(self):
        current_player_idx = self.small_blind_idx   # not correct for pre flop betting'
        players = [p for p in self.players if not p.folded]

        while True: # TODO: revisit this, again
            player = players[current_player_idx]
            
            print(f"{self.pot = }")
            print(f"{self.highest_stake = }")

            move: dict = player.make_move(self.highest_stake) # gets the dict from the player's AI
            self._parse_move(move, player, current_player_idx)
        
            print(f"{player.name} {move['action']}s {move.get('amount', '')} chips\n{' '.join(str(card) for card in player.hand)} | {' '.join(str(card) for card in self.table_cards)}")

            current_player_idx = (current_player_idx + 1) % len(players)
            if (current_player_idx == self.last_raise_idx) or \
               (self.last_raise_idx is None) or \
               (len([p for p in players if not p.folded]) == 1):
                break

    def _parse_move(self, move: dict, player: Player, player_idx: int):
        if move["action"] == "fold":
            player.folded = True
        elif move["action"] == "raise":
            amount = move["amount"]
            self._update_stake_chips(player_idx, amount)
            self.highest_stake = max(self.highest_stake, player.stake)
            self.last_raise_idx = player_idx
        elif move["action"] == "call":
            amount = self.highest_stake - player.stake
            if (amount > 0): self._update_stake_chips(player_idx, amount)
        elif move["action"] == "check":
            pass
        else:
            raise ValueError(f"Invalid move: {move}")
        return # move["action"]

    def _evaluate_winner(self): # TODO: rework this -- its messy
        hands = {}
        for player in self.players:
            if player.folded:
                continue

            hands[player] = self._get_best_hand(player.hand, self.table_cards)

        if len(hands) == 0:
            print("All players folded!")
            return
        
        if len(hands) == 1:
            print(f"{player.name} wins by default with score {hands[player]}!\n{' '.join(str(card) for card in player.hand)} | {' '.join(str(card) for card in self.table_cards)}")
            return
        
        for player in hands.keys():
            if hands[player] == max(hands.values()):
                best = hands[player]
                break
        print(f"{player.name} wins with score {best}!\n{' '.join(str(card) for card in player.hand)} | {' '.join(str(card) for card in self.table_cards)}")

        player.chips += self.pot - player.stake

    def _get_best_hand(self, hole_cards: list[Card], community_cards: list[Card]):
        all_cards = hole_cards + community_cards
        # best_hand = None
        best_rank = None
        for combination in combinations(all_cards, 5):
            rank = self._rank_hand(combination)
            if best_rank is None or rank > best_rank:
                best_rank = rank
                # best_hand = combination
        return best_rank # , best_hand

    def _rank_hand(self, hand: list[Card]):
        suits = [card.suit for card in hand]
        hand_values = [card.value for card in hand]
        value_counts = Counter(card.value for card in hand)

        is_flush = (len(set(suits)) == 1)
        is_straight = (len(value_counts) == 5 and (max(hand_values) - min(hand_values) == 4))  #
        sorted_values = sorted(value_counts.keys(), key=lambda x: CARD_VALUES[x], reverse=True)

        if (is_straight and is_flush):     # Straight flush
            return (8, sorted_values) 
        elif 4 in value_counts.values():   # Four of a kind
            return (7, self._get_rank_value(value_counts, 4, 1))
        elif (3 in value_counts.values() and 2 in value_counts.values()): # Full house
            return (6, self._get_rank_value(value_counts, 3, 2))
        elif is_flush:
            return (5, sorted_values)  
        elif is_straight:
            return (4, sorted_values)
        elif 3 in value_counts.values():   # Three of a kind
            return (3, self._get_rank_value(value_counts, 3, 1))  
        elif list(value_counts.values()).count(2) == 2:
            return (2, self._get_rank_value(value_counts, 2, 2))  # Two pair
        elif 2 in value_counts.values():
            return (1, self._get_rank_value(value_counts, 2, 1))  # One pair
        else:
            return (0, sorted_values)  # High card

    def _get_rank_value(self, value_counts: Counter[int], *counts):
        values, nums = np.array(list(value_counts.items())).T
        result = values[np.isin(nums, counts)].tolist()
        result.sort(key=lambda x: list(CARD_VALUES.keys()).index(x), reverse=True)

        return result


if __name__ == "__main__":
    raise RuntimeError("This submodule is not meant to be run directly.")
