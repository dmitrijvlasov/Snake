import pygame
import sys
import random
pygame.init()
FPS = 60
BLACK = 255, 255, 255


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = self.width, self.height
        self.IMAGE_SIZE = self.I_WIDTH, self.I_HEIGHT = 30, 30
        self.SPEED_X, self.SPEED_Y = 3, 3
        self.direction = [self.SPEED_X, self.SPEED_Y]

        # Create screen surface with size (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.size)

        # Load image into apple variable
        self.apple = pygame.image.load("knowledge_graph_logo.png")
        self.apple2 = pygame.image.load("RedApple_1.png")
        # Update apple variable with new smaller image
        self.apple = pygame.transform.scale(self.apple, self.IMAGE_SIZE)
        self.apple2 = pygame.transform.scale(self.apple2, self.IMAGE_SIZE)
        # get apple's rectangle
        self.apple_rect = self.apple.get_rect()
        self.apple_rect2 = self.apple2.get_rect()

        self.flipped_apple = pygame.transform.flip(self.apple, False, False)
        self.flipped_apple2 = pygame.transform.flip(self.apple2, False, False)

        # resize generated apple rectangle
        self.apple_rect.center = (width // 2, height // 2)
        self.apple_rect2.center = (width // 2, height // 2)

    def apple_1(self):
        if self.apple_rect.x <= 0:
            self.direction = self.direction[0], self.direction[1]
            print(self.direction)
            self.flipped_apple = pygame.transform.flip(self.apple, True, False)
        if self.apple_rect.x + self.apple_rect.width >= self.width:
            self.direction = -self.direction[0], self.direction[1]
            print(self.direction)
            self.flipped_apple = pygame.transform.flip(self.apple, True, False)
        if self.apple_rect.y <= 0:
            self.direction = self.direction[0], self.direction[1]
            print(self.direction)
            self.flipped_apple = pygame.transform.flip(self.apple, True, False)
        if self.apple_rect.y + self.apple_rect.height >= self.height:
            self.direction = self.direction[0], -self.direction[1]
            print(self.direction)
            self.flipped_apple = pygame.transform.flip(self.apple, True, True)

    def apple_2(self):
        if self.apple_rect2.x <= 0:
            self.direction = random.randint(1, 10), self.direction[1]
            print(self.direction)
            self.flipped_apple2 = pygame.transform.flip(self.apple2, False, False)
        if self.apple_rect2.x + self.apple_rect.width >= self.width:
            self.direction = -random.randint(1, 10), self.direction[1]
            print(self.direction)
            self.flipped_apple2 = pygame.transform.flip(self.apple2, False, False)
        if self.apple_rect2.y <= 0:
            self.direction = self.direction[0], random.randint(1, 10)
            print(self.direction)
            self.flipped_apple2 = pygame.transform.flip(self.apple2, False, False)
        if self.apple_rect2.y + self.apple_rect.height >= self.height:
            self.direction = self.direction[0], -random.randint(1, 10)
            print(self.direction)
            self.flipped_apple2 = pygame.transform.flip(self.apple2, False, False)

    def run(self):
        while True:
            self.screen.fill(BLACK)
            self.screen.blit(self.flipped_apple, self.apple_rect)
            self.screen.blit(self.flipped_apple2, self.apple_rect2)

            self.apple_1()
            # self.apple_2()

            self.apple_rect.move_ip(self.direction)
            # self.apple_rect2.move_ip(self.direction)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()
            pygame.time.Clock().tick(FPS)


game = Game(800, 600)
game.run()

