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


numbers = [5, 7, 2, 3, 15, 12]
print(numbers)
for index, element in enumerate(numbers):
    if index + 1 < len(numbers):
        if numbers[index] > numbers[index + 1]:
            current = element
            next_ = numbers[index + 1]
            numbers[index] = next_
            numbers[index + 1] = current
print(numbers)

for index in reversed(range(0, len(numbers))):
    print(numbers[index])