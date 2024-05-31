"""
Modifiable class for players creating AI.
"""

import os

class AI():
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return f"{os.path.basename(os.path.dirname(__file__))}"

    def get_action(self) -> dict:
        return {'action': "call"}
