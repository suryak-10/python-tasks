# Task 7: Replace Negative Numbers with 0
# Sample Input:
#     List: [3, -2, 7, -5, 9]
# Expected Output:
#     Result: [3, 0, 7, 0, 9]

l=[3, -2, 7, -5, 9]
l = [(i > 0) * i for i in l]
print(l)