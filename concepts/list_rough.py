# def square(x):
#     return x * x
#
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(square, numbers)
# print(list(squared_numbers))
from concepts.list_functions import list_group_by_even

# numbers = [1, 2, 3, 4, 5, 6]
# filtered_numbers = filter(lambda x: x % 2 != 0, numbers)
# filtered_numbers = list(filtered_numbers)
# print(filtered_numbers)

# numbers = [1, 2, 3, 4, 5, 6]
# filtered_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         filtered_numbers.append(num)
# print(filtered_numbers)

# def flatten(nested_list):
#     flattened = []
#     for item in nested_list:
#         if isinstance(item, list):
#             flattened.extend(flatten(item))  # Recursively flatten if it's a list
#         else:
#             flattened.append(item)
#     return flattened
#
# nested_list = [1, [2, 3], [4, [5, 6]], 7]
# flattened_list = flatten(nested_list)
# print(flattened_list)


# numbers = [1, 2, 3, 4]
# first_even = next((x for x in numbers if x % 2 == 0), None)  # Find
# print(first_even)


# def find_first_even(numbers):
#     return next((x for x in numbers if x % 2 == 0), None)
#
# numbers = [1, 2, 3, 4]
# first_even = find_first_even(numbers)
# print(first_even)

# words = ["Hello", "world", "from", "Python"]
# result = " ".join(words)
# print(result)


# words = ["2025", "01", "21"]
# result = "-".join(words)
# print(result)

# lines = ["First line", "Second line", "Third line"]
# result = "\n".join(lines)
# print(result)




# lst = ['a', 'b', 'c', 'd', 'b', 'e']
#
# last_index = len(lst) - 1 - lst[::-1].index('b')
#
# print("Last index of 'b' is:", last_index)



# LastIndexOf:
# numbers = [1, 2, 3, 2, 4]
# last_index = len(numbers) - 1 - numbers[::-1].index(2)  # LastIndexOf
# print(last_index)  # 3
#
#
# lst = ['a', 'b', 'c', 'd', 'b', 'e']
# last_index = len(lst)
# print(lst[-2])



# Concat: Combine lists
# numbers1 = [1, 2]
# numbers2 = [3, 4]
# combined = numbers1 + numbers2
# print(combined)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = []
# for lst in [list1, list2]:
#     result.extend(lst)
# print(result)


# lst = [10, 20, 30, 40, 50]
# result = 30 in lst
# print(result)
#
# result = 100 in lst
# print(result)


# lst = [0, 0, 1, 0]
# result = any(lst)
# print(result)

# lst = [1, 3, 5, 7, 8]
# result = any(x % 2 == 0 for x in lst)
# print(result)

# Find: Find the first matching element
# numbers = [1, 2, 3, 4]
# first_even = next((x for x in numbers if x % 2 == 0), None)
# print(first_even)

# FindIndex: Find the index of the first matching element
# numbers = [1, 2, 3, 4]
# index = next((i for i, x in enumerate(numbers) if x % 2 == 0), -1)
# print(index)


# my_list = [10, 20, 30, 40, 50]
# index = my_list.index(30)
# print("Index of 30:", index)


# my_list = [10, 20, 30, 40, 50]
#
# try:
#     index = my_list.index(60)
#     print("Index of 60:", index)
# except ValueError:
#     print("Element not found")





# Task 2: Check for Odd and Even Numbers in a List
# Sample Input:
#     List: [10, 15, 22, 33, 44, 55]
# Expected Output:
#     Even Numbers: [10, 22, 44]
#     Odd Numbers: [15, 33, 55]


from functools import reduce
from list_functions import  list_group_by_even
list1=[10, 15, 22, 33, 44, 55]


total = reduce(list_group_by_even, list1, {"even":[], "odd": []})

print("reduce fn value for even number: ", total['even'])
print("reduce fn value for odd number: ", total['odd'])