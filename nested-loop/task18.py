# Task 18: Find All Triplets Adding to a Target
# Sample Input:
#     List: [1, 2, 3, 4]
#     Target: 6
# Expected Output:
#     Triplets: [(1, 2, 3)]

# n=[1, 2, 3, 4]
# for i in range(n+1):
#     for j in range(n+1):
#         if i+j <= n:
#          print((i, j, n-i-j))

# n=[1, 2, 3, 4]
# for i in range(n + 1):
#     for j in range(i, (n - i)//2 + 1):
#      out.append((i, j, n-i-j))

# n=[1, 2, 3, 4]
# def triplets(array,targetsum):
    # array.sort(n)
    # triplets=[]
    # for i in range(len(array)-2):
    #     left=i=1
    #     right=len(array) - 1
    #     print(n)