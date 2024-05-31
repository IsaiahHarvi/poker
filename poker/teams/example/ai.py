"""
Modifiable class for players creating AI.
"""

import os
from abc import ABC

class AI(ABC):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        """
        Return name of AI, defaults to your team's directory name.
        """
        return f"{os.path.basename(os.path.dirname(__file__))}"

    def get_action(self) -> dict:
        """
        Return an action to be sent to the game engine.

        Possible actions: ["fold", "check", "raise", "call"]

        Returns:
            response: dict = { 
                action: str, 
                amount: int if (action == raise) else None
            }
        """

            
        # assert action in ["fold", "check", "raise", "call"], f"Invalid action: {action}"
        return {"action" : "call", "amount" : None}

