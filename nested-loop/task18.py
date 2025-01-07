# Task 18: Find All Triplets Adding to a Target
# Sample Input:
#     List: [1, 2, 3, 4]
#     Target: 6
# Expected Output:
#     Triplets: [(1, 2, 3)]

# from itertools import combinations
#
#
# def lists(lst, key):
#     def valid(val):
#         return sum(val) == key
#
#     return list(filter(valid, list(combinations(lst, 3))))
#
# lst = [1, 2, 3, 4]
# print(lists(lst, 6))