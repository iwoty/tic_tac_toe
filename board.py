
from space import Space


class Board:

    def __init__(self):
        self.todo_quarters = {'1': Space(),
                              '2': Space(),
                              '3': Space(),
                              '4': Space(),
                              '5': Space(),
                              '6': Space(),
                              '7': Space(),
                              '8': Space(),
                              '9': Space()}

    # def check_if_win(self):
    #     if (self.todo_quarters['1'].is_player() is True and
    #         self.todo_quarters['2'].is_player() is True and
    #         self.todo_quarters['3'].is_player() is True):
    #         return True

    def __str__(self):
        mark1 = self.todo_quarters['1'].return_sign()
        mark2 = self.todo_quarters['2'].return_sign()
        mark3 = self.todo_quarters['3'].return_sign()
        mark4 = self.todo_quarters['4'].return_sign()
        mark5 = self.todo_quarters['5'].return_sign()
        mark6 = self.todo_quarters['6'].return_sign()
        mark7 = self.todo_quarters['7'].return_sign()
        mark8 = self.todo_quarters['8'].return_sign()
        mark9 = self.todo_quarters['9'].return_sign()

        view_board = ['╔═══╦═══╦═══╗']
        view_board.append('║ {} ║ {} ║ {} ║'.format(mark7, mark8, mark9))
        view_board.append('╠═══╬═══╬═══╣')
        view_board.append('║ {} ║ {} ║ {} ║'.format(mark4, mark5, mark6))
        view_board.append('╠═══╬═══╬═══╣')
        view_board.append('║ {} ║ {} ║ {} ║'.format(mark1, mark2, mark3))
        view_board.append('╚═══╩═══╩═══╝')

        return '\n'.join(view_board)

    """
    ╔═══╦═══╦═══╗
    ║ 7 ║ 8 ║ 9 ║
    ╠═══╬═══╬═══╣
    ║ 4 ║ 5 ║ 6 ║
    ╠═══╬═══╬═══╣
    ║ 1 ║ 2 ║ 3 ║
    ╚═══╩═══╩═══╝
    """
