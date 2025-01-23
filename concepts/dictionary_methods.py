# Dictionary Operations in Python

# Creating a Dictionary
# Using curly braces
my_dict = {"key1": "value1", "key2": "value2"}
# Using the dict() constructor
my_dict_constructor = dict(key1="value1", key2="value2")



# Accessing Dictionary Elements
# Access a value by key
value = my_dict["key1"]
# Using .get() to avoid KeyError
value_with_default = my_dict.get("key1", "default_value")



# Adding or Updating Elements
# Add or update a key-value pair
my_dict["key3"] = "value3"





# Removing Elements
# Remove an item by key
removed_value = my_dict.pop("key1", None)  # Avoid KeyError if key doesn't exist
# Remove an arbitrary item
key, value = my_dict.popitem()
# Delete an item by key
del my_dict["key2"]
# Clear all items
my_dict.clear()





# Checking for Keys
# Check if a key exists
key_exists = "key1" in my_dict
# Check if a key does not exist
key_not_exists = "key1" not in my_dict






# Iterating Over a Dictionary
# Iterate over keys
for key in my_dict:
    print(f"Key: {key}")
# Iterate over values
for value in my_dict.values():
    print(f"Value: {value}")
# Iterate over key-value pairs
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")






# Dictionary Views
# Get all keys
keys = my_dict.keys()
# Get all values
values = my_dict.values()
# Get all key-value pairs
items = my_dict.items()






# Merging Dictionaries
other_dict = {"key4": "value4", "key5": "value5"}
# Using the update() method
my_dict.update(other_dict)
# Using dictionary unpacking (Python 3.9+)
merged = {**my_dict, **other_dict}






# Copying a Dictionary
# Shallow copy
shallow_copy = my_dict.copy()
# Using dict() constructor
constructor_copy = dict(my_dict)






# Other Useful Methods
# Get value or set a default if key is missing
value_or_default = my_dict.setdefault("key6", "default_value")
# Create a dictionary with default values
fromkeys_dict = dict.fromkeys(["key1", "key2"], "default_value")






# Length and Clearing
# Number of items in dictionary
dict_length = len(my_dict)
# Empty the dictionary
my_dict.clear()






# Comprehensions
# Create a dictionary using comprehension
squared_numbers = {x: x**2 for x in range(5)}






# Sorting
# Sort by keys
sorted_by_keys = dict(sorted(my_dict.items()))
# Sort by values
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))






# Advanced Dictionary Operations in Python

# Nested Dictionaries
# Creating a nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}






# Accessing values in a nested dictionary
name_person1 = nested_dict["person1"]["name"]






# Updating nested dictionary
nested_dict["person1"]["age"] = 26






# Merging Nested Dictionaries
nested_update = {
    "person1": {"location": "New York"},
    "person3": {"name": "Charlie", "age": 35}
}

for key, value in nested_update.items():
    nested_dict[key] = {**nested_dict.get(key, {}), **value}






# Dictionary with Default Values
from collections import defaultdict

default_dict = defaultdict(int)
default_dict["key1"] += 1

# Grouping Items by Key
from collections import defaultdict
items = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "carrot")]
grouped_items = defaultdict(list)
for category, item in items:
    grouped_items[category].append(item)







# Filtering a Dictionary
original_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered_dict = {k: v for k, v in original_dict.items() if v % 2 == 0}





# Inverting a Dictionary                                               --> swapping its keys and values.
original_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = {v: k for k, v in original_dict.items()}






# Counting with Dictionaries
from collections import Counter
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = Counter(data)






# Sorting a Dictionary by Key and Value
unsorted_dict = {"b": 2, "a": 3, "c": 1}
# Sort by keys
sorted_by_key = dict(sorted(unsorted_dict.items()))
# Sort by values
sorted_by_value = dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))






# ChainMap for Merging Multiple Dictionaries
from collections import ChainMap
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_chain = ChainMap(dict1, dict2)






# Accessing deeply nested dictionaries safely                                                    #-->The "get()" method allows you to provide a default value if a key is missing, so it won't raise an error.
nested_data = {"level1": {"level2": {"level3": "value"}}}
value = nested_data.get("level1", {}).get("level2", {}).get("level3", "default")






# Example Usage

if __name__ == "__main__":
    print("Original Dictionary:", my_dict)
    print("Shallow Copy:", shallow_copy)
    print("Squared Numbers:", squared_numbers)
    print("Sorted by Keys:", sorted_by_keys)
    print("Nested Dictionary:", nested_dict)
    print("Default Dictionary:", dict(default_dict))
    print("Grouped Items:", dict(grouped_items))
    print("Filtered Dictionary:", filtered_dict)
    print("Inverted Dictionary:", inverted_dict)
    print("Counter:", counter)
    print("Sorted by Key:", sorted_by_key)
    print("Sorted by Value:", sorted_by_value)
    print("Merged with ChainMap:", dict(merged_chain))
    print("Deeply Nested Value:", value)