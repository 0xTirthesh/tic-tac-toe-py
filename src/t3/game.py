from time import sleep

from t3.constants import BOARD, CROSS, OH, P1️, P2️, P3️, P4️, P5️, P6️, P7️, P8️, P9️


class Game:

    def __init__(self, against_computer: bool):
        self.__board = [P1️, P2️, P3️, P4️, P5️, P6️, P7️, P8️, P9️]
        self.__is_player_1s_turn = True
        self.__playing_against_computer = against_computer
        self.__is_player_1_winner = None

        if against_computer:
            print(f"\nOkay here is your board. Player 1 plays '{CROSS}' & Computer plays '{OH}'")
        else:
            print(f"\nOkay here is your board. Player 1 plays '{CROSS}' & Player 2 plays '{OH}'")

    def display_board(self):
        print(BOARD.format(*self.__board))

    def start(self):
        """
        - will check at each step if more steps available or not?
        - player will have to choose from number's 1-9
        - player chooses an option, validate it - cannot override + within the bounds
        - if invalid, keep on re-trying until player chooses the right value
        - record the move in the case of valid selection
        - check the status of the board... is game over?
        - if yes, then mark the winner and exit else swap the turn and continue
        - display the board for each iteration
        """
        can_continue = True  # not self.__is_game_over()
        while can_continue and self.__is_space_left():
            print(f"It's {self.__resolve_player_name()} turn. "
                  "Please select the available number from the above board.")

            selected_slot = input("Your Selection: ")
            is_selection_valid = self.__handle_selection(selected_slot)
            while not is_selection_valid:
                sleep(2)
                selected_slot = input("Please re-select: ")
                is_selection_valid = self.__handle_selection(selected_slot)

            self.__record_move(int(selected_slot))
            if not self.__is_game_over():  # if game is not over
                # flip the player
                self.__is_player_1s_turn = not self.__is_player_1s_turn
            else:
                # we have a winner; hence can't continue
                self.__is_player_1_winner = self.__is_player_1s_turn
                can_continue = False

            self.display_board()
        return

    def declare_winner(self):
        if self.__is_player_1_winner is None:
            print("Ahh! It's Tie!")
        else:
            name = "Player 1" if self.__is_player_1s_turn \
                else ("Computer" if self.__playing_against_computer else "Player 2")

            print(f"{name} is winner! Hooray!")
        return

    def __get_symbol(self) -> str:
        return CROSS if self.__is_player_1s_turn else OH

    def __resolve_player_name(self) -> str:
        return "Player 1" if self.__is_player_1s_turn \
            else ("Computer" if self.__playing_against_computer else "Player 2")

    def __is_game_over(self) -> bool:
        """
        Check if the symbol on any of these matches with the current player...?
            rows :: 1 = 0,1,2 ; 2 = 3,4,5 ; 3 = 6,7,8
            cols :: 1 = 0,3,6 ; 2 = 1,4,7 ; 3 = 2,5,8
            diag :: 1 = 0,4,8 ; 2 = 2,4,6

        if yes then current player is the winner
        """
        symbol = self.__get_symbol()
        return all(i == symbol for i in self.__board[0:3]) or \
               all(i == symbol for i in self.__board[3:6]) or \
               all(i == symbol for i in self.__board[6:8]) or \
               all(i == symbol for i in (self.__board[0], self.__board[3], self.__board[6])) or \
               all(i == symbol for i in (self.__board[1], self.__board[4], self.__board[7])) or \
               all(i == symbol for i in (self.__board[2], self.__board[5], self.__board[8])) or \
               all(i == symbol for i in (self.__board[0], self.__board[4], self.__board[8])) or \
               all(i == symbol for i in (self.__board[2], self.__board[4], self.__board[6]))

    def __is_space_left(self) -> bool:
        spaces = filter(lambda x: x not in (CROSS, OH), self.__board)
        return len(list(spaces)) != 0

    def __handle_selection(self, slot: str) -> bool:
        if not slot.isdigit():
            print("\nErr! Invalid input. Only digits from 1-9 (if available) are allowed to be selected.")
            return False

        slot_num = int(slot)
        if slot_num < 1 or slot_num > 9:
            print("\nErr! Invalid Input. Only digits from 1-9 (if available) are allowed to be selected.")
            return False

        if self.__board[slot_num - 1] in (CROSS, OH):
            print("\nErr! Invalid Input. The slot is not available.")
            return False

        return True

    def __record_move(self, slot: int):
        self.__board[slot - 1] = self.__get_symbol()
        return

    def get_state(self):
        return {
            "board": self.__board,
            "active_player": self.__resolve_player_name(),
            "is_player_1_winner": self.__is_player_1_winner
        }
