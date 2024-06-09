import pytest
from poker.deck import Deck, Card
from poker.player import Player, construct_players
from poker.game import Game
from poker.teams.example.ai import AI as MockAI

class MockPlayer(Player):
    def __init__(self, name, chips, ai):
        super().__init__(ai)
        self.name = name
        self.chips = chips
        self.move_sequence = []
        self.current_move = 0

    def set_moves(self, moves):
        self.move_sequence = moves

    def make_move(self, highest_stake):
        move = self.move_sequence[self.current_move]
        self.current_move += 1
        return move

@pytest.fixture(scope="module")
def setup_game():
    players = construct_players(debug=True)
    for i in range(len(players)):
        players[i] = MockPlayer(f"Player {i}", 1000, MockAI)
    game = Game(players)
    return game, players

def test_game_initialization(setup_game):
    game, players = setup_game
    assert len(game.players) == len(players)
    assert isinstance(game.deck, Deck)
    assert game.pot == 0
    assert game.highest_stake == 0

def test_take_blinds(setup_game):
    game, players = setup_game
    game._take_blinds()
    assert players[0].chips == 999
    assert players[0].stake == 1
    assert players[1].chips == 998
    assert players[1].stake == 2
    assert game.pot == 3

def test_get_bets(setup_game):
    game, players = setup_game
    players[0].set_moves([{"action": "call"}, {"action": "check"}])
    players[1].set_moves([{"action": "call"}, {"action": "check"}])
    players[2].set_moves([{"action": "check"}])

    game._get_bets()
    assert game.pot == 3 # just the blind amount

def test_evaluate_winner(setup_game):
    game, players = setup_game
    players[0].hand = [Card('Hearts', 2), Card('Hearts', 3)]
    players[1].hand = [Card('Hearts', 4), Card('Hearts', 5)]
    players[2].hand = [Card('Hearts', 6), Card('Hearts', 7)]
    game.table_cards = [
        Card('Hearts', 8), Card('Hearts', 9), 
        Card('Hearts', 10), Card('Diamonds', 11), 
        Card('Clubs', 12)
    ]

    players[0].folded = False
    players[1].folded = False
    players[2].folded = False

    game._evaluate_winner()
    assert players[2].chips == 1000 + game.pot - players[2].stake
    

if __name__ == "__main__":
    pytest.main()
