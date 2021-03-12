from t3.constants import RULES
from t3.game import Game

if __name__ == '__main__':
    print("\nWelcome! Let's Play `TicTacToe`")
    print(RULES)

    game = Game()
    game.display_board()
    game.start()
    game.declare_winner()
