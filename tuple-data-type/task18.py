# Task 18: Add an Element to a Tuple
# Sample Input:
#     Tuple: (5, 10, 15)
#     Element to Add: 20
# Expected Output:
#     New Tuple: (5, 10, 15, 20)

tuple = (5, 10, 15)
element = 20
new_tuple=(tuple)+(element,)
print(new_tuple)