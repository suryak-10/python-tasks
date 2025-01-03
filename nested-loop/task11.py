# lista= [[1, 2], [3, 4]]
# for i in range(len(lista)):
#     x = sum(lista[i][lista])
# print(x)


def a(matrix):
    return [sum(row) for row in matrix]
matrix = [[1, 2], [3, 4]]
row = a(matrix)
print(row)