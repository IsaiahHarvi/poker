"""
Modifiable class for players creating AI.
"""

from abc import ABC, abstractmethod

class AI(ABC):
    def __init__(self):
        ...

    def __str__(self) -> str:
        ... # return name of AI

    def get_action(self) -> dict:
        # _ex = {
        #     action: fold,
        #     amount: 0 if action == raise
        # }

        # Modified by player
        ...


