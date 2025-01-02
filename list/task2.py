# Task 2: Even Numbers Filter
# Sample Input:
#     User Input: "1, 2, 3, 4, 5, 6, 7, 8, 9"
# Expected Output:
#     Even Numbers: [2, 4, 6, 8]

a=[ 1, 2, 3, 4, 5, 6, 7, 8, 9]
b=[]
for num in a:
    if num % 2 == 0:
     b.append(num)
print(b)