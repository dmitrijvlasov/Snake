import pygame
import sys
pygame.init()

BLACK = 0, 0, 0
GREEN = 80, 220, 100
SNAKE_SIZE = 10
FPS = 20
WINDOW_SIZE = WIDTH, HEIGHT = 400, 400
MOVE_X = 10
MOVE_Y = 10
snake[0] = pygame.Rect(WIDTH//2, HEIGHT//2, SNAKE_SIZE, SNAKE_SIZE)
snake_body = pygame.Rect((WIDTH//2 + SNAKE_SIZE), HEIGHT//2, SNAKE_SIZE, SNAKE_SIZE)
snake_tail = pygame.Rect((WIDTH//2 + (SNAKE_SIZE*2)), HEIGHT//2, SNAKE_SIZE, SNAKE_SIZE)
snake_color = GREEN
move = False
direction = 0, 0

snake = [snake[0], snake_body, snake_tail]

screen = pygame.display.set_mode(WINDOW_SIZE)

while True:
    screen.fill(BLACK)
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
    print(snake)

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)
