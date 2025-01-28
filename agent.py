from audioop import minmax
from game import Player 
import random

class RandomPlayer(Player):
    def __init__(self, char):
        self.char = char

    def choose_action(self, state):
        actions = state.actions(self.char)
        return random.choice(actions)

class MinimaxPlayer(Player):
    def __init__(self, char, depth=6):
        self.char = char
        self.depth = depth

    def choose_action(self, state):

        actions = state.actions(self.char)
        best_eval = float('-inf')
        best_action = None
        for action in actions:
            new_state = state.clone().execute(action)
            eval = self.minimax(new_state, self.depth - 1, False)
            if eval > best_eval:    
                best_eval = eval
                best_action = action
        return best_action
    
    def minimax(self, state, depth, maximizing_player):
        if state.game_over():   # Check if game is over or depth limit reached
            return self.evaluate(state)

        if maximizing_player:
            max_eval = float('-inf')   # Set initial max evaluation
            best_action = None
            for action in state.actions(self.char):
                new_state = state.clone().execute(action)
                eval = self.minimax(new_state, depth - 1, False)  # Recursively call minimax for the new state
                if eval > max_eval:
                    max_eval = eval
                    best_action = action      # Update max evaluation and best action
            return max_eval
        else:
            min_eval = float('inf') # Set initial min evaluation
            best_action = None
            for action in state.actions(self.other_char()):
                new_state = state.clone().execute(action)
                eval = self.minimax(new_state, depth - 1, True)    # Recursively call minimax for the new state
                if eval < min_eval:
                    min_eval = eval
                    best_action = action
            return min_eval



    def other_char(self):
        return 'O' if self.char == 'X' else 'X'

    def evaluate(self, state):
        loser = state.loser()
        if loser == self.char:
            return -1
        elif loser == self.other_char():
            return 1
        else:
            return 0