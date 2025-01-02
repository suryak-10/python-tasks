# Task 6: Find Difference Between Two Sets
# Sample Input:
#     Set 1: {10, 20, 30, 40, 50}
#     Set 2: {30, 40, 60}
# Expected Output:
#     Difference: {10, 20, 50}

s1={10, 20, 30, 40, 50}
s2={30, 40, 60}
return_value=s1.difference_update(s2)
print(s1)