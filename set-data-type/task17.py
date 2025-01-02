# Task 7: Find the Difference Between Three Sets
# Sample Input:
#     Set 1: {1, 2, 3, 4}
#     Set 2: {3, 4, 5}
#     Set 3: {4, 5, 6}
# Expected Output:
#     Difference: {1, 2}

set1={1, 2, 3, 4}
set2={3, 4, 5}
set3={4, 5, 6}
res=set1.difference(set2,set3)
print(res)