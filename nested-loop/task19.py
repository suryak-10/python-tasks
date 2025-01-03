# Task 19: Generate Pascal's Triangle
# Sample Input:
#     Rows: 4
# Expected Output:
#     1
#     1 1
#     1 2 1
#     1 3 3 1


rows=4
for i in range(rows):
    a = 1
    for j in range(0, i + 1):
        print(a, end=' ')
        a = a * (i - j) // (j + 1)
    print()