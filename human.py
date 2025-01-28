from game import Player
import util

class HumanPlayer(Player):
    def __init__(self, char):
        self.char = char

    def choose_action(self, state):
        actions = state.actions(self.char)
        print("Possible actions:")
        for i, action in enumerate(actions):
            print(f"{i}: {action}")
        choice = int(input("Please choose an action: "))
        return actions[choice]