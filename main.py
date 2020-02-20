import pygame
import sys
import random

pygame.init()

ZEROINTENSITY = 0  # color range from
MAXINTENSITY = 255  # color range to
SNAKE_SIZE = 20
APPLE_SIZE = 15
GREEN = 0, 255, 0  # Color of apple
BLUE = 52, 137, 255  # Color of display
RED = 255, 0, 0  # Color of box (square)
FPS = 30
SPEED_X = 3
SPEED_Y = 3

size = SCREEN_WIDTH, SCREEN_HEIGHT = 320, 240  # size of display
box = pygame.Rect((SCREEN_WIDTH//2) - (SNAKE_SIZE//2), (SCREEN_HEIGHT//2) - (SNAKE_SIZE//2), SNAKE_SIZE, SNAKE_SIZE)  # give coordinates to square
apple = pygame.Rect(random.randint(0, (SCREEN_WIDTH - APPLE_SIZE)), random.randint(0, (SCREEN_HEIGHT - APPLE_SIZE)), APPLE_SIZE, APPLE_SIZE)
move = False  # move by default set to False
direction = 0, 0  # direction by default set to 0
apple_color = GREEN


def is_point_in_box(square: pygame.Rect, point_x, point_y):
    """
    Checks for if the snake hits the apple
    :param square: Snake in a form of rect
    :param point_x:
    :param point_y:
    :return: if the box point_x and point_y is
    """
    if square.x <= point_x <= square.x + square.width and square.y <= point_y <= square.y + square.height:
        return True
    else:
        return False


def get_random_color():
    """
    Gets random color for apple, each time, when snake hits the apple
    :return: Random color for each - red, green, blue
    """
    r = random.randint(ZEROINTENSITY, MAXINTENSITY)
    g = random.randint(ZEROINTENSITY, MAXINTENSITY)
    b = random.randint(ZEROINTENSITY, MAXINTENSITY)
    rn_color = r, g, b
    return rn_color


def get_random_position():
    """
    Gets random position for apple, each time, when snake hits the apple
    :return: Random x and y in screen range
    """
    rn_x = random.randint(0, SCREEN_WIDTH - APPLE_SIZE)
    rn_y = random.randint(0, SCREEN_HEIGHT - APPLE_SIZE)
    rn_position = rn_x, rn_y
    return rn_position


screen = pygame.display.set_mode(size)  # create window

while True:  # loop
    screen.fill(BLUE)  # background blue
    pygame.draw.rect(screen, RED, box)  # create a square
    pygame.draw.rect(screen, apple_color, apple)  # apple
    pygame.display.flip()  # update screen

    for event in pygame.event.get():  # get the list of events
        print(event)
        if event.type == pygame.QUIT:  # if in the list there is event QUIT
            print("Breaking from loop")
            sys.exit()  # then close the window

            # if the RIGHT button is in the list of events
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            move = True
            direction = (SPEED_X, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            move = True
            direction = (-SPEED_X, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            move = True
            direction = (0, -SPEED_Y)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            move = True  # move is True
            direction = (0, SPEED_Y)  # direction is down

    if move is True:
        box.move_ip(direction[0], direction[1])   # move_ip(0, 0) make box move

    apple_detected = is_point_in_box(box, apple.x, apple.y)  # function is equals to variable
    if apple_detected:
        apple_color = get_random_color()  # give to apple random color after hit
        new_position = get_random_position()  # give to apple random position after hit
        apple.x = new_position[0]  # set position coordinates
        apple.y = new_position[1]  # set position coordinates
    apple_detected = is_point_in_box(box, apple.x + apple.width, apple.y)
    if apple_detected:
        apple_color = get_random_color()
        new_position = get_random_position()
        apple.x = new_position[0]
        apple.y = new_position[1]
    apple_detected = is_point_in_box(box, apple.x, apple.y + apple.height)
    if apple_detected:
        apple_color = get_random_color()
        new_position = get_random_position()
        apple.x = new_position[0]
        apple.y = new_position[1]
    apple_detected = is_point_in_box(box, apple.x + apple.width, apple.y + apple.height)
    if apple_detected:
        apple_color = get_random_color()
        new_position = get_random_position()
        apple.x = new_position[0]
        apple.y = new_position[1]

    if box.x + box.width >= SCREEN_WIDTH:  # if box hits the wall, then
        print("Game Over, you hit the wall")
        sys.exit()  # close the game
    if box.x <= 0:
        print("Game Over, you hit the wall")
        sys.exit()
    if box.y + box.height >= SCREEN_HEIGHT:
        print("Game Over, you hit the wall")
        sys.exit()
    if box.y <= 0:
        print("Game Over, you hit the wall")
        sys.exit()

    pygame.time.Clock().tick(FPS)  # refresh page per sec
