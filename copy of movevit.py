# import pygame module in this program
# you have to import pygame iniorder to use it to make a game and code in it.
import pygame

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
# I erased pygame.init() to see what would happen


# what does display.set_mode do?
# try googling "pygame display.set_mode"
# hint: https://www.pygame.org/docs/ref/display.html
# is it to set whether the screensaver may run or not?
# I changed the numbers to see what would happen.
win = pygame.display.set_mode((200, 200))

# what does set_caption do?
#set_caption sets the current window caption


# object current co-ordinates
x = 200
y = 200

# dimensions of the window
width = 500
height = 500

# velocity / speed of movement
vel = 10

# Indicates pygame is running
run = True

# what does image.load do with this gif or jpeg?
# it puts the image of your character
ball = pygame.image.load("moving-mario.gif")

# infinite loop
while run:
    # creates time delay of 10ms
    # try changing this and see what happens
    #it delays the time of running the project.
    #If the delay is 10 sec it means that it will take around 10 secs to pop up the screen.
    # If the delay is 1 sec it means that it will take around 1 sec to pop up the screen.
    pygame.time.delay(10)

    # what does event.get() do?
    # why do you think we have to loop through it?
    for event in pygame.event.get():

        # what is an event?
        if event.type == pygame.QUIT:
            # what is the point of making run False?
            run = False

    # what does key.get_pressed() do?
    # what does it return?
    #I think key.get_pressed makes it so that when you press a key it moves the cahracter
    keys = pygame.key.get_pressed()

    # what does pygame.K_LEFT mean?
    # why do we use those square brackets keys->[pygame.K_LEFT]<- ? (list)
    # why check if x > 0?
    #x has to be more than 0?
    # what happens if you take it out? and go allll the way left (keep clicking left arrow)
    if keys[pygame.K_LEFT]:
        # decrement in x co-ordinate
        x -= vel

    # why do we check if x<width-ball.get_width() ?
    #so we dont go all the way to the right
    # try taking it out
    if keys[pygame.K_RIGHT] and x < width - ball.get_width():
        # increment in x co-ordinate
        x += vel

# I took out the y > 0 things for the next few lines of code.
    # why check if y > 0? try taking it out
    if keys[pygame.K_UP]:
        # decrement in y co-ordinate
        y -= vel

    # why check if y < height-ball.get_height() ?
    # what happens if you take it out?
    #if i take it out I can scroll all the way down without stopping.
    if keys[pygame.K_DOWN] and y < height - ball.get_height():
        # increment in y co-ordinate
        y += vel

    # completely fill the surface object
    # with black colour
    # colors are filled using RGB values
    #pick your color here https://g.co/kgs/yPwruv
    win.fill((32, 40, 189))

    # what does blit() do?
    win.blit(ball, [x, y])
    # it refreshes the window
    pygame.display.update()

# closes the pygame window
#I took out pygame.quit() to see what would happen.