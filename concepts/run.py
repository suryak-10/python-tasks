# Map: Transform elements
from list.task6 import result

numbers = [1, 2, 3, 4]


def square(num: int):
    return num ** 2


# squared = map(lambda x: x**2, numbers)  # Map
squared = map(square, numbers)  # Map
print(squared)  # [1, 4, 9, 16]


def custom_map(callback, give_list):
    result = []
    for num in give_list:
        result.append(callback(num))
    return result


def cube(num: int):
    return num ** 3


def is_even(num: int):
    return num % 2 == 0


print(custom_map(square, numbers))
print(custom_map(cube, numbers))
print(list(map(square, numbers)))

# print(result)
