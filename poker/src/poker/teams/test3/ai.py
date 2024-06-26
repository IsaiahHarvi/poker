import os

class AI():
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return f"{os.path.basename(os.path.dirname(__file__))}"

    def get_action(self) -> dict:
        actions = ['fold', 'check', 'raise', 'call']

        print(f"\nAvailable actions for {self.__str__()}: {actions}")
        action = input("> ").lower()

        if len(action.split()) == 2:
            action, amount = action.split()
            return {"action": action, "amount": int(amount)}
        else:
            return {"action": action, "amount": 0}
