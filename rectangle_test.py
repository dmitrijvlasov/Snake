import pygame
import sys

pygame.init()

SIZE = WIDTH, HEIGHT = 300, 300
RECT = 20
BLACK = 0, 0, 0
WHITE = 255, 255, 255
FPS = 30
MOVE_X = 1
MOVE_Y = 1

apple = pygame.Rect(WIDTH // 2, HEIGHT//2 - RECT - MOVE_Y, RECT, RECT)
# snake = pygame.Rect(WIDTH//2 + RECT*2, HEIGHT//2, RECT, RECT)
snake = []

for index in range(0, 3):
    new_part = pygame.Rect((WIDTH // 2) + (RECT * index), HEIGHT // 2, RECT, RECT)
    snake.append(new_part)

screen = pygame.display.set_mode(SIZE)

while True:
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, apple)

    for snake_part in snake:
        pygame.draw.rect(screen, WHITE, snake_part)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            snake.move_ip(-MOVE_X, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            snake.move_ip(MOVE_X, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            snake.move_ip(0, -MOVE_Y)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            snake.move_ip(0, MOVE_Y)

    print(snake, apple)

    if apple.collidelist(snake):
        print("Collision!!!")

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)
