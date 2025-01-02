# Task 8: Check if a Set is Superset of Another Set
# Sample Input:
#     Set 1: {1, 2, 3, 4, 5}
#     Set 2: {3, 4}
# Expected Output:
#     Output: "Set 1 is a superset of Set 2."

s1= {1, 2, 3, 4, 5}
s2= {3, 4}
return_value = s1.issuperset(s2)

# if return_value:
#     print('Is superset')
#
# if return_value:
#     print(s2, "is present in set s1")

print(return_value)