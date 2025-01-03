# Task 7: Generate a Diamond Pattern
# Sample Input:
#     Rows: 3
# Expected Output:
#       *
#      * *
#     * * *
#      * *
#       *

rows=3
for i in range(rows):
    print(" "*(rows-i-1)+"* "*(i+1))
for j in range(rows-1,0,-1):
    print(" "*(rows-j)+"* "*(j))