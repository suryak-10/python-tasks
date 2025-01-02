# Task 6: List Duplicates Counter
# Sample Input:
#     User Input: "apple, banana, apple, cherry, banana, apple"
# Expected Output:
#     Duplicates Count: {"apple": 3, "banana": 2}
from importlib.resources.readers import remove_duplicates

a="apple","banana","apple","cherry","banana","apple"
fruits  = ["apple","banana","apple", "mango", "cherry","banana","apple", "mango", 'audi']

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

result = {}

for key, value in fruit_count.items():
    print(key, value)
    if value > 1:
        result[key] = value

print(result)