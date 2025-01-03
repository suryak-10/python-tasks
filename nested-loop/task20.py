# Task 20: Print an Alphabet Triangle
# Sample Input:
#     Rows: 3
# Expected Output:
#     A
#     A B
#     A B C


n=3
def triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(j + 65), end=" ")
        print()
triangle(n)