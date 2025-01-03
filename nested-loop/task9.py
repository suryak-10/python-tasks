# Task 9: Generate a Spiral Matrix
# Sample Input:
#     Rows: 3
#     Columns: 3
# Expected Output:
#     1 2 3
#     8 9 4
#     7 6 5

start = 3
end = 3

for i in range(start, end + 1):
    for j in range(start, end + 1):
        print(i * j, end=" ")
    print()