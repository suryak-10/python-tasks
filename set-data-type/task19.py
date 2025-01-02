# Task 9: Find the Symmetric Difference of Multiple Sets
# Sample Input:
#     Set 1: {1, 2, 3}
#     Set 2: {2, 3, 4}
#     Set 3: {3, 4, 5}
# Expected Output:
#     Symmetric Difference: {1, 5}

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
set1=s1|s2
set2=s2|s3
result=set1.symmetric_difference(set2)
# set2.symmetric_difference(set3)
print("Symmetric Difference:", result)