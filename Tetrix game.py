import pygame
pygame.init()
from tetrix_object import TetrixObject
from tiles import Tiles



red = (214, 32, 32)
orange = (214, 108, 32)
yellow = (215, 224, 34)
green = (12, 176, 18)
cyan = (41, 189, 230)
blue = (34, 91, 224)
purple = (124, 47, 212)
white = (255, 255, 255)
grey = (114, 121, 122)
black = (0, 0, 0)


window_width = 400
window_height = 500
size = (window_width, window_height)
screen = pygame.display.set_mode (size)


clock = pygame.time.Clock()




pygame.display.set_caption("Welcome to Tetrix")

'''
for i in range(tiles.height):
    for j in range(tiles.width):
        pygame.draw.rect(screen, white, [tiles.x + tiles.zoom * j, tiles.y + tiles.zoom * i, tiles.zoom, tiles.zoom],
                         1)
        if tiles.field[i][j] > 0:
            pygame.draw.rect(screen, cyan
            [tiles.x + tiles.zoom * j + 1, tiles.y + tiles.zoom * i + 1, tiles.zoom - 2,
             tiles.zoom - 1])

'''
def draw_grid(tiles):
    for i in range(tiles.height):
        for j in range(tiles.width):
            pygame.draw.rect(screen, grey, [tiles.x + tiles.zoom * j, tiles.y + tiles.zoom * i, tiles.zoom, tiles.zoom],
                             1)
            if tiles.field[i][j] > 0:
                pygame.draw.rect(screen, cyan
                                 [tiles.x + tiles.zoom * j + 1, tiles.y + tiles.zoom * i + 1, tiles.zoom - 2,
                                  tiles.zoom - 1])

is_running = True

tiles = TetrixObject(20, 10)

pressing_down = False
counter = 0
fps = 25

while is_running is True:
    if tiles.tile is None:
        tiles.new_tile()
    counter+=1
    if counter > 100000:
        counter = 0
    if counter%(fps//tiles.level//2)==0 or pressing_down:
        if tiles.state == "start":
            tiles.gravity()
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            tiles.rotate()
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.MOUSEBUTTONDOWN:
                tiles.rotate()
            if event.key == pygame.K_a:
                tiles.side_movement(-1)
            if event.key == pygame.K_d:
                tiles.side_movement(1)
            if event.key == pygame.QUIT:
                is_running = False
            if event.key == pygame.K_s:
                pressing_down = True
                tiles.y_movement(1)
    screen.fill(white)

    for i in range(tiles.height):
        for j in range(tiles.width):
            pygame.draw.rect(screen, grey, [tiles.x + tiles.zoom * j, tiles.y + tiles.zoom * i, tiles.zoom, tiles.zoom],
                             1)
            if tiles.field[i][j] > 0:
                pygame.draw.rect(screen, cyan
                [tiles.x + tiles.zoom * j + 1, tiles.y + tiles.zoom * i + 1, tiles.zoom - 2,
                 tiles.zoom - 1])
    if tiles.tile is not None:

        for a in range (4):
            for b in range(4):
                p = a*4+b
                if p in tiles.tile.image():
                    pygame.draw.rect(screen, blue, [tiles.x + tiles.zoom * (b + tiles.tile.x) + 1,
                     tiles.y + tiles.zoom * (a + tiles.tile.y) + 1,
                     tiles.zoom - 2, tiles.zoom - 2])






    pygame.display.flip()
    clock.tick(fps)



block_grid = [[0,  1,  2,  3,  4,  5,  6,  7],
             [8,   9, 10, 11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20, 21, 22, 23],
             [24, 25, 26, 27, 28, 29, 30, 31],
             [32, 33, 34, 35, 36, 37, 38, 39],
             [40, 41, 42, 43, 44, 45, 46, 47],
             [48, 49, 50, 51, 52, 53, 54, 55],
             [56, 57, 58, 59, 60, 61, 62, 63]]

#0 1 2 3
#4 5 6 7
#8 9 10 11
#12 13 14 15


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




