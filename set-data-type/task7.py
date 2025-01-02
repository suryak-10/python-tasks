# Task 7: Check if a Set is Subset of Another Set
# Sample Input:
#     Set 1: {1, 2, 3}
#     Set 2: {1, 2, 3, 4, 5}
# Expected Output:
#     Output: "Set 1 is a subset of Set 2."

s1={1, 2, 3}
s2={1, 2, 3, 4, 5}
return_value=s1.issubset(s2)
print(return_value)