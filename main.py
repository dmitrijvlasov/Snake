import pygame, sys
import random

pygame.init()

BOX_SIZE = 15
APPLE_SIZE = 20
size = SCREEN_WIDTH, SCREEN_HEIGHT = 320, 240  # size of display
box = pygame.Rect((SCREEN_WIDTH//2) - (BOX_SIZE//2), (SCREEN_HEIGHT//2) - (BOX_SIZE//2), BOX_SIZE, BOX_SIZE)  # give coordinates to square
apple = pygame.Rect(random.randint(0, (SCREEN_WIDTH - APPLE_SIZE)), random.randint(0, (SCREEN_HEIGHT - APPLE_SIZE)), APPLE_SIZE, APPLE_SIZE)
# apple = pygame.Rect(120, 80, APPLE_SIZE, APPLE_SIZE)
move_right = False  # move right by default set to False
move_left = False
move_up = False
move_down = False

BLUE = 0, 0, 255  # Color of display
RED = 255, 0, 0  # Color of box (square)
GREEN = 0, 255, 0 # Color of apple
FPS = 30
SPEED_X = 5
SPEED_Y = 5

screen = pygame.display.set_mode(size)  # create window

while True:  # loop
    screen.fill(BLUE)  # background blue
    pygame.draw.rect(screen, RED, box)  # create a square
    pygame.draw.rect(screen, GREEN, apple)  # apple
    pygame.display.flip()  # update screen

    for event in pygame.event.get():  # get the list of events
        print(event)
        if event.type == pygame.QUIT:  # if in the list there is event QUIT
            print("Breaking from loop")
            sys.exit()  # then close the window

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:  # if in the list there is RIGHT with button pressed
            move_right = True  # then its true
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:  # if in the list there is RIGHT with button released
            move_right = False  # then its false

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

    if move_right is True:  # and box.x + box.width < SCREEN_WIDTH:  # if moving is true and box is less then screen
        if box.x + box.width >= apple.x > box.x and \
             box.y <= apple.y + apple.height and \
             box.y + box.height >= apple.y:
            print("game end")
            sys.exit()
        box.move_ip(SPEED_X, 0)  # then move square
        print("Moving right")

    if move_left is True:  # and box.x > 0:
        if box.x <= apple.x + apple.width < box.x + box.width and \
             box.y <= apple.y + apple.height and \
             box.y + box.height >= apple.y:
            print("game end")
            sys.exit()
        box.move_ip(-SPEED_X, 0)  # then move square
        print("Moving left")

    if move_up is True:  # and box.y > 0:
        if box.y <= apple.y + apple.height and \
             box.x <= apple.x + apple.width and \
             box.x + box.width >= apple.x:
            print("game end")
            sys.exit()
        box.move_ip(0, -SPEED_Y)  # then move square
        print("Moving up")

    if move_down is True:  # and box.y + box.height < SCREEN_HEIGHT:
        if box.y + box.height >= apple.y and \
             box.x <= apple.x + apple.width and \
             box.x + box.width >= apple.x:
            print("game end")
            sys.exit()
        box.move_ip(0, SPEED_Y)  # then move square
        print("Moving down")

    if box.x + box.width >= SCREEN_WIDTH:  # if box is more then
        print("Game finito")
        sys.exit()
    if box.x <= 0:  # if box is more then
        print("Game finito")
        sys.exit()
    if box.y + box.height >= SCREEN_HEIGHT:  # if box is more then
        print("Game finito")
        sys.exit()
    if box.y <= 0:  # if box is more then
        print("Game finito")
        sys.exit()

    pygame.time.Clock().tick(FPS)  # refresh page per sec
