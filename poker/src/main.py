"""
Runs the game driver.
"""

from game import Game
from player import construct_players


def main():
    Game(construct_players(debug=True)).start_hand()


if __name__ == "__main__":
    main()
