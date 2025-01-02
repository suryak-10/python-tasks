# Task 16: Merge Two Tuples and Sort Them
# Sample Input:
#     Tuple 1: (3, 1, 2)
#     Tuple 2: (6, 5, 4)
# Expected Output:
#     Merged and Sorted Tuple: (1, 2, 3, 4, 5, 6)

tuple1 = (3, 1, 2)
tuple2 = (6, 5, 4)
tuple3=tuple1+tuple2
converted_list= list(tuple3)
converted_list.sort()
converted_list = tuple(converted_list)
print(converted_list)