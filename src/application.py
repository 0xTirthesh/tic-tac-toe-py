from time import sleep

from t3.constants import RULES
from t3.game import Game

if __name__ == '__main__':
    print("\nWelcome! Let's Play `TicTacToe`")
    print(RULES)
    sleep(1)

    against_computer = False  # input("\nDo you wish to play against the Computer? [y/n] ").lower() == "y"
    game = Game(against_computer)

    sleep(1)
    game.display_board()

    game.start()
    game.declare_winner()
