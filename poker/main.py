"""
Game
"""

import os
from deck import Deck, Card
from player import Player, construct_players
from ai import AI

def main():
    deck = Deck() 
    players = construct_players(debug=True)
    print(players)




if __name__ == "__main__":
    main()
