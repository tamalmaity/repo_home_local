import pygame
import os
from tkinter import *
from tkinter import messagebox


letter_X = pygame.image.load(os.path.join('letters', 'letter_X.png'))
letter_O = pygame.image.load(os.path.join('letters', 'letter_O.png'))

letter_X = pygame.transform.scale(letter_X, (100,100))
letter_O = pygame.transform.scale(letter_O, (100,100))


class Grid:
    def __init__(self):
        self.grid_lines = [((0,100), (300,100)),         # list of tuple of tuples for 4 lines we need
                           ((0,200), (300,200)),
                           ((100,0), (100,300)),
                           ((200,0), (200,300))]

        self.grid = [[0 for x in range (3)] for y in range (3)]

        self.valid_move = True

        self.game_over = False

        self.message = False
        self.message_index = -1

    def draw(self, win):
        for line in self.grid_lines:
            pygame.draw.line(win, (0,0,0), line[0], line[1], 2)

        for x in range (3):
            for y in range (3):
                if (self.get_cell_value(x,y) == "X"):
                    win.blit(letter_X, (x*100, y*100))
                elif (self.get_cell_value(x,y) == "O"):
                    win.blit(letter_O, (x*100, y*100))

    def grid_print(self):
        for row in self.grid:
            print(row)

    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value

    def get_mouse(self, x, y, player):
        if (self.get_cell_value(x,y) == 0):
            self.valid_move = True
            if player == "X":
                self.set_cell_value(x, y, "X")
            else:
                self.set_cell_value(x, y, "O")
            self.has_won(player)
        else:
            self.valid_move = False


    def has_won(self, player):
        self.won = False
        count = 0
        for y in range (3):
            for x in range (3):
                if (self.grid[x][y] == player): count+= 1
            if count == 3:
                self.won = True
                break
            else: count = 0

        if self.won == False:
            for y in range (3):
                for x in range (3):
                    if (self.grid[y][x] == player): count+= 1
                if count == 3:
                    self.won = True
                    break
                else: count = 0

        if (self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == player): self.won = True
        if (self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == player): self.won = True

        if self.won == True:
            print(player + ' has won!')
            self.game_over = True

            self.message = True
            self.message_index = 0

        if self.won == False and self.is_full() == True:
            self.game_over = True
            print('Match has ended in a draw!')

            self.message = True
            self.message_index = 1

            self.message_show(1, player)

    def is_full(self):
        for row in self.grid:
            for value in row:
                if value == 0:
                    return False
        return  True

    def clear_grid(self):
        for x in range(3):
            for y in range(3):
                self.grid[x][y] = 0


    def message_show(self, message_index, player):
        Tk().wm_withdraw()
        if message_index == 0:
            messagebox.showinfo('Match result', player + ' has won! Press SPACE to play again. Press ESC to quit')
        elif message_index == 1:
            messagebox.showinfo('Match result', 'Match has ended in a draw! Press SPACE to play again. Press ESC '
                                                'to quit')

        self.message = False

