from concepts.functions import list_total

list_values = [1, "2", 57, "23", 85]

# list operations types
# 1. Updates or edits original list
# 2. Returns updates list
# 3. Search in original list

# list_values.()


# ---- Mutating Original List ----

# Push: Add to the end of the list
numbers = [1, 2, 3]
numbers.append(4)  # Push
print(numbers)  # [1, 2, 3, 4]

# Pop: Remove from the end of the list
numbers = [1, 2, 3, 4]
numbers.pop()  # Pop
print(numbers)  # [1, 2, 3]

# Shift: Remove the first element
numbers = [1, 2, 3, 4]
first = numbers.pop(0)  # Shift
print(numbers)  # [2, 3, 4]
print(first)  # 1

# Unshift: Add to the start of the list
numbers = [2, 3, 4]
numbers.insert(0, 1)  # Unshift
print(numbers)  # [1, 2, 3, 4]

# Splice: Add or remove elements
numbers = [1, 2, 3, 4]
numbers[1:3] = [9, 10]  # Splice
print(numbers)  # [1, 9, 10, 4]

# Reverse: Reverse the list
numbers = [1, 2, 3, 4]
numbers.reverse()  # Reverse
print(numbers)  # [4, 3, 2, 1]

# Sort: Sort the list
numbers = [4, 2, 1, 3]
numbers.sort()  # Sort
print(numbers)  # [1, 2, 3, 4]







# ---- Producing New Lists ----

# Map: Transform elements
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))  # Map
print(squared)  # [1, 4, 9, 16]

# Filter: Keep elements based on condition
numbers = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # Filter
print(evens)  # [2, 4]

# Flat: Flatten nested lists
nested = [[1, 2], [3, 4]]
flat = [item for sublist in nested for item in sublist]  # Flat
print(flat)  # [1, 2, 3, 4]

# FlatMap: Flatten and map                                                    --
nested = [[1, 2], [3, 4]]
flat_mapped = [x * 2 for sublist in nested for x in sublist]  # FlatMap
print(flat_mapped)  # [2, 4, 6, 8]

# Slice: Create a sub-list
numbers = [1, 2, 3, 4]
subset = numbers[1:3]  # Slice
print(subset)  # [2, 3]






# ---- Producing Single Values ----

# Reduce: Reduce to a single value                                               --
from functools import reduce
numbers = [1, 2, 3, 4]


from list_functions import  list_total as lt
from list_functions import  square as sq

total = reduce(lt, numbers, 0)  # Reduce

total1 = reduce(sq, numbers, [])  # Reduce
print("reduce fn value for square: ", total)  # 10



fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]


fruit_count = {
    "apple": 0,
    "banana": 0,
    "cherry": 0
}

print(fruits[0], fruit_count['banana'])

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 0
    fruit_count[fruit] = fruit_count[fruit] + 1


def fruits_counter(acc, fruit):
    if fruit in acc:
        acc[fruit] += 1
    else:
        acc[fruit] = 1
    return acc

fruits_count = reduce(fruits_counter, fruits, {})
print("Fruits reduce fn result :", fruits_count, end="\n")

# total = 0
# for num in numbers:
#     total += num
#
total = reduce(list_total, numbers)  # Reduce
print("reduce fn value: ", total)  # 10

# Find: Find the first matching element
numbers = [1, 2, 3, 4]
first_even = next((x for x in numbers if x % 2 == 0), None)  # Find
print(first_even)  # 2

# FindIndex: Find the index of the first matching element
numbers = [1, 2, 3, 4]
index = next((i for i, x in enumerate(numbers) if x % 2 == 0), -1)  # FindIndex
print(index)  # 1






# ---- Checking Conditions ----

# Some: Check if any element matches
numbers = [1, 2, 3, 4]
has_even = any(x % 2 == 0 for x in numbers)  # Some
print(has_even)  # True

# Every: Check if all elements match
numbers = [1, 2, 3, 4]
all_positive = all(x > 0 for x in numbers)  # Every
print(all_positive)  # True

# Includes: Check if an element exists
numbers = [1, 2, 3, 4]
includes_three = 3 in numbers  # Includes
print(includes_three)  # True






# ---- Producing Strings ----

# Join: Join elements into a string
words = ["Hello", "World"]
sentence = " ".join(words)  # Join
print(sentence)  # "Hello World"






# ---- Producing Indices ----

# IndexOf: Find the first index of an element
numbers = [1, 2, 3, 4]
index = numbers.index(3)  # IndexOf
print(index)  # 2

# LastIndexOf: Find the last index of an element
numbers = [1, 2, 3, 2, 4]
last_index = len(numbers) - 1 - numbers[::-1].index(2)  # LastIndexOf
print(last_index)  # 3




# ---- Combining Lists ----

# Concat: Combine lists
numbers1 = [1, 2]
numbers2 = [3, 4]
combined = numbers1 + numbers2  # Concat
print(combined)  # [1, 2, 3, 4]