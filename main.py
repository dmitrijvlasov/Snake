import pygame
import sys
import random
import helper_functions

pygame.init()

SNAKE_SIZE = 20
APPLE_SIZE = 15
GREEN = 0, 255, 0  # Color of apple
BLUE = 52, 137, 255  # Color of display
RED = 255, 0, 0  # Color of snake (square)
FPS = 30
SPEED_X = 3
SPEED_Y = 3

size = SCREEN_WIDTH, SCREEN_HEIGHT = 320, 240  # size of display
# give coordinates to snake
snake = pygame.Rect((SCREEN_WIDTH//2) - (SNAKE_SIZE//2), (SCREEN_HEIGHT//2) - (SNAKE_SIZE//2), SNAKE_SIZE, SNAKE_SIZE)
# give coordinates to apple
apple = pygame.Rect(random.randint(0, (SCREEN_WIDTH - APPLE_SIZE)), random.randint(0, (SCREEN_HEIGHT - APPLE_SIZE)),
                    APPLE_SIZE, APPLE_SIZE)
move = False  # move by default set to False
direction = 0, 0  # direction by default set to 0
apple_color = GREEN

screen = pygame.display.set_mode(size)  # create window

while True:  # loop
    screen.fill(BLUE)  # background
    pygame.draw.rect(screen, RED, snake)  # create a square
    pygame.draw.rect(screen, apple_color, apple)  # apple
    pygame.display.flip()  # update screen

    for event in pygame.event.get():  # get the list of events
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
            direction = (0, SPEED_Y)

    if move is True:
        snake.move_ip(direction[0], direction[1])   # move_ip(0, 0) make snake move

    # function is equals to variable
    apple_detected = helper_functions.is_point_in_snake(snake, apple.x, apple.y)
    if apple_detected:
        # give to apple random color after hit
        apple_color = helper_functions.get_random_color()
        # give to apple random position after hit
        new_position = helper_functions.get_random_position(0, SCREEN_WIDTH - APPLE_SIZE, 0, SCREEN_HEIGHT - APPLE_SIZE)
        apple.x = new_position[0]  # set position coordinates
        apple.y = new_position[1]  # set position coordinates
    apple_detected = helper_functions.is_point_in_snake(snake, apple.x + apple.width, apple.y)
    if apple_detected:
        apple_color = helper_functions.get_random_color()
        new_position = helper_functions.get_random_position(0, SCREEN_WIDTH - APPLE_SIZE, 0, SCREEN_HEIGHT - APPLE_SIZE)
        apple.x = new_position[0]
        apple.y = new_position[1]
    apple_detected = helper_functions.is_point_in_snake(snake, apple.x, apple.y + apple.height)
    if apple_detected:
        apple_color = helper_functions.get_random_color()
        new_position = helper_functions.get_random_position(0, SCREEN_WIDTH - APPLE_SIZE, 0, SCREEN_HEIGHT - APPLE_SIZE)
        apple.x = new_position[0]
        apple.y = new_position[1]
    apple_detected = helper_functions.is_point_in_snake(snake, apple.x + apple.width, apple.y + apple.height)
    if apple_detected:
        apple_color = helper_functions.get_random_color()
        new_position = helper_functions.get_random_position(0, SCREEN_WIDTH - APPLE_SIZE, 0, SCREEN_HEIGHT - APPLE_SIZE)
        apple.x = new_position[0]
        apple.y = new_position[1]

    if snake.x >= SCREEN_WIDTH:  # if snake hits the wall, then
        snake_new_position = helper_functions.get_normal_position(1 - snake.width, snake.y)
        snake.x = snake_new_position[0]
        snake.y = snake_new_position[1]
    if snake.x + snake.width <= 0:
        snake_new_position = helper_functions.get_normal_position(SCREEN_WIDTH, snake.y)
        snake.x = snake_new_position[0]
        snake.y = snake_new_position[1]
    if snake.y >= SCREEN_HEIGHT:
        snake_new_position = helper_functions.get_normal_position(snake.x, 1 - snake.height)
        snake.x = snake_new_position[0]
        snake.y = snake_new_position[1]
    if snake.y + snake.height <= 0:
        snake_new_position = helper_functions.get_normal_position(snake.x, SCREEN_HEIGHT)
        snake.x = snake_new_position[0]
        snake.y = snake_new_position[1]

    pygame.time.Clock().tick(FPS)  # refresh page per sec
