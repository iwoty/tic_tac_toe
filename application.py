
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

    WIN_POSSIBILITIES = [['1', '2', '3'],
                         ['4', '5', '6'],
                         ['7', '8', '9'],
                         ['1', '4', '7'],
                         ['2', '5', '8'],
                         ['3', '6', '9'],
                         ['7', '5', '3'],
                         ['1', '5', '9']]
    PLAYER_SPACES = []
    AI_SPACES = []

    def __init__(self):
        self.is_game_over = False

    def run(self):
        os.system('clear')
        board = Board()

        while not self.is_game_over:
            os.system('clear')

            self.display_clean_board()
            print(board)
            self.display_menu()

            choice_option = self.get_input('Your mark is -> O <- by default.\n Where do you want put your mark? (1-9 without already marked): ')

            if choice_option in self.POSSIBLE_SPACES:
                self.POSSIBLE_SPACES.remove(choice_option)  # remove space from possible spaces
                board.todo_quarters[choice_option].set_player_mark()
                self.PLAYER_SPACES.append(choice_option)

                for element in self.WIN_POSSIBILITIES:
                    if set(element).issubset(self.PLAYER_SPACES):
                        print("Congratz, You Win!")
                        self.game_over = True
                        print(board)
                        return self.game_over

                """AI TURN"""
                AI_choice = random.choice(self.POSSIBLE_SPACES)
                self.POSSIBLE_SPACES.remove(AI_choice)
                board.todo_quarters[AI_choice].set_AI_mark()
                self.AI_SPACES.append(choice_option)

                for element in self.WIN_POSSIBILITIES:
                    if set(element).issubset(self.AI_SPACES):
                        print("Sorry, You have lost!")
                        self.game_over = True
                        print(board)
                        return self.game_over

            elif choice_option == '0':
                self.is_game_over = True

    def get_input(self, message):
        return input(message)

    def display_menu(self):
        print('\n'.join(self.menu_choice_option))

    def display_clean_board(self):
        print('\n'.join(self.clean_board))
