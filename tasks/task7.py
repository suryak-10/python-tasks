# Task 7: Create a Factorial Using Memoization



def sum_of_nums(num):
    if num == 1:
        return 1
    else:
        return num * sum_of_nums(num - 1)

print(sum_of_nums(5))



# num = 6
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
#
# print(f"The factorial of {num} is {factorial}")