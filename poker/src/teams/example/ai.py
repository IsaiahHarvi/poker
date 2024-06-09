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
        Create an action to send to the game engine.
        Referred to as the response.

        Must call the _send_action method to send your response.
        """

        response = {"action": "fold", "amount": 0}
        return self._send_action(action=response)

    def _send_action(self, response: dict) -> None:
        """
        Send an action to the game engine.

        Args:
            action: dict = { 
                action: str, 
                amount: int if (action == raise) else None
            }
        """
        assert "action" in response, "Response must contain an action key"
        assert response["action"] in ["fold", "check", "raise", "call"], f"Invalid action: '{response['action']}"
        assert "amount" in response, "Response must contain an action key"
        assert isinstance(response["amount"], int), "Raise amount must be an integer"
        assert response["amount"] >= 0, "Raise amount must be non-negative"
        return response
