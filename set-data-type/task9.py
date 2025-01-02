# Task 9: Find Symmetric Difference Between Two Sets
# Sample Input:
#     Set 1: {1, 2, 3, 4}
#     Set 2: {3, 4, 5, 6}
# Expected Output:
#     Symmetric Difference: {1, 2, 5, 6}

set1={1, 2, 3, 4}
set2={3, 4, 5, 6}
res = set1.symmetric_difference(set2)
print(res)

# diff_set = set2.difference(set1)
# print(diff_set)