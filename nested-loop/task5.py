# Task 5: Calculate Pairwise Sum of Two Lists
# Sample Input:
#     List1: [1, 2]
#     List2: [3, 4]
# Expected Output:
#     Pairwise Sum: [4, 5, 5, 6]

list1 = [1, 2]
list2 = [3, 4]
list3= [x + y for x in list1 for y in list2]
print(list3)