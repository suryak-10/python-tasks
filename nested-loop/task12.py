# Task 12: Count Unique Pairs in a List
# Sample Input:
#     List: [1, 2, 3]
# Expected Output:
#     Unique Pairs: (1, 2), (1, 3), (2, 3)

lists = [1, 2, 3]
import itertools as it
print(list(it.combinations(lists, 2)))