"""
Modifiable class for players creating AI.
"""

import os

class AI():
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return f"AI {os.path.basename(os.path.dirname(__file__))}"

    def get_action(self) -> dict:
        # _ex = {
        #     action: fold,
        #     amount: 0 if action == raise
        # }
        actions = ['fold', 'check', 'raise', 'call']

        print(f"Available actions for {self.__str__()}: {actions}")
        action = input("> ").lower()

        if action == 'raise':
            amount = int(input("Amount: "))       
            return {'action': action, 'amount': amount}
        return {'action': action}
