# Task 17: Find Symmetric Pairs in a Matrix
# Sample Input:
#     Matrix: [[1, 2], [1, 2], [2, 1]]
# Expected Output:
#     Symmetric Pairs: [(0, 1), (1, 0)]

matrix = [[1, 2], [1, 4], [5, 1], [9,8,7], [7,9,8]]

result = []
for i, target in enumerate(matrix):
    for j, current in enumerate(matrix):
        if i == j:
            continue
        target = set(target)
        if target == set(current):
            result.append(list(target))
        # print(current)
    # print(index, value)

print(result)
# def findPairs(pairs):

#     s = set()
#     for (x, y) in matrix:
#         s.add((x, y))
#         if (y, x) in s:
#             print((x, y))
# matrix = [[1, 2], [2, 1]]
# findPairs(matrix)