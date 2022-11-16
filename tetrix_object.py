import pygame
import random
from tiles import Tiles

class TetrixObject:

    level = 2

    height = 0
    width = 0
    field = []
    tile = None
    x = 100
    y = 60
    zoom = 20
    state = "start"


    def __init__(self, x, y):
        self.field = []
        self.state ="start"
        self.height = x
        self.width = y
        for i in range (self.height):
            new_line = []

            for j in range (self.width):
                new_line.append(0)

            self.field.append(new_line)

    def new_tile(self):
        self.tile = Tiles(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.tile.image():
                    if i + self.tile.y > self.height - 1 or \
                            j + self.tile.x > self.width - 1 or \
                            j + self.tile.x < 0 or \
                            self.field[i + self.tile.y][j + self.tile.x] > 0:
                        intersection = True
        return intersection

    def rotate(self):
        old_rotation = self.tile.rotation
        self.tile.rotate()
        if self.intersects():
            self.tile.rotation = old_rotation

    def gravity(self):
        self.tile.y+=1
        if self. intersects():
            self.tile.y-=1
            self.freeze

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.tile.image():
                    self.field[i + self.tile.y][j + self.tile.x] = self.tile.color
        self.break_lines()
        self.new_tile()
        if self.intersects():
            self.state = "gameover"

    def new_tile(self):
        self.tile = Tiles(3, 0)

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2


    def side_movement(self, direction):
        print("hghgghfhghgghghgfdsdfghjklkjhgfdsaASDFGHJKasdfghjhgfdsdfghj")
        old_x = self.tile.x
        self.tile.x+=direction
        if self.intersects():
            self.tile.x = old_x


    def y_movement(self, direction):
        old_y = self.tile.y
        self.tile.y += direction
        if self.intersects():
            self.tile.y = old_y











