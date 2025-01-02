# Task 19: Remove an Element from a Tuple
# Sample Input:
#     Tuple: (10, 20, 30, 40, 50)
#     Element to Remove: 30
# Expected Output:
#     New Tuple: (10, 20, 40, 50)

tuple1=(10, 20, 30, 40, 50)
element=30
list1= list(tuple1)
list1.remove(element)
tuple2 = tuple(list1)
print(tuple2)