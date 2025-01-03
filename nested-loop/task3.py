# Task 3: Create a Multiplication Table
# Sample Input:
#     Range: 1 to 3
# Expected Output:
#     1 2 3
#     2 4 6
#     3 6 9

start = 1
end = 3

for i in range(start, end + 1):
    for j in range(start, end + 1):
        print(i * j, end=" ")
    print()