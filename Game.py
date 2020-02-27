import pygame
import sys
import random
pygame.init()

SIZE = WIDTH, HEIGHT = 400, 400
IMAGE_SIZE = I_WIDTH, I_HEIGHT = 30, 30
BLACK = 255, 255, 255
SPEED_X, SPEED_Y = 3, 3
FPS = 60
direction = [SPEED_X, SPEED_Y]

# Create screen surface with size (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)

# Load image into apple variable
apple = pygame.image.load("knowledge_graph_logo.png")
# Update apple variable with new smaller image
apple = pygame.transform.scale(apple, IMAGE_SIZE)

# get apple's rectangle
apple_rect = apple.get_rect()

flipped_apple = pygame.transform.flip(apple, False, False)

# resize generated apple rectangle
apple_rect.center = (WIDTH // 2, HEIGHT // 2)

while True:
    screen.fill(BLACK)
    screen.blit(flipped_apple, apple_rect)

    if apple_rect.x <= 0:
        direction = random.randint(1, 5), direction[1]
        print(direction)
        flipped_apple = pygame.transform.flip(apple, True, False)
    if apple_rect.x + apple_rect.width >= WIDTH:
        direction = -random.randint(1, 5), direction[1]
        print(direction)
        flipped_apple = pygame.transform.flip(apple, True, False)
    if apple_rect.y <= 0:
        direction = direction[0], random.randint(1, 5)
        print(direction)
        flipped_apple = pygame.transform.flip(apple, True, False)
    if apple_rect.y + apple_rect.height >= HEIGHT:
        direction = direction[0], -random.randint(1, 5)
        print(direction)
        flipped_apple = pygame.transform.flip(apple, True, True)

    apple_rect.move_ip(direction)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)
