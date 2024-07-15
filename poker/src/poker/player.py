"""
Instance of a player mapped to an AI
"""

import os
from poker.teams.example.ai import AI # for typing
from importlib import import_module

class Player():
    def __init__(self, ai: AI) -> None:
        self.AI = ai()
        self.name = self.AI.__str__()
        self.hand = [] # list[Card]
        self.chips: int = 0
        self.stake: int = 0 # per hand
        self.folded: bool = False

    def make_move(self, highest_stake: int) -> None:
        return self.AI.get_action()


def construct_players(debug: bool = False) -> list[Player]:
    players = []
    base_dir = os.path.join(os.getcwd(), "src/poker/teams")
    for team_dir in os.listdir(base_dir):
        if ("test" in team_dir and not debug) or (team_dir == "example"):
            continue # skip test teams and the example unless debug is enabled

        team_path = os.path.join(base_dir, team_dir)
        if os.path.isdir(team_path) and "ai.py" in os.listdir(team_path):
            try:
                ai_module = import_module(f"poker.teams.{team_dir}.ai")
                imported_class = getattr(ai_module, 'AI', None)
                if imported_class:
                    players.append(Player(ai = imported_class))
                else:
                    raise ValueError(f"No AI class found in teams.{team_dir}.ai")
            except ImportError as e:
                raise ImportError(f"Error trying to import 'teams.{team_dir}.ai': {str(e)}")
    return players


if __name__ == "__main__":
    raise RuntimeError("This submodule is not meant to be run directly.")
