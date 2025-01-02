# Task 4: Find Union of Two Sets
# Sample Input:
#     Set 1: {1, 2, 3, 4}
#     Set 2: {3, 4, 5, 6}
# Expected Output:
#     Union: {1, 2, 3, 4, 5, 6}

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.update(set2)
print(set1)