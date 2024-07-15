"""
Runs the game driver.
"""

from poker.game import Game
from poker.player import construct_players


def main():
    Game(
        players=construct_players(debug=True)
    ).start_hand()


if __name__ == "__main__":
    main()
