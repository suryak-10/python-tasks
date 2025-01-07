# Task 6: Print Characters in a Grid
# Sample Input:
#     String: "abc"
#     Rows: 3
# Expected Output:
#     a b c
#     a b c
#     a b c


def print_in_grid(string, rows):
    characters = list(string)
    for char in range(rows):
        print(" ".join(characters))
print_in_grid("abc", 3)
print_in_grid("abcSDFASD", 8)
print_in_grid("HELLO", 3)