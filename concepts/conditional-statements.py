# Conditional Statements in Python Examples



# 1. if Statement
x = 10
if x > 5:
    print("x is greater than 5")







# 2. if-else Statement
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")




# 3. if-elif-else Statement
z = -10
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")




# 4. Ternary Conditional Operator
x=16
status = "Adult" if x >= 18 else "Minor"
print(f"Status: {status}")




# 5. Conditional Expression in while Loops
counter = 5
while counter > 0:
    print(counter)
    counter -= 1




# 6. Conditional Expression in for Loops
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        print(f"Even number: {n}")




# 7. Logical Operators (and, or, not)
a, b = True, False
if a and not b:
    print("Condition met")




# 8. Nested Conditional Statements
value = 20
if value > 10:
    if value % 2 == 0:
        print("Value is even and greater than 10")




# 9. match-case Statement
fruit = "apple"
match fruit:
    case "apple":
        print("This is an apple")
    case "banana":
        print("This is a banana")
    case _:
        print("Unknown fruit")




# 10. try-except as Conditional Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")




# 11. assert Statement
num = 0
age = 19

# assert age >= 18, "Age must be above 18 to get a sim card"
if not age >= 18:
    raise Exception("Age must be above 18 to get a sim card")




# 12. Conditional Expression with lambda Functions
is_positive = lambda x: "Positive" if x > 0 else "Non-positive"
print(is_positive(-5))




# 13. List Comprehensions with Conditions
squares = [n**2 for n in numbers if n % 2 == 0]
print(f"Squares of even numbers: {squares}")




# 14. Generator Expressions with Conditions
odd_numbers = (n for n in numbers if n % 2 != 0)
for odd in odd_numbers:
    print(f"Odd number: {odd}")




# 15. with Statement with Conditions
with open("test.txt", "w") if x > 5 else open("default.txt", "w") as file:
    file.write("Conditional file handling example")

print("file operation completed")



x=17
# 16. Short-Circuit Evaluation
short_circuit = x > 5 and "x is large"

print(short_circuit)
print(short_circuit)

name = input("Enter your name: ")

if name != "":
    print(name)
else:
    print("NA")

print(name or "NA")
print("NA" if name == "" else name)

def greet(name):
    print(f"Hello this is greet message {name}")

# greet(name)
name and greet(name)
# print(name or x == 19 or "Empty name" or "Your name is empty")  # "or"  return true
print('_____')
print(name and x == 17 and "Empty name" and "Your name is empty")  # "and" return false
print('_____')

# 17. Decorators with Conditional Logic
def conditional_decorator(func):
    def wrapper(*args, **kwargs):
        if args[0] > 0:
            return func(*args, **kwargs)
        else:
            return "Condition not met"
    return wrapper

@conditional_decorator
def greet(num):
    return "Hello, Positive Number!"

print(greet(5))
print(greet(-5))




# 18. break and continue in Loops
for num in range(10):
    if num == 5:
        break
    if num % 2 == 0:
        continue
    print(f"Processed number: {num}")




# 19. Exception Handling as Condition
def check_positive(value):
    if value < 0:
        raise ValueError("Value must be non-negative")
    return True

try:
    check_positive(-10)
except ValueError as e:
    print(e)




# 20. Conditional Logic with itertools
from itertools import filterfalse
data = [1, 2, 3, 4, 5]
filtered = list(filterfalse(lambda x: x % 2 != 0, data))
print(f"Filtered data (no evens): {filtered}")



numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)


numbers = [1, 3, 5, 7, 8, 10]
first_even = next((x for x in numbers if x % 2 == 0), None)
print(first_even)