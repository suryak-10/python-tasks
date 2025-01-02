# Task 3: Rotate List by n Positions
# Sample Input:
#     List: [1, 2, 3, 4, 5]
#     n: 2
# Expected Output:
#     Rotated List: [4, 5, 1, 2, 3]

n = 2

list1 = [1, 2, 3, 4, 5]
list1 = (list1[len(list1) - n:len(list1)] + list1[0:len(list1) - n])
print(list1)