# Task 8: Find Intersection of Two Lists
# Sample Input:
#     List 1: [1, 2, 3, 4, 5]
#     List 2: [4, 5, 6, 7, 8]
# Expected Output:
#     Intersection: [4, 5]

a=[1, 2, 3, 4, 5]
b=[4, 5, 6, 7, 8]
c=list(set(a) & set(b))
print("intersection:",c)