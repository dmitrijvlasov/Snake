import pygame
import sys
import random
import helper_functions
pygame.init()

GREEN = 0, 128, 0
BLACK = 0, 0, 0
BLUE = 52, 137, 255
FPS = 15


class Game:
    def __init__(self, width, height):
        self.SNAKE_SIZE = 10
        self.APPLE_SIZE = 10
        self.MOVE = self.MOVE_X = self.MOVE_Y = 11
        self.snake = []
        self.width = width
        self.height = height
        self.apple = pygame.Rect(random.randint(0, (width - self.APPLE_SIZE)),
                                 random.randint(0, (height - self.APPLE_SIZE)), self.APPLE_SIZE, self.APPLE_SIZE)
        self.snake_color = BLACK
        self.apple_color = GREEN
        self.move = False
        self.direction = 0, 0
        size = self.width, self.height
        self.screen = pygame.display.set_mode(size)
        for index in range(0, 10):
            self.new_part = pygame.Rect((self.width // 2 + (self.MOVE * index)), self.height // 2, self.SNAKE_SIZE,
                                        self.SNAKE_SIZE)
            self.snake.append(self.new_part)

    def draw_snake(self):
        for snake_part in self.snake:
            pygame.draw.rect(self.screen, self.snake_color, snake_part)

    def check_button_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.move = True
                self.direction = -self.MOVE_X, 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.move = True
                self.direction = self.MOVE_X, 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.move = True
                self.direction = 0, -self.MOVE_Y
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.move = True
                self.direction = 0, self.MOVE_Y

    def move_snake(self):
        for number in reversed(range(0, len(self.snake))):
            if number == 0:
                self.snake[number].move_ip(self.direction[0], self.direction[1])
            else:
                part_before = self.snake[number - 1]
                self.snake[number].x = part_before.x
                self.snake[number].y = part_before.y

    def detects_apple(self):
        apple_detected = helper_functions.is_point_in_snake(self.snake[0], self.apple.x, self.apple.y)
        if apple_detected:
            # give to apple random color after hit
            self.apple_color = helper_functions.get_random_color()
            # give to apple random position after hit
            new_position = helper_functions.get_random_position(0, self.width - self.APPLE_SIZE, 0,
                                                                self.height - self.APPLE_SIZE)
            self.apple.x = new_position[0]  # set position coordinates
            self.apple.y = new_position[1]  # set position coordinates
            for index in range(0, 1):
                snake_tail = self.snake[-1]
                tail_grow = pygame.Rect(snake_tail.x, snake_tail.y, self.SNAKE_SIZE, self.SNAKE_SIZE)
                self.snake.append(tail_grow)
        apple_detected = helper_functions.is_point_in_snake(self.snake[0], self.apple.x + self.apple.width,
                                                            self.apple.y)
        if apple_detected:
            self.apple_color = helper_functions.get_random_color()
            new_position = helper_functions.get_random_position(0, self.width - self.APPLE_SIZE, 0,
                                                                self.height - self.APPLE_SIZE)
            self.apple.x = new_position[0]
            self.apple.y = new_position[1]
            for index in range(0, 1):
                snake_tail = self.snake[-1]
                tail_grow = pygame.Rect(snake_tail.x, snake_tail.y, self.SNAKE_SIZE, self.SNAKE_SIZE)
                self.snake.append(tail_grow)
        apple_detected = helper_functions.is_point_in_snake(self.snake[0], self.apple.x, self.apple.y +
                                                            self.apple.height)
        if apple_detected:
            self.apple_color = helper_functions.get_random_color()
            new_position = helper_functions.get_random_position(0, self.width - self.APPLE_SIZE, 0,
                                                                self.height - self.APPLE_SIZE)
            self.apple.x = new_position[0]
            self.apple.y = new_position[1]
            for index in range(0, 1):
                snake_tail = self.snake[-1]
                tail_grow = pygame.Rect(snake_tail.x, snake_tail.y, self.SNAKE_SIZE, self.SNAKE_SIZE)
                self.snake.append(tail_grow)
        apple_detected = helper_functions.is_point_in_snake(self.snake[0], self.apple.x + self.apple.width, self.apple.y
                                                            + self.apple.height)
        if apple_detected:
            self.apple_color = helper_functions.get_random_color()
            new_position = helper_functions.get_random_position(0, self.width - self.APPLE_SIZE, 0,
                                                                self.height - self.APPLE_SIZE)
            self.apple.x = new_position[0]
            self.apple.y = new_position[1]
            for index in range(0, 1):
                snake_tail = self.snake[-1]
                tail_grow = pygame.Rect(snake_tail.x, snake_tail.y, self.SNAKE_SIZE, self.SNAKE_SIZE)
                self.snake.append(tail_grow)

    def trough_walls(self):
        if self.snake[0].x >= self.width:  # if snake hits the wall, then
            snake_new_position = helper_functions.get_normal_position(1 - self.snake[0].width, self.snake[0].y)
            self.snake[0].x = snake_new_position[0]
            self.snake[0].y = snake_new_position[1]
        if self.snake[0].x + self.snake[0].width <= 0:
            snake_new_position = helper_functions.get_normal_position(self.width, self.snake[0].y)
            self.snake[0].x = snake_new_position[0]
            self.snake[0].y = snake_new_position[1]
        if self.snake[0].y >= self.height:
            snake_new_position = helper_functions.get_normal_position(self.snake[0].x, 1 - self.snake[0].height)
            self.snake[0].x = snake_new_position[0]
            self.snake[0].y = snake_new_position[1]
        if self.snake[0].y + self.snake[0].height <= 0:
            snake_new_position = helper_functions.get_normal_position(self.snake[0].x, self.height)
            self.snake[0].x = snake_new_position[0]
            self.snake[0].y = snake_new_position[1]

    def snake_hit_it_self(self):
        snake_body = self.snake[1:]
        for snake_part in snake_body:
            snake_detected = helper_functions.is_point_in_snake(snake_part, self.snake[0].x, self.snake[0].y)
            if snake_detected:
                print("Game over")
                sys.exit()

        snake_body = self.snake[1:]
        for snake_part in snake_body:
            snake_detected = helper_functions.is_point_in_snake(snake_part, self.snake[0].x + self.snake[0].width,
                                                                self.snake[0].y)
            if snake_detected:
                print("Game over")
                sys.exit()

        snake_body = self.snake[1:]
        for snake_part in snake_body:
            snake_detected = helper_functions.is_point_in_snake(snake_part, self.snake[0].x, self.snake[0].y
                                                                + self.snake[0].height)
            if snake_detected:
                print("Game over")
                sys.exit()

        snake_body = self.snake[1:]
        for snake_part in snake_body:
            snake_detected = helper_functions.is_point_in_snake(snake_part, self.snake[0].x + self.snake[0].width,
                                                                self.snake[0].y + self.snake[0].height)
            if snake_detected:
                print("Game over")
                sys.exit()

    def run(self):

        while True:
            self.screen.fill(BLUE)
            pygame.draw.rect(self.screen, self.apple_color, self.apple)

            self.snake_hit_it_self()

            self.draw_snake()

            self.check_button_pressed()

            if self.move is True:
                self.move_snake()

            self.detects_apple()

            self.trough_walls()

            pygame.display.flip()
            pygame.time.Clock().tick(FPS)


game = Game(500, 500)
game.run()
