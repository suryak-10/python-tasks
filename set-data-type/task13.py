# Task 3: Find the Union of Three Sets
# Sample Input:
#     Set 1: {1, 2, 3}
#     Set 2: {3, 4, 5}
#     Set 3: {5, 6, 7}
# Expected Output:
#     Union: {1, 2, 3, 4, 5, 6, 7}

set1= {1, 2, 3}
set2= {3, 4, 5}
set3= {5, 6, 7}
res=set1.union(set2,set3)
print(res)