
class Space:
    def __init__(self):
        self.is_marked = False
        self.is_player = False
        self.is_AI = False

    def return_sign(self):
        if self.is_marked is False and self.is_player is False and self.is_AI is False:
            return 'N'
        elif self.is_marked is True and self.is_player is True and self.is_AI is False:
            return 'O'
        elif self.is_marked is True and self.is_player is False and self.is_AI is True:
            return 'X'

    def set_player_mark(self):
        self.is_marked = True
        self.is_player = True

    def set_AI_mark(self):
        self.is_marked = True
        self.is_AI = True
