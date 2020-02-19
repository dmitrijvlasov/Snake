import pygame, sys
import random

pygame.init()

BOX_SIZE = 15
APPLE_SIZE = 20
size = SCREEN_WIDTH, SCREEN_HEIGHT = 320, 240  # size of display
box = pygame.Rect((SCREEN_WIDTH//2) - (BOX_SIZE//2), (SCREEN_HEIGHT//2) - (BOX_SIZE//2), BOX_SIZE, BOX_SIZE)  # give coordinates to square
apple = pygame.Rect(random.randint(0, (SCREEN_WIDTH - APPLE_SIZE)), random.randint(0, (SCREEN_HEIGHT - APPLE_SIZE)), APPLE_SIZE, APPLE_SIZE)
# apple = pygame.Rect(120, 80, APPLE_SIZE, APPLE_SIZE)
move = False  # move by default set to False
direction = 0, 0  # direction by default set to 0

BLUE = 0, 0, 255  # Color of display
RED = 255, 0, 0  # Color of box (square)
GREEN = 0, 255, 0 # Color of apple
FPS = 30
SPEED_X = 3
SPEED_Y = 3


def is_point_in_box(square: pygame.Rect, point_x, point_y):
    if square.x <= point_x <= square.x + square.width and square.y <= point_y <= square.y + square.height:
        return True
    else:
        return False


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

        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:  # if in the list there is RIGHT with button released
            move = True
            direction = (SPEED_X, 0)
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:  # if in the list there is LEFT with button released
            move = True
            direction = (-SPEED_X, 0)
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:  # if in the list there is UP with button released
            move = True
            direction = (0, -SPEED_Y)
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:  # if in the list there is DOWN with button released
            move = True  # move is True
            direction = (0, SPEED_Y)  # direction is down

    if move is True:
        box.move_ip(direction[0], direction[1])   # move_ip(0, 0)

    is_apple_detected = is_point_in_box(box, apple.x, apple.y)
    if is_apple_detected:
        quit()
    is_apple_detected = is_point_in_box(box, apple.x + apple.width, apple.y)
    if is_apple_detected:
        quit()
    is_apple_detected = is_point_in_box(box, apple.x, apple.y + apple.height)
    if is_apple_detected:
        quit()
    is_apple_detected = is_point_in_box(box, apple.x + apple.width, apple.y + apple.height)
    if is_apple_detected:
        quit()

    if box.x + box.width >= SCREEN_WIDTH:  # if box is more, then
        print("Game finito")
        sys.exit()
    if box.x <= 0:  # if box is more, then
        print("Game finito")
        sys.exit()
    if box.y + box.height >= SCREEN_HEIGHT:  # if box is more, then
        print("Game finito")
        sys.exit()
    if box.y <= 0:  # if box is more, then
        print("Game finito")
        sys.exit()

    pygame.time.Clock().tick(FPS)  # refresh page per sec
