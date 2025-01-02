# Task 5: Split List into Two Halves
# Sample Input:
#     List: [1, 2, 3, 4, 5, 6]
# Expected Output:
#     First Half: [1, 2, 3]
#     Second Half: [4, 5, 6]

# l1=[1, 2, 3, 4, 5, 6]
l1=[44,12,81,22,68,67,99,24,55]
a = len(l1) // 2
x = []
y = []
for i in range(len(l1)):
    # print(i)
    if (i < a):
        x.append(l1[i])
    else:
        y.append(l1[i])
print("First Half:",x)
print("Second Half:",y)