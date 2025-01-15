# Task 2: Even Numbers Filter
# Sample Input:
#     User Input: "1, 2, 3, 4, 5, 6, 7, 8, 9"
# Expected Output:
#     Even Numbers: [2, 4, 6, 8]



a=[ 1, 2, 3, 4, 5, 6, 7, 8, 9]
b=[]


def is_even(num):
    return num % 2 == 0

for num in a:
    if not is_even(num):
     b.append(num)
print(b)



