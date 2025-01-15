# Task 7: Create a Factorial Using Memoization



def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)

print(facto(5))



# num = 6
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
#
# print(f"The factorial of {num} is {factorial}")