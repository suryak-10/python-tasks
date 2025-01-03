# Task 14: Generate All Subsets of a List
# Sample Input:
#     List: [1, 2]
# Expected Output:
#     Subsets: [], [1], [2], [1, 2]


# def subsets(s):
#     if len(s) == 0:
#         return [[]]
#     x = subsets(s[:-1])
#     return x + [[s[-1]] + y for y in x]
# s = [1, 2]
# result = subsets(s)
# print(result)