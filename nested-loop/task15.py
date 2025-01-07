# Task 15: Generate a Cross Pattern
# Sample Input:
#     Size: 3
# Expected Output:
#     *   *
#      * *
#       *
#      * *
#     *   *

# n = 3
# for i in range(1, 2 * n):
#   for j in range(1, 2 * n):
#     if i==j or i+j==2 * n:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

num=int(input("enter the numbers of rows: "))
# length=len(num)
for i in range(0,num):
  for j in range(0,num):
    if i==j or i+j==num-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()