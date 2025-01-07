# Task 16: Calculate Column-Wise Sum in a Matrix
# Sample Input:
#     Matrix: [[1, 2, 3], [3, 4, 6]]
# Expected Output:
#     Column Sums: [4, 6, 9]
# [0, 0, 0]

# matrix = [[1, 2,3], [3, 4]]
# num_columns = len(matrix[0])
# column_wise_sum = [0] * num_columns
#
# for row in matrix:
#     for i in range(num_columns):
#         column_wise_sum[i] += row[i]
#
# print(column_wise_sum)

matrix = [[1, 2, 3], [3, 4, 6]]
num_columns = len(matrix[0])
column_wise_sum = [0] * num_columns

for row in matrix:
    for i in range(num_columns):
        column_wise_sum[i] += row[i]

print(column_wise_sum)