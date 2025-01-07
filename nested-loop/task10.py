# Task 10: Print Prime Numbers in a Triangle
# Sample Input:
#     Rows: 4
# Expected Output:
#     2
#     3 5
#     7 11 13
#     17 19 23 29

# def prime(n):
#     return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))
#
# def prime_triangle(rows):
#     num, count = 2, 0
#     for r in range(1, rows + 1):
#         primes = []
#         while len(primes) < r:
#             if prime(num): primes.append(num)
#             num += 1
#         print(" ".join(map(str, primes)))
# prime_triangle(4)