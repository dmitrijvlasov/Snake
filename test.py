# class Dog:
#     def __init__(self, name, owner):
#         self.name = name
#         self.owner = owner
#
#     def speak(self):
#         print("wuf", self.name)
#
#
# d = Dog(name="doggy", owner="me")
# d.speak()
#
#
# class Point:
#     def __init__(self, point_x, point_y):
#         self.point_x = point_x
#         self.point_y = point_y
#
#     def __str__(self):
#         return "Point(" + str(self.point_x) + ", " + str(self.point_y) + ")"
#
#
# def get_list_of_points():
#     # create list
#     list_of_points = []
#     for index in range(0, 20):
#         # create new Point
#         new_point = Point(index, index)
#         print(new_point)
#         # add new point to list
#         list_of_points.append(new_point)
#     # return lit of points
#     print(list_of_points)
#     return
#
#
# get_list_of_points()

#
# numbers = [5, 7, 2, 3, 15, 12]
# print(numbers)
# for index, element in enumerate(numbers):
#     if index + 1 < len(numbers):
#         if numbers[index] > numbers[index + 1]:
#             current = element
#             next_ = numbers[index + 1]
#             numbers[index] = next_
#             numbers[index + 1] = current
# print(numbers)
#
# for index in reversed(range(0, len(numbers))):
#     print(numbers[index])

snake_body = self.snake[2:]
for snake_part in snake_body:
    snake_detected = helper_functions.is_point_in_snake(snake_part, self.snake[0].x, self.snake[0].y)
    if snake_detected:
        print("Game over 1")
        print(snake_part, self.snake[0].x, self.snake[0].y)
        # sys.exit()

snake_body = self.snake[2:]
for snake_part in snake_body:
    snake_detected = helper_functions.is_point_in_snake(snake_part, self.snake[0].x + self.snake[0].width,
                                                        self.snake[0].y)
    if snake_detected:
        print("Game over 2")
        print(snake_part, self.snake[0].x + self.snake[0].width, self.snake[0].y)
        # sys.exit()

snake_body = self.snake[2:]
for snake_part in snake_body:
    snake_detected = helper_functions.is_point_in_snake(snake_part, self.snake[0].x, self.snake[0].y
                                                        + self.snake[0].height)
    if snake_detected:
        print("Game over3")
        print(snake_part, self.snake[0].x, self.snake[0].y + self.snake[0].height)
        # sys.exit()

snake_body = self.snake[2:]
for snake_part in snake_body:
    snake_detected = helper_functions.is_point_in_snake(snake_part, self.snake[0].x + self.snake[0].width,
                                                        self.snake[0].y + self.snake[0].height)
    if snake_detected:
        print("Game ove4r")
        print(snake_part, self.snake[0].x + self.snake[0].width, self.snake[0].y + self.snake[0].height)
        # sys.exit()
