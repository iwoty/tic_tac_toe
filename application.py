
from board import Board
from space import Space
import random
import os


class Application:
    menu_choice_option = ['Press 0 to exit']

    clean_board = ['╔═══╦═══╦═══╗',
                   '║ 7 ║ 8 ║ 9 ║',
                   '╠═══╬═══╬═══╣',
                   '║ 4 ║ 5 ║ 6 ║',
                   '╠═══╬═══╬═══╣',
                   '║ 1 ║ 2 ║ 3 ║',
                   '╚═══╩═══╩═══╝']

    POSSIBLE_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self):
        self.is_running = True

    def run(self):
        # os.system('clear')
        board = Board()

        while self.is_running:
            os.system('clear')

            # if len(self.POSSIBLE_SPACES) < 1:
            #     print('The board is full')
            #     self.is_running = False

            self.display_clean_board()
            print(board)
            self.display_menu()

            choice_option = self.get_input('Your mark is -> O <- by default.\n Where do you want put your mark? (1-9 without already marked): ')

            if choice_option in self.POSSIBLE_SPACES:
                self.POSSIBLE_SPACES.remove(choice_option)  # remove space from possible spaces
                board.todo_quarters[choice_option].set_player_mark()

                # if board.check_if_win() is True:
                #     print('Win')

                """AI TURN"""
                AI_choice = random.choice(self.POSSIBLE_SPACES)
                self.POSSIBLE_SPACES.remove(AI_choice)
                board.todo_quarters[AI_choice].set_AI_mark()

            elif choice_option == '0':
                self.is_running = False

    def get_input(self, message):
        return input(message)

    def display_menu(self):
        print('\n'.join(self.menu_choice_option))

    def display_clean_board(self):
        print('\n'.join(self.clean_board))
