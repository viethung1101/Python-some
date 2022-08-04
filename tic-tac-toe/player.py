import math
import random


class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        square = ramdom.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter +'\'s turn. Input Move(0-9):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
            except ValueError:
                print('Invalid move. Try again!')
        return val