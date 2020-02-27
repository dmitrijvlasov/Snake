import pygame
import sys
import random
import helper_functions
pygame.init()

GREEN = 0, 128, 0
BLACK = 0, 0, 0
BLUE = 52, 137, 255
FPS = 10


class Game:
    def __init__(self, width, height):
        self.SNAKE_SIZE = 20
        self.APPLE_SIZE = 20
        self.MOVE = self.MOVE_X = self.MOVE_Y = 21
        self.snake = []
        self.snake_images = []
        self.width = width
        self.height = height
        # Load image into apple variable
        self.apple = pygame.image.load("RedApple_1.png")
        # Update apple variable with new smaller image
        self.apple = pygame.transform.scale(self.apple, (self.APPLE_SIZE, self.APPLE_SIZE))
        # get apple's rectangle
        self.apple_rect = self.apple.get_rect()
        self.apple_rect.center = random.randint(0, (width -
                                                    self.APPLE_SIZE)), random.randint(0, (height - self.APPLE_SIZE))
        self.snake_color = BLACK
        self.apple_color = GREEN
        self.move = False
        self.direction = 0, 0
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)
        self.snake_head = pygame.image.load("head.png")
        self.snake_head = pygame.transform.scale(self.snake_head, (self.SNAKE_SIZE, self.SNAKE_SIZE))
        self.flipped_snake_head = pygame.transform.rotate(self.snake_head, 0)
        self.snake_horizontal_body = pygame.image.load("body.png")
        self.snake_horizontal_body = pygame.transform.scale(self.snake_horizontal_body,
                                                            (self.SNAKE_SIZE, self.SNAKE_SIZE))
        self.snake_vertical_body = pygame.image.load("body_v.png")
        self.snake_vertical_body = pygame.transform.scale(self.snake_vertical_body,
                                                            (self.SNAKE_SIZE, self.SNAKE_SIZE))
        # self.flipped_snake_body = pygame.transform.rotate(self.snake_body, 0)
        self.snake_tail = pygame.image.load("tail.png")
        self.snake_tail = pygame.transform.scale(self.snake_tail, (self.SNAKE_SIZE, self.SNAKE_SIZE))
        self.flipped_snake_tail = pygame.transform.rotate(self.snake_tail, 0)

        # create snake elements
        for index in range(0, 10):
            self.new_part = pygame.Rect((self.width // 2 + (self.MOVE * index)), self.height // 2, self.SNAKE_SIZE,
                                        self.SNAKE_SIZE)
            self.snake.append(self.new_part)
            self.snake_images.append("Horizontal")

    def draw_snake(self):
        for index, snake_part in enumerate(self.snake):
            if index == 0:
                self.screen.blit(self.flipped_snake_head, snake_part)
            elif index == len(self.snake) - 1:
                self.screen.blit(self.flipped_snake_tail, snake_part)
            else:
                if self.snake_images[index] == "Horizontal":
                    self.screen.blit(self.snake_horizontal_body, snake_part)
                if self.snake_images[index] == "Vertical":
                    self.screen.blit(self.snake_vertical_body, snake_part)

    def check_button_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.move = True
                self.direction = -self.MOVE_X, 0
                self.flipped_snake_head = pygame.transform.rotate(self.snake_head, 0)
                self.flipped_snake_tail = pygame.transform.rotate(self.snake_tail, 0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.move = True
                self.direction = self.MOVE_X, 0
                self.flipped_snake_head = pygame.transform.rotate(self.snake_head, 180)
                self.flipped_snake_tail = pygame.transform.rotate(self.snake_tail, 180)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.move = True
                self.direction = 0, -self.MOVE_Y
                self.flipped_snake_head = pygame.transform.rotate(self.snake_head, 270)
                self.flipped_snake_tail = pygame.transform.rotate(self.snake_tail, 270)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.move = True
                self.direction = 0, self.MOVE_Y
                self.flipped_snake_head = pygame.transform.rotate(self.snake_head, 90)
                self.flipped_snake_tail = pygame.transform.rotate(self.snake_tail, 90)

    def move_snake(self):
        for number in reversed(range(0, len(self.snake))):
            if number == 0:
                self.snake[number].move_ip(self.direction[0], self.direction[1])
            else:
                part_before = self.snake[number - 1]

                if part_before.x != self.snake[number].x:
                    self.snake_images[number] = "Horizontal"
                    # print("Horizontal", self.snake[number])

                if part_before.y != self.snake[number].y:
                    self.snake_images[number] = "Vertical"
                    # print("vertical", self.snake[number])

                self.snake[number].x = part_before.x
                self.snake[number].y = part_before.y

    def detects_apple(self):
        apple_detected = helper_functions.is_point_in_snake(self.snake[0], self.apple_rect.x, self.apple_rect.y)
        if apple_detected:
            # give to apple random color after hit
            self.apple_color = helper_functions.get_random_color()
            # give to apple random position after hit
            new_position = helper_functions.get_random_position(0, self.width - self.APPLE_SIZE, 0,
                                                                self.height - self.APPLE_SIZE)
            self.apple_rect.x = new_position[0]  # set position coordinates
            self.apple_rect.y = new_position[1]  # set position coordinates
            for index in range(0, 1):
                snake_tail = self.snake[-1]
                tail_grow = pygame.Rect(snake_tail.x, snake_tail.y, self.SNAKE_SIZE, self.SNAKE_SIZE)
                self.snake.append(tail_grow)
                self.snake_images.append(self.snake_images[-1])
        apple_detected = helper_functions.is_point_in_snake(self.snake[0], self.apple_rect.x + self.apple_rect.width,
                                                            self.apple_rect.y)
        if apple_detected:
            self.apple_color = helper_functions.get_random_color()
            new_position = helper_functions.get_random_position(0, self.width - self.APPLE_SIZE, 0,
                                                                self.height - self.APPLE_SIZE)
            self.apple_rect.x = new_position[0]
            self.apple_rect.y = new_position[1]
            for index in range(0, 1):
                snake_tail = self.snake[-1]
                tail_grow = pygame.Rect(snake_tail.x, snake_tail.y, self.SNAKE_SIZE, self.SNAKE_SIZE)
                self.snake.append(tail_grow)
                self.snake_images.append(self.snake_images[-1])
        apple_detected = helper_functions.is_point_in_snake(self.snake[0], self.apple_rect.x, self.apple_rect.y +
                                                            self.apple_rect.height)
        if apple_detected:
            self.apple_color = helper_functions.get_random_color()
            new_position = helper_functions.get_random_position(0, self.width - self.APPLE_SIZE, 0,
                                                                self.height - self.APPLE_SIZE)
            self.apple_rect.x = new_position[0]
            self.apple_rect.y = new_position[1]
            for index in range(0, 1):
                snake_tail = self.snake[-1]
                tail_grow = pygame.Rect(snake_tail.x, snake_tail.y, self.SNAKE_SIZE, self.SNAKE_SIZE)
                self.snake.append(tail_grow)
                self.snake_images.append(self.snake_images[-1])
        apple_detected = helper_functions.is_point_in_snake(self.snake[0], self.apple_rect.x + self.apple_rect.width,
                                                            self.apple_rect.y + self.apple_rect.height)
        if apple_detected:
            self.apple_color = helper_functions.get_random_color()
            new_position = helper_functions.get_random_position(0, self.width - self.APPLE_SIZE, 0,
                                                                self.height - self.APPLE_SIZE)
            self.apple_rect.x = new_position[0]
            self.apple_rect.y = new_position[1]
            for index in range(0, 1):
                snake_tail = self.snake[-1]
                tail_grow = pygame.Rect(snake_tail.x, snake_tail.y, self.SNAKE_SIZE, self.SNAKE_SIZE)
                self.snake.append(tail_grow)
                self.snake_images.append(self.snake_images[-1])

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

        snake_body = self.snake[1:]
        for snake_part in snake_body:
            snake_detected = helper_functions.is_point_in_snake(snake_part, self.snake[0].x + self.snake[0].width,
                                                                self.snake[0].y)
            if snake_detected:
                print("Game over")

        snake_body = self.snake[1:]
        for snake_part in snake_body:
            snake_detected = helper_functions.is_point_in_snake(snake_part, self.snake[0].x, self.snake[0].y
                                                                + self.snake[0].height)
            if snake_detected:
                print("Game over")

        snake_body = self.snake[1:]
        for snake_part in snake_body:
            snake_detected = helper_functions.is_point_in_snake(snake_part, self.snake[0].x + self.snake[0].width,
                                                                self.snake[0].y + self.snake[0].height)
            if snake_detected:
                print("Game over")

    def run(self):

        while True:
            self.screen.fill(BLUE)
            self.screen.blit(self.apple, self.apple_rect)

            self.snake_hit_it_self()

            self.draw_snake()

            self.check_button_pressed()

            if self.move is True:
                self.move_snake()

            self.detects_apple()

            self.trough_walls()

            pygame.display.flip()
            pygame.time.Clock().tick(FPS)


game = Game(800, 600)
game.run()
