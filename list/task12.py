# Task 2: Find the Second Largest Number
# Sample Input:
#     List: [12, 45, 7, 34, 89, 23]
# Expected Output:
#     Second Largest Number: 45

numbers = [12, 45, 7, 34, 89, 23]
numbers.remove(max(numbers))
print(max(numbers))
print(numbers)