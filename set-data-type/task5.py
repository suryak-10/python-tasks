# Task 5: Find Intersection of Two Sets
# Sample Input:
#     Set 1: {1, 2, 3, 4}
#     Set 2: {3, 4, 5, 6}
# Expected Output:
#     Intersection: {3, 4}

s1={1, 2, 3, 4}
s2={3, 4, 5, 6}
s1.intersection_update(s2)
print(s1)