# Task 2: Print a Star Pattern
# Sample Input:
#     Rows: 4
# Expected Output:
#     *
#     * *
#     * * *
#     * * * *

rows = 4

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()