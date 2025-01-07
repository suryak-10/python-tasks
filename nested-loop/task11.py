# Task 11: Calculate Row-Wise Sum in a Matrix
# Sample Input:
#     Matrix: [[1, 2], [3, 4]]
# Expected Output:
#     Row Sums: [3, 7]
from numpy.matrixlib.defmatrix import matrix


# def row_wise(matrix):
#     return [sum(row) for row in matrix]
# matrix = [[1, 2], [3, 4]]
# row = row_wise(matrix)
# print(row)

matrixs = [[1, 2], [3, 4]]
result=[]
for matrix in matrixs:
    result.append(sum(matrix))
    # print(sum(matrix))
print(result)