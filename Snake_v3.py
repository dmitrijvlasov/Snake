import pygame
import sys
import random
import helper_functions
pygame.init()

GREEN = 0, 128, 0
BLACK = 0, 0, 0
BLUE = 52, 137, 255
FPS = 120
SNAKE_SIZE = 10
APPLE_SIZE = 10
MOVE = MOVE_X = MOVE_Y = 2
snake = []


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.apple = pygame.Rect(random.randint(0, (width - APPLE_SIZE)), random.randint(0, (height - APPLE_SIZE)),
                                 APPLE_SIZE, APPLE_SIZE)
        self.snake_color = BLACK
        self.apple_color = GREEN
        self.move = False
        self.direction = 0, 0
        size = self.width, self.height
        self.screen = pygame.display.set_mode(size)
        for index in range(0, 100):
            self.new_part = pygame.Rect((self.width // 2 + (MOVE * index)), self.height // 2, SNAKE_SIZE, SNAKE_SIZE)
            snake.append(self.new_part)

    def draw_snake(self):
        for snake_part in snake:
            pygame.draw.rect(self.screen, self.snake_color, snake_part)

    def check_button_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.move = True
                self.direction = -MOVE_X, 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.move = True
                self.direction = MOVE_X, 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.move = True
                self.direction = 0, -MOVE_Y
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.move = True
                self.direction = 0, MOVE_Y

    def move_snake(self):
        for number in reversed(range(0, len(snake))):
            if number == 0:
                snake[number].move_ip(self.direction[0], self.direction[1])
            else:
                part_before = snake[number - 1]
                snake[number].x = part_before.x
                snake[number].y = part_before.y

    def detects_apple(self):
        apple_detected = helper_functions.is_point_in_snake(snake[0], self.apple.x, self.apple.y)
        if apple_detected:
            # give to apple random color after hit
            self.apple_color = helper_functions.get_random_color()
            # give to apple random position after hit
            new_position = helper_functions.get_random_position(0, self.width - APPLE_SIZE, 0,
                                                                self.height - APPLE_SIZE)
            self.apple.x = new_position[0]  # set position coordinates
            self.apple.y = new_position[1]  # set position coordinates
            for index in range(0, 10):
                snake_tail = snake[-1]
                tail_grow = pygame.Rect(snake_tail.x, snake_tail.y, SNAKE_SIZE, SNAKE_SIZE)
                snake.append(tail_grow)
        apple_detected = helper_functions.is_point_in_snake(snake[0], self.apple.x + self.apple.width, self.apple.y)
        if apple_detected:
            self.apple_color = helper_functions.get_random_color()
            new_position = helper_functions.get_random_position(0, self.width - APPLE_SIZE, 0,
                                                                self.height - APPLE_SIZE)
            self.apple.x = new_position[0]
            self.apple.y = new_position[1]
            for index in range(0, 10):
                snake_tail = snake[-1]
                tail_grow = pygame.Rect(snake_tail.x, snake_tail.y, SNAKE_SIZE, SNAKE_SIZE)
                snake.append(tail_grow)
        apple_detected = helper_functions.is_point_in_snake(snake[0], self.apple.x, self.apple.y +
                                                            self.apple.height)
        if apple_detected:
            self.apple_color = helper_functions.get_random_color()
            new_position = helper_functions.get_random_position(0, self.width - APPLE_SIZE, 0,
                                                                self.height - APPLE_SIZE)
            self.apple.x = new_position[0]
            self.apple.y = new_position[1]
            for index in range(0, 10):
                snake_tail = snake[-1]
                tail_grow = pygame.Rect(snake_tail.x, snake_tail.y, SNAKE_SIZE, SNAKE_SIZE)
                snake.append(tail_grow)
        apple_detected = helper_functions.is_point_in_snake(snake[0], self.apple.x + self.apple.width, self.apple.y
                                                            + self.apple.height)
        if apple_detected:
            self.apple_color = helper_functions.get_random_color()
            new_position = helper_functions.get_random_position(0, self.width - APPLE_SIZE, 0,
                                                                self.height - APPLE_SIZE)
            self.apple.x = new_position[0]
            self.apple.y = new_position[1]
            for index in range(0, 10):
                snake_tail = snake[-1]
                tail_grow = pygame.Rect(snake_tail.x, snake_tail.y, SNAKE_SIZE, SNAKE_SIZE)
                snake.append(tail_grow)

    def trough_walls(self):
        if snake[0].x >= self.width:  # if snake hits the wall, then
            snake_new_position = helper_functions.get_normal_position(1 - snake[0].width, snake[0].y)
            snake[0].x = snake_new_position[0]
            snake[0].y = snake_new_position[1]
        if snake[0].x + snake[0].width <= 0:
            snake_new_position = helper_functions.get_normal_position(self.width, snake[0].y)
            snake[0].x = snake_new_position[0]
            snake[0].y = snake_new_position[1]
        if snake[0].y >= self.height:
            snake_new_position = helper_functions.get_normal_position(snake[0].x, 1 - snake[0].height)
            snake[0].x = snake_new_position[0]
            snake[0].y = snake_new_position[1]
        if snake[0].y + snake[0].height <= 0:
            snake_new_position = helper_functions.get_normal_position(snake[0].x, self.height)
            snake[0].x = snake_new_position[0]
            snake[0].y = snake_new_position[1]
    #
    # def snake_hit_it_self(self):
    #     snake_body = snake[1:]
    #     for snake_part in snake_body:
    #         snake_detected = helper_functions.is_point_in_snake(snake_part, snake[0].x, snake[0].y)
    #         if snake_detected:
    #             print("Game over")
    #             sys.exit()

    def run(self):

        while True:
            self.screen.fill(BLUE)
            pygame.draw.rect(self.screen, self.apple_color, self.apple)

            self.draw_snake()

            self.check_button_pressed()

            if self.move is True:
                self.move_snake()

            self.detects_apple()

            self.trough_walls()

            # self.snake_hit_it_self()

            pygame.display.flip()
            pygame.time.Clock().tick(FPS)


game = Game(500, 500)
game.run()
