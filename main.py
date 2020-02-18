import pygame, sys

pygame.init()

size = SCREEN_WIDTH, SCREEN_HEIGHT = 320, 240  # size of display
box = pygame.Rect(160, 120, 10, 10)  # give coordinates to square
move_right = False  # move right by default set to False
move_left = False
move_up = False
move_down = False

BLUE = 0, 0, 255  # Color of display
RED = 255, 0, 0  # Color of box (square or rectangle)
FPS = 30
SPEED_X = 5
SPEED_Y = 5

screen = pygame.display.set_mode(size)  # create window

while True:  # loop
    screen.fill(BLUE)  # background blue
    pygame.draw.rect(screen, RED, box)  # create a square
    pygame.display.flip()  # update screen

    for event in pygame.event.get():  # get the list of events
        print(event)
        if event.type == pygame.QUIT:  # if in the list there is event QUIT
            print("Breaking from loop")
            sys.exit()  # then close the window

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:  # if in the list there is RIGHT with button pressed
            move_right = True  # then its true
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:  # if in the list there is RIGHT with button released
            move_right = False # then its false

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:  # if in the list there is LEFT with button pressed
            move_left = True
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:  # if in the list there is LEFT with button released
            move_left = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:  # if in the list there is UP with button pressed
            move_up = True
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:  # if in the list there is UP with button released
            move_up = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:  # if in the list there is DOWN with button pressed
            move_down = True
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:  # if in the list there is DOWN with button released
            move_down = False

    if move_right is True and box.x + box.width < SCREEN_WIDTH:  # if conditions are met
        box.move_ip(SPEED_X, 0)  # then move square
        print("Moving right")

    if move_left is True and box.x > 0:
        box.move_ip(-SPEED_X, 0)  # then move square
        print("Moving left")

    if  move_up is True and box.y > 0:
        box.move_ip(0, -SPEED_Y)  # then move square
        print("Moving up")

    if  move_down is True and box.y + box.height < SCREEN_HEIGHT:
        box.move_ip(0, SPEED_Y)  # then move square
        print("Moving down")

    pygame.time.Clock().tick(FPS)
