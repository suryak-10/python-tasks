# Task 2: Find the Second Largest Number in a List


def second_largest(input_list):
  input_list.sort()
  return input_list[-2]
print(second_largest([12, 45, 7, 34, 89, 23]))