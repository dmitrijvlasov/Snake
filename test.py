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