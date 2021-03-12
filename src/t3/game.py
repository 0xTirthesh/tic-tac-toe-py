from t3.constants import BOARD, CROSS, OH, P1️, P2️, P3️, P4️, P5️, P6️, P7️, P8️, P9️


class Game:

    def __init__(self):
        self.__board = [P1️, P2️, P3️, P4️, P5️, P6️, P7️, P8️, P9️]
        self.__is_player_1s_turn = True

        print(f"\nOkay here is your board. Player 1 plays '{CROSS}' & Player 2 plays '{OH}'")

    def display_board(self):
        print(BOARD.format(*self.__board))

    def start(self):
        pass

    def declare_winner(self):
        pass

    def get_state(self):
        return {
            "board": self.__board
        }
