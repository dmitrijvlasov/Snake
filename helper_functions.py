import random
import pygame


def is_point_in_snake(square: pygame.Rect, point_x, point_y):
    """
    Checks for if the snake hits the apple
    :param square: Snake in a form of rect
    :param point_x: apple point in range of snake by x
    :param point_y: apple point in range of snake by y
    :return: true if apple point inside snake, else false
    """
    if square.x <= point_x <= square.x + square.width and square.y <= point_y <= square.y + square.height:
        return True
    else:
        return False


def get_random_color(start_intensity=0, end_intensity=255):
    """
    Gets random color for apple
    :return: Random color for each - red, green, blue
    """
    r = random.randint(start_intensity, end_intensity)
    g = random.randint(start_intensity, end_intensity)
    b = random.randint(start_intensity, end_intensity)
    rn_color = r, g, b
    return rn_color


def get_random_position(min_x, max_x, min_y, max_y):
    """
    Gets random position for apple
    :return: Random x and y in screen range
    """
    rn_x = random.randint(min_x, max_x)
    rn_y = random.randint(min_y, max_y)
    rn_position = rn_x, rn_y
    return rn_position


def get_normal_position(x_pos, y_pos):
    """
    Gets a position for snake
    :param x_pos: x position of snake
    :param y_pos: y position of snake
    :return: position x and y in screen range
    """
    normal_position = x_pos, y_pos
    return normal_position
