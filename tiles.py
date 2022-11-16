import pygame
import random

class Tiles:
    red = (214, 32, 32)
    orange = (214, 108, 32)
    yellow = (215, 224, 34)
    green = (12, 176, 18)
    cyan = (41, 189, 230)
    blue = (34, 91, 224)
    purple = (124, 47, 212)
    all_colors = red + orange + yellow + green + cyan + blue + purple

    tiny_t = [[1, 4, 5, 6],
             [1, 4, 5, 9],
             [9, 4, 5, 6],
             [6, 1, 5, 9]]

    short_i = [[0, 1, 2, 3],
              [0, 4, 8, 12]]

    tiny_square = [[0, 1, 4, 5]]

    l_shaped = [[0, 4, 8, 9],
            [1, 5, 9, 8],
            [4, 5, 6, 10],
            [6, 5, 4, 8]]

    all_tiles = []
    all_tiles.append(tiny_square)
    all_tiles.append(short_i)
    all_tiles.append(tiny_t)
    all_tiles.append(l_shaped)
    print(all_tiles)

    x = 0
    y = 0

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.all_tiles)-1)
        self.color = random.randint(0, len(self.all_colors)-1)
        self.rotation = 0

    def image(self):
        return self.all_tiles[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation +1)% len(self.all_tiles[self.type])