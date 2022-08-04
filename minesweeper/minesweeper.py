#!/usr/bin/env python3
import random
import re
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.dug = set() #if we dig at 00, then self.dug = {(0,0)}
        self.board = self.make_new_board() #plant the bomb
        self.assign_value_to_board()
    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        #plant the bomb
        boms_planted = 0
        while boms_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue
            board[row][col] = '*'
            boms_planted += 1
        return board
    def assign_value_to_board(self):
        for i in range(0, self.dim_size):
            for j in range(0, self.dim_size):
                if self.board[i][j] == '*':
                    continue
                else:
                    count_bombs = 0
                    for k in [-1, 0 , 1]:
                        for l in [-1, 0, 1]:
                            if i-k < 0 or i-k >= self.dim_size  or j-l < 0 or j-l >= self.dim_size:
                                count_bombs += 0
                            else:
                                if self.board[i-k][j-l] == '*':
                                    count_bombs += 1
                    self.board[i][j] = count_bombs
    def dig(self, row, col):
        self.dug.add((row, col))
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        for r in range(max(0, row -1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1,col+1)+1):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)
        return True
    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
                # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

def play(dim_size=10, num_bombs=10):
    #1. Create the board and plant the bombs
    board = Board(dim_size, num_bombs)
    #2. show the user the board and ask for where they want to dig
    #3. a.if location is a bomb, show game over message
    #   b. if location is not a bomb, dig recursively until each square is at least next to a bomb
    #4. repeat step 2 and 3ab until there are no more places to dig -> victory
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*',input("Where you would like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row<0 or row>=board.dim_size or col<0 or col >= dim_size:
            print("Invalid location. Try again!")
            continue
        safe = board.dig(row,col)
        if not safe:
            break
    if safe:
        print("COngrate!!!")
        print(board)
    else:
        print("Game Over!!")
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board )
if __name__ == '__main__':
    play()
