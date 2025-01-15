# Types of functions
#     1.  Built in
#     2.  User define
from multiprocessing.spawn import prepare
from struct import pack_into

# 1.  Built in
total = sum([1 , 2, 4])
print(total)
print(sum([1 , 2, 4]))


# 2.  User define
def list_total(list_of_nums):
    total = 0
    for num in list_of_nums:
        total = total + num
    return total


# function variations :
# 1. Function
# 2. Method

my_total = list_total([1, 2, 4, 5])
nums = [1, 2, 4, 5]
print(my_total)
print(list_total(nums))
print(sum(nums))

def greet_name(name, age):
    print('Hello ' + name + " and my age is " +str(name))

greet_name(name="Surya", age=24)
greet_name(name="John", age=27)
greet_name(name="Sushil", age=34)
greet_name(name="vignesh", age=22)

# Function with return type and without return type.

# def mul_by_7(num):
#     result = num * 7
#     print(result)

def mul_by_7(num:int):
    result = num * 7
    return result

mul_by_7(4)
mul_by_7(1)
mul_by_7(3)
mul_by_7(6)
num8 = mul_by_7(8)
print(num8)

nums = [12, 3, 4, 5, 8,6]


print(len(nums))

subjects = [183, 147, 134, 167, 174]

def calc_percentage(num:int):
    percentage = (num/500) * 100
    # print(f"The percentage is = {percentage}")
    return percentage

for subject in subjects:
    percentage = calc_percentage(subject)
    print(f"The percentage of {subject} is {percentage}")


num = 174
percentage = calc_percentage(num)
print(f"The result percentage is {percentage}")