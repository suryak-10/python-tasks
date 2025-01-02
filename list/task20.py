# Task 10: Flatten a Nested List
# Sample Input:
#     Nested List: [[1, 2], [3, 4, 5], [6]]
# Expected Output:
#     Flattened List: [1, 2, 3, 4, 5, 6]

nested_list=[[1, 2], [3, 4, 5], [6]]
Flattened_list = sum(nested_list, [])
print( Flattened_list)