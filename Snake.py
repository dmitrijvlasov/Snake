import pygame
import sys
import random
import helper_functions
pygame.init()

SNAKE_SIZE = 10
APPLE_SIZE = 10
GREEN = 0, 255, 0  # Color of apple
BLUE = 52, 137, 255  # Color of display
RED = 255, 0, 0  # Color of snake (square)
FPS = 120
WINDOW_SIZE = WIDTH, HEIGHT = 400, 400
MOVE = MOVE_X = MOVE_Y = 1
snake = []
for index in range(0, 100):
    new_part = pygame.Rect((WIDTH//2 + (MOVE*index)), HEIGHT//2, SNAKE_SIZE, SNAKE_SIZE)
    snake.append(new_part)
apple = pygame.Rect(random.randint(0, (WIDTH - APPLE_SIZE)), random.randint(0, (HEIGHT - APPLE_SIZE)),
                    APPLE_SIZE, APPLE_SIZE)
snake_color = GREEN
apple_color = GREEN
move = False
direction = 0, 0

screen = pygame.display.set_mode(WINDOW_SIZE)

while True:  # loop
    screen.fill(BLUE)  # background
    pygame.draw.rect(screen, apple_color, apple)  # apple

    for snake_part in snake:
        pygame.draw.rect(screen, snake_color, snake_part)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            move = True
            direction = -MOVE_X, 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            move = True
            direction = MOVE_X, 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            move = True
            direction = 0, -MOVE_Y
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            move = True
            direction = 0, MOVE_Y

    if move is True:
        for number in reversed(range(0, len(snake))):
            if number == 0:
                snake[number].move_ip(direction[0], direction[1])
            else:
                part_before = snake[number-1]
                snake[number].x = part_before.x
                snake[number].y = part_before.y

    # function is equals to variable
    apple_detected = helper_functions.is_point_in_snake(snake[0], apple.x, apple.y)
    if apple_detected:
        # give to apple random color after hit
        apple_color = helper_functions.get_random_color()
        # give to apple random position after hit
        new_position = helper_functions.get_random_position(0, WIDTH - APPLE_SIZE, 0, HEIGHT - APPLE_SIZE)
        apple.x = new_position[0]  # set position coordinates
        apple.y = new_position[1]  # set position coordinates
    apple_detected = helper_functions.is_point_in_snake(snake[0], apple.x + apple.width, apple.y)
    if apple_detected:
        apple_color = helper_functions.get_random_color()
        new_position = helper_functions.get_random_position(0, WIDTH - APPLE_SIZE, 0, HEIGHT - APPLE_SIZE)
        apple.x = new_position[0]
        apple.y = new_position[1]
    apple_detected = helper_functions.is_point_in_snake(snake[0], apple.x, apple.y + apple.height)
    if apple_detected:
        apple_color = helper_functions.get_random_color()
        new_position = helper_functions.get_random_position(0, WIDTH - APPLE_SIZE, 0, HEIGHT - APPLE_SIZE)
        apple.x = new_position[0]
        apple.y = new_position[1]
    apple_detected = helper_functions.is_point_in_snake(snake[0], apple.x + apple.width, apple.y + apple.height)
    if apple_detected:
        apple_color = helper_functions.get_random_color()
        new_position = helper_functions.get_random_position(0, WIDTH - APPLE_SIZE, 0, HEIGHT - APPLE_SIZE)
        apple.x = new_position[0]
        apple.y = new_position[1]

    if snake[0].x >= WIDTH:  # if snake hits the wall, then
        snake_new_position = helper_functions.get_normal_position(1 - snake[0].width, snake[0].y)
        snake[0].x = snake_new_position[0]
        snake[0].y = snake_new_position[1]
    if snake[0].x + snake[0].width <= 0:
        snake_new_position = helper_functions.get_normal_position(WIDTH, snake[0].y)
        snake[0].x = snake_new_position[0]
        snake[0].y = snake_new_position[1]
    if snake[0].y >= HEIGHT:
        snake_new_position = helper_functions.get_normal_position(snake[0].x, 1 - snake[0].height)
        snake[0].x = snake_new_position[0]
        snake[0].y = snake_new_position[1]
    if snake[0].y + snake[0].height <= 0:
        snake_new_position = helper_functions.get_normal_position(snake[0].x, HEIGHT)
        snake[0].x = snake_new_position[0]
        snake[0].y = snake_new_position[1]

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)
