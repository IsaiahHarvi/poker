"""
Game
"""

import os
from game import Game
from player import Player, construct_players
from ai import AI


def main():
    Game(construct_players(debug=True))


if __name__ == "__main__":
    main()
