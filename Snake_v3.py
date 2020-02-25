import pygame
import sys
import random
import helper_functions
pygame.init()

GREEN = 0, 128, 0
BLACK = 0, 0, 0
FPS = 30
SIZE = 10


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.apple = pygame.Rect((width // 2), (height // 2), SIZE, SIZE)
        self.apple_color = GREEN

    def run(self):
        size = self.width, self.height
        screen = pygame.display.set_mode(size)

        while True:
            screen.fill(BLACK)
            pygame.draw.rect(screen, self.apple_color, self.apple)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()
            pygame.time.Clock().tick(FPS)


game = Game(300, 300)
game.run()
