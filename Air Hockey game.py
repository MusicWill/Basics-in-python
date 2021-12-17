import pygame
from paddle import Paddle
from puck import Puck

pygame.init()  # initalize pygame

# initializing our colors we want to use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (71, 142, 255)
RED = (250, 5, 5)


# create a window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Welcome to Air Hockey!")  # show name of game

paddleA = Paddle(RED, 80, 100)
paddleA.rect.x = -45
paddleA.rect.y = 200

paddleB = Paddle(RED, 80, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

puck = Puck(WHITE, 15, 15)
puck.rect.x = 345
puck.rect.y = 195

# list of sprites we will use in game
all_sprites_list = pygame.sprite.Group()
# add paddles to sprite list
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(puck)

# 1 events (key strokes)
# 2 logic of game (if the ball hits paddle, it moves - if ball misses paddle scores)
# 3 refreshing the screen

clock = pygame.time.Clock()

scoreA = 0
scoreB = 0






keepRunning = True
while keepRunning:
    # main event loop (keeps track of key strokes)
    for event in pygame.event.get():  # user did something
        if event.type == pygame.QUIT:
            keepRunning = False

    # User events for key strokes - paddle movement
    # player 1 w/s
    # player 2 up/down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

        # update the paddle info (like location)
    all_sprites_list.update()

    # check if ball is bouncing on the edge of the window
    if puck.rect.x >= 690:
        scoreA += 1
        puck.velocity[0] = -puck.velocity[0]
    if puck.rect.x <= 0:
        scoreB += 1
        puck.velocity[0] = -puck.velocity[0]

    if puck.rect.y >= 490:
        puck.velocity[1] = -puck.velocity[1]
    if puck.rect.y <= 0:
        puck.velocity[1] = -puck.velocity[1]

    if pygame.sprite.collide_mask(puck, paddleA) or pygame.sprite.collide_mask(puck, paddleB):
        puck.bounce()

    screen.fill(BLUE)
    # draw the line in the middle of the screen (net)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # draws sprites on the screen , updates thru out game
    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))

    # update the screen
    pygame.display.flip()

    # refresh clock 60 frames per second
    clock.tick(60)

pygame.quit()



