import sys
from game import Game
from human import HumanPlayer
from agent import RandomPlayer, MinimaxPlayer
from munch import State

def get_player(player_type, char):
    if player_type == 'human':
        return HumanPlayer(char)
    elif player_type == 'random':
        return RandomPlayer(char)
    elif player_type == 'minimax':
        return MinimaxPlayer(char)
    else:
        raise ValueError(f"Invalid player type: {player_type}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python main.py <player1> <player2>")
        sys.exit(1)

    player1_type, player2_type = sys.argv[1], sys.argv[2]
    player1 = get_player(player1_type, 'X')
    player2 = get_player(player2_type, 'O')

    game = Game(player1, player2)
    loser, states = game.play() # get loser and states to print for results
    print(f"{loser} loses")
    for state in states:
        print(state.pprint_string() + "\n")
        