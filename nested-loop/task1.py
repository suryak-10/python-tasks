# Task 1: Print a Number Triangle
# Sample Input:
#     Rows: 3
# Expected Output:
#     1
#     1 2
#     1 2 3

rows = 3

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()