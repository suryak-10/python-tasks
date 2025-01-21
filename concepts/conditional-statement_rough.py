# 1. if Statement
# x = 10
# if x > 5:
#     print("x is greater than 5")


# name="hello"
# if 'o' in name:
#     print("The name contains the letter 'o' .")

# num=18
# if num % 2==0:
#     print("the number is even.",num)


# 2. if-else Statement
# y = 6
# if y % 2 == 0:
#     print("y is even")
# else:
#     print("y is odd")


# x=3
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is less than or equal to 5")


# 3. if-elif-else Statement
# z = -10
# if z > 0:
#     print("z is positive")
# elif z < 0:
#     print("z is negative")
# else:
#     print("z is zero")

# x=7
# if x > 10:
#     print("x is greater than 10")
# elif x == 10:    print("x is equal to 10")
# else:
#     print("x is lesser than 10")


# 4. Ternary Conditional Operator
# x=16
# status = "Adult" if x >= 18 else "Minor"
# print(f"Status: {status}")


# x=11
# result = "even" if x %2 == 0 else "odd"
# print(result)

# a=15
# b=68
# num = a if a<b else b
# print(num)

# x=28
# age="minor" if x < 18 else ("Young adult" if x<30 else "adult")
# print(age)

# name=""
# greet = "hello world" if name else "no name provided"
# print(greet)

# age = None
# age = age if age is not None else 30
# print(age)

# num = 15
# message = "equal" if num == 15 else "Not equal"
# print(message)


# 5. Conditional Expression in while Loops
# counter = 5
# while counter > 0:
#     print(counter)
#     counter -= 1  # ( counter=counter-1 )

# x = 0
# while x < 10 and x % 2 == 0:  # 0 lesser than 10
#     print("even x:",x)
#     x+=2

# x=5
# while not x == 0:
#     print("x is:",x)
#     x-=1

# 6. Conditional Expression in for Loops
# numbers = [1, 2, 3, 4, 5,6]
# for n in numbers:
#     if n % 2 == 0:
#         print(f"Even number: {n}")

 # numbers = [1, 2, 3, 4, 5, 6]
# categories = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
# print(categories)

# numbers = [1, 2, 3, 4, 5, 6]
# for num in numbers:
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared_evens = [num**2 for num in numbers if num % 2 == 0]
# print(squared_evens)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     if num % 2 == 0:
#         print(num**2)


# 7. Logical Operators (and, or, not)
# a, b = True, False     #not false = true
# if a and not b:
#     print("Condition met")

# age=22
# income=4000
# if age >= 18 and income >= 5000:
#     print("your are eligible for th loan")
# else:
#     print("your are  not eligible for th loan")


# num=16
# if num<10 or num>20:
#     print("the given number outside the range of 10 to 20:",num)
# else:
#     print("the given number within the range of 10 to 20:",num)


# is_weekend = True
# if not is_weekend:
#     print("it's a weekday.you have to work!")
# else:
#     print("it's a weekend. enjoy the day!")

# number = 189
# if (number < 0 or number > 100) and not (number % 5==0):
#     print("Condition met.")
# else:
#     print("Condition not met.")



# 8. Nested Conditional Statements
# value = 20
# if value > 10:
#     if value % 2 == 0:
#         print("Value is even and greater than 10")


# value = 5
# if value > 10:
#     if value % 2 == 0:
#         print("Value is even and greater than 10")
# else:
#      print("Value is odd and lesser than 10")


# age = 19
# citizen = not False
# if age >= 18:
#     if citizen:
#         print("you are eligible to vote.")
#     else:
#         print("you need to be citizen to vote.")
# else:
#     print("you are too young to vote.")



# 9. match-case Statement
# fruit = "apple"
# match fruit:
#     case "banana":
#         print("This is an banana")
#     case "apple":
#         print("This is a apple")
#     case _:
#         print("Unknown fruit")


# numbers = 400
# match numbers:
#     case 300:
#         print("server error")
#     case 400:
#         print("correct")
#     case 404:
#         print("error")
#     case _:
#         print("unknown numbers")



# 10. try-except as Conditional Error Handling
# try:
#     result = 10 / 0
#     print(result)
# except ZeroDivisionError:
#     print("Cannot divide by zero")


# try:
#   a=int(input("enter number 1:"))
#   b=int(input("enter number 2:"))
#   result=a//b
#   print("your answer is :",result)
# except ZeroDivisionError:
#   print("cannot be divided by zero.")
# except ValueError:
#   print("alphabet cannot be divided.")


# 11. assert Statement
# age = 17
#
# assert age >= 18, "Age must be above 18 to get a sim card"
#
# if not age >= 18:
#     raise Exception("Age must be above 18 to get a sim card")
#
#
# else:
#     print("You are eligible to get a sim card!")


# x = 10
# assert x > 5, "x should be greater than 5"
# print("Assertion passed, x is greater than 5.")


# items = [1, 2, 3]
# assert len(items) > 0, "The list is empty"
# print("The list has items.")





# 12. Conditional Expression with lambda Functions
# is_positive = lambda x: "Positive" if x > 0 else "Non-positive"
# print(is_positive(-5))

# even_or_odd = lambda num: "even" if num % 2 == 0 else "odd"
# print(even_or_odd(6))
# print(even_or_odd(7))

# sign = lambda num: "positive" if num > 0 else "negative" if num < 0 else "zero"
# print(sign(6))
# print(sign(-7))
# print(sign(0))



# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x**2, numbers)
# squared_numbers_list = list(squared_numbers)
# print(squared_numbers_list)



# 13. List Comprehensions with Conditions
# numbers = [1, 2, 3, 4, 5, 6]
# squares = [n**2 for n in numbers if n % 2 == 0]
# print(f"Squares of even numbers: {squares}")

# numbers=[1,2,3,4,5,6]
# for n in numbers:
#    if n % 2 == 0:
#     print(n**2)



# # 14. Generator Expressions with Conditions
# numbers = [1, 2, 3, 4, 5, 6]
# odd_numbers = (n for n in numbers if n % 2 != 0)
# for odd in odd_numbers:
#     print(f"Odd number: {odd}")




# 15. with Statement with Conditions
# x=10
# with open("test.txt", "w") if x > 5 else open("default.txt", "w") as file:
#     file.write("Conditional file handling example")
#
# print("file operation completed")


# x = 10
# if x > 15:
#     with open("test.txt", "w") as file:
#         file.write("Conditional file handling example")
# else:
#     with open("default.txt", "w") as file:
#         file.write("Conditional file handling example")
#
# print("file operation completed")
#



# 16. Short-Circuit Evaluation
# x=17
# short_circuit = x > 5 and "x is large"
#
# print(short_circuit)
# print(short_circuit)
#
# name = input("Enter your name: ")
#
# if name != "":
#     print(name)
# else:
#     print("NA")
#
# print(name or "NA")
# print("NA" if name == "" else name)
#
# def greet(name):
#     print(f"Hello this is greet message {name}")
#
# # greet(name)
# name and greet(name)
# # print(name or x == 19 or "Empty name" or "Your name is empty")  # "or"  return true
# print('_____')
# print(name and x == 17 and "Empty name" and "Your name is empty")  # "and" return false
# print('_____')







# x=15
# short_circuit = x > 5 and "x is large"
# print(short_circuit)


# x = 2
# y = 10
# if x < 3 and y > 7:
#     print("Both conditions are true.")
# else:
#     print("One or both conditions are false.")
#
# if x > 3 or y < 5:
#     print("At least one condition is true.")




# 17. Decorators with Conditional Logic
# def greet(num):
#     return "Hello, Positive Number!"
#
# print(greet(5))
# print(greet(-5))




# 18. break and continue in Loops
# for num in range(10):
#     if num == 5:
#         break
#     if num % 2 == 0:
#         continue
#     print(f"Processed number: {num}")



# for number in range(1, 10):
#     if number == 7:
#         print("Breaking the loop when number is 7.")
#         break
#     print(number)


# for number in range(1, 10):
#     if number % 2 == 0:
#         continue
#     print(number)




# 19. Exception Handling as Condition
# def check_positive(value):
#     if value < 0:
#         raise ValueError("Value must be non-negative")
#     return True
#
# try:
#     check_positive(-10)
# except ValueError as e:
#     print(e)




# def divide_numbers(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         result = "Cannot divide by zero."
#     return result
#
# print(divide_numbers(10, 0))
# print(divide_numbers(10, 8))




# 20. Conditional Logic with itertools
# from itertools import filterfalse
# data = [1, 2, 3, 4, 5]
# filtered = list(filterfalse(lambda x: x % 2 == 0, data))
# print(f"Filtered data (no evens): {filtered}")



#21. next()
# numbers = [1, 3, 5, 7, 8, 10]
# first_even = next((x for x in numbers if x % 2 == 0), None)
# print(first_even)


# my_list = [1, 2, 3]
# iterator = iter(my_list)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator, "No more items"))