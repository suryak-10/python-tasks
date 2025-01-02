# Task 6: Remove Elements at Even Indices
# Sample Input:
#     List: [10, 20, 30, 40, 50, 60]
# Expected Output:
#     Result: [20, 40, 60]

# input  = [10, 20, 30, 10, 40, 50, 40, 60, 10, 30 ]
# output = [20, 10, 40, 40, 10]

l=[10, 20, 30, 10, 10, 40, 50, 40, 60, 10, 30 ]
#   0   1   2   3   4   5   6  7    8   9   10
# l = [10, 20, 30, 40, 50, 60]
x=[]
for i in range(len(l)):
    # print(i)
    if i % 2 != 0:
        x.append(l[i])
print(x)
    # l.remove(i)
# print("result:",l)