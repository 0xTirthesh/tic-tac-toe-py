from time import sleep

from t3.constants import RULES
from t3.game import Game

if __name__ == '__main__':
    print("\nWelcome! Let's Play `TicTacToe`")
    print(RULES)
    sleep(1)

    game = Game()

    sleep(1)
    game.display_board()

    game.start()
    game.declare_winner()
