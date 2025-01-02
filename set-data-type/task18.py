# Task 8: Update a Set with New Elements
# Sample Input:
#     Set: {5, 10, 15}
#     Elements to Add: 20, 25
# Expected Output:
#     Set after update: {5, 10, 15, 20, 25}

set={5,10,15}
elements_to_add=20,25
set.update(elements_to_add)
print("Set after update:",set)