from munch import State

class Player:
    def choose_action(self, state):
        pass

class Game:
    def __init__(self, player1, player2, initial_state=State()):
        self.player1 = player1
        self.player2 = player2
        self.state = initial_state

    def play(self):
        states = []
        current_player = self.player1
        other_player = self.player2
        while not self.state.game_over():
            action = current_player.choose_action(self.state) #Choose an action
            self.state.execute(action)
            states.append(self.state.clone())
            current_player, other_player = other_player, current_player
        loser = self.state.loser()
        return loser, states