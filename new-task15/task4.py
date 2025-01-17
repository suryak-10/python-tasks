# def save_to_file(data, filename):
#     with open(filename, 'w') as f:
#         f.write(data)
#     print("Data saved successfully!")
#
# save_to_file("Hello, World!", "output.txt")
from numpy.testing.print_coercion_tables import print_new_cast_table

# def add():
#   a = 5
#   b = 3
#   print(a+b)
#
# add()


# def add(a, b):
#      return a + b
#
# result = add(5, 3)
# print(result)



# def arithmetic_operations(a, b):
#     # return a + b, a - b, a * b, a / b
#     return [a + b, a - b, a * b, a / b, "completed",1,2,3,4,5]
#
# result = arithmetic_operations(10, 2)
# add = result[0]
# sub = result[1]
# mul = result[2]
# div = result[3]
# message = result[4]
# numbers = result[5]
# print(result)
#
# add, sub, mul, div, message, *numbers= arithmetic_operations(10, 2)
# # add, sub, mul, div = (12, 8, 20, 5)
# print(add, sub, mul, div, message , *numbers)


# global_var = "I'm global"
# print(global_var)
# age=None
# def my_function1():
#     date = "15/01/24"
#
#     global name, age
#     print(len([12, 3, 45, 6]))
#     age =25
#     print(name, age)
#     name = "John"
#     print(name)
#     print(global_var)  # Accessible inside the function
#
# print(len([1,2, 4]))
#
# name = "surya"
# print(name)
# def my_function():
#     name = "vignesh"
#     print(age)
#     global_var1 = "I'm local"
#     print(name)
#     print(global_var)  # Accessible inside the function
#
# print(age)
# my_function1()
# print(age)
# my_function()

# def outer_function():
#     enclosing_var = "Hello"
#
#     def inner_function():
#         print(enclosing_var)  # Accessing the enclosing variable
#
#     inner_function()
#
# outer_function()

# def function_b():
#     print("Inside function B")
#     function_c()
#
# def function_a():
#     print("Inside function A")
#     function_b()
#
# def function_c():
#     print("Inside function C")
#
# # Starting point
# function_a()
#
# def add(a,b):        #(a,b) --> Parameter  | add --> Function Name , we can give any Function Name    | def --> Function Definition
#   return(a+b)
#
# print(add(b=2, a=8))
# print(add(b=2, a=8))

# name1 = "surya"
#
# def update_name():
#     global  name1
#     name1 = "john"
#     print(name1)
#     age = 28
#     if name1 == "john":
#         # age = 28
#         print(age)
#     print(age)
#
# print(name1)
# update_name()
# print(name1)


# def fibonacci(n):
#     if n == 0:  # Base case 1
#         return 0
#     elif n == 1:  # Base case 2
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
#
# print(fibonacci(6))

# add2 = lambda a, b: a + b
# print(add2(5, 3))
# print(add2(6, 8))


# def greet(name):
#     print(f"Hello, {name}! Welcome to Python programming.")
#
# greet("Alice")

# def add(a, b, c):
#     return a + b + c
#
# result = add(1, 2, 3)
# print(result)

# def add(a,b):      # (a,b)<--- parameters
#   return(a+b)
#
# print(add(8,3))


# def add(a, b, c):
#     return a + b + c
#
# # Keyword arguments
# result = add(c=3, b=2, a=1)  # (c=3, b=2, a=1) <-- Keyword Arguments
#
# print(result)

# def add(a, b):
#     result = a + b
#     return result  # return <--- Return Statement
#
# # Calling the function and printing the returned value
# sum_result = add(3, 4)
# print(sum_result)

# def add(a, b):
#     return a + b      # return ---> return statement
#
# result = add(5, 3)
# print(result)

# def arithmetic_operations(a, b):
#     return {
#         "add": a+b,
#         'div': a / b,
#         "mul": a*b,
#         "sub": a - b,
#     }
#     return [a + b, a - b, a * b, a / b, "completed", 1,2, 3, 4, 5 ]
#
# result = arithmetic_operations(10, 2)
# add = result["add"]
# sub = result["sub"]
# mul = result["mul"]
# div = result["div"]
# print(result)
#
# values  = arithmetic_operations(10, 2)
# print(values)

# count = 0  # Global variable
#
# def increment():
#     global count  # Declare that we're using the global variable
#     count += 1
#
# increment()
# print(count)


# nums = [13, 5, 6, 8, [24, 6, 3, 64,[1,5, [1, [1, 2, [2, 4, 3, ]],  2, 4], 6], 93,6,3], 95, 3, 3, ]
# print(nums)
#
# def print_list(elements, level):
#     for element in elements:
#         if type(element) == list:
#             print_list(element, level+1)
#         else:
#             print(f"{element} in level {level}")
#
# print_list(nums, 0)

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     # Recursive case
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# # Calling the function
# print(fibonacci(6))


# name1 = ["surya"]
#
# def update_name():
#     name1[0] = "john"
#     print(name1[0])
#     age = 28
#     if name1 == "john":
#         print(age)
#     print(age)
#
# print(name1[0])
# update_name()
# print(name1[0])

# def get_fruits():
#     return ["Apple", "Banana", "Cherry"]
#
# fruits = get_fruits()
# print(fruits)

# def arithmetic_operations(a, b):
#     return {
#         "add": a+b,
#         'div': a / b,
#         "mul": a*b,
#         "sub": a - b,
#     }
#     return [a + b, a - b, a * b, a / b, "completed", 1,2, 3, 4, 5 ]
#
# result = arithmetic_operations(10, 2)
# # add = result["add"]
# # sub = result["sub"]
# # mul = result["mul"]
# # div = result["div"]
#
# print(result)
#
# values  = arithmetic_operations(10, 2)
# print(values)

# def my_function():
#     local_var = 10
#     print(local_var)
#
# my_function()


# def outer_function():
#     enclosing_var = "Hello"
#
#     def inner_function():
#         print(enclosing_var)
#     inner_function()
#
# outer_function()

# global_var = "I'm global"
#
# def my_function():
#     print(global_var)  # Accessible inside the function
#
# my_function()
# print(global_var)


# square = lambda x: x ** 2
# print(square(5))

