# person = {
#     "name": "bob",
#     "age": 30,
#     "city": "New York",
#     "is_employed": True
# }
# print(person["name"])
# print(person["age"])
# print(person["city"])
# print(person["is_employed"])

# person = {"name": "john",
#           "age": "28"
#          }
# print(person["name"])
# print(person["age"])
# print(person.get("city"))
# print(person.get("city","N/A"))







# my_dict = {}
# my_dict["name"] = "bob"
# print(my_dict)

# my_dict = {"name":"bob","age":25}
# my_dict["age"] = 26
# print(my_dict)

# my_dict = {"name":"bob","age":25}
# my_dict.update({"age":30,"city": "chennai"})
# print(my_dict)








# my_dict = {'a': 1, 'b': 2, 'c': 3}
# del my_dict['b']
# print(my_dict)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# value = my_dict.pop('b')
# print(my_dict)
# print(value)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# value = my_dict.pop('d','keyword not found')
# print(value)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_dict.clear()
# print(my_dict)






# my_dict = {'a': 1, 'b': 2, 'c': 3}
# if 'b' in my_dict:
#     print("Key exists!")
# else:
#     print("Key does not exist!")

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# if 'b' not in my_dict:
#     print("Key exists!")
# else:
#     print("Key does not exist!")







# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key in my_dict.keys():
#     print(key)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for value in my_dict.values():
#     print(value)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key in my_dict:
#     print(key)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key in my_dict:
#     value = my_dict[key]
#     print(f"Key: {key}, Value: {value}")






# my_dict = {'a': 1, 'b': 2, 'c': 3}
# keys = my_dict.keys()
# print(keys)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# keys = list(my_dict.keys())
# print(keys)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# keys = tuple(my_dict.keys())
# print(keys)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# values = my_dict.values()
# print(values)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# items = my_dict.items()
# print(items)






# my_dict1= {'a': 1, 'b': 2}
# my_dict2= {'c': 3, 'd': 4}
# my_dict1.update(my_dict2)
# print(my_dict1)

# my_dict1= {'a': 1, 'b': 2}
# my_dict2= {'b': 3, 'd': 4}
# my_dict1.update(my_dict2)
# print(my_dict1)

# my_dict1= {'a': 1, 'b': 2}
# my_dict2= {'b': 5, 'd': 4}
# merged_dict={**my_dict1, **my_dict2}
# print(merged_dict)

# my_dict1= {'a': 1, 'b': 2}
# my_dict2= {'b': 5, 'c': 4}
# my_dict3= {'d': 1}
# merged_dict={**my_dict1, **my_dict2,**my_dict3,'e':3}                     # unpacking
# print(merged_dict)







# original_dict = {'a': 1, 'b': [2, 3], 'c': {'nested_key': 4}}
# duplicate_dict = original_dict.copy()
# duplicate_dict['a'] = 10
# duplicate_dict['b'].append(4)
# print("Original Dictionary:", original_dict)
# print("duplicate_dict:", duplicate_dict)

# original_dict = {'a': 1, 'b': [2, 3], 'c': {'nested_key': 4}}
# duplicate_dict = dict(original_dict)
# duplicate_dict['a'] = 10
# duplicate_dict['b'].append(4)
# print("Original Dictionary:", original_dict)
# print("duplicate_dict:", duplicate_dict)

# data = [('a', 1), ('b', 2), ('c', 3)]
# my_dict = dict(data)
# print(my_dict)
#
# my_dict = dict(a=1, b=2, c=3)
# print(my_dict)

# keys = ["a", "b", "c"]
# values = [1, 2, 3]
# my_dict=dict(zip(keys,values))
# print(my_dict)







# my_dict = {'a': 1, 'b': 2}
# value = my_dict.get('c', "5")
# print(value)

# my_dict = {'a': 1, 'b': 2}
# value = my_dict.get('a', 0)
# print(value)
# value = my_dict.get('c', 10)
# print(value)

# my_dict = {'name': 'Alice', 'age': 30}
# name = my_dict.get('name')
# print(name)
# city = my_dict.get('city')
# print(city)

# my_dict = {'user': 'Bob', 'status': 'active'}
# user_name = my_dict.get('user', [])
# print(user_name)
# user_age = my_dict.get('age', [])
# print(user_age)

# my_dict = {'a': 1, 'b': 2}
# print(my_dict.get('a', 0))
# print(my_dict.get('c', 0))

# keys = ['a', 'b', 'c']
# default_value = 0
# my_dict = {key: default_value for key in keys}
# print(my_dict)






# my_dict = {"a": 1, "b": 2}
# print(len(my_dict))

# my_dict.clear()
# print(my_dict)

# my_dict = {"a": 1, "b": 2, "c": 3}
# num_items = len(my_dict)
# print(num_items)

# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# print("Before clearing:", my_dict)
# my_dict.clear()
# print("After clearing:", my_dict)







# squares = {x: x**2 for x in range(1, 6)}
# print(squares)

# for x in range(1, 6):
#     print( x**2 )

# even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# print(even_squares)

# for x in range(1, 11):
#     if x % 2 == 0:
#       print(x**2)

# num_dict = {x: ("even" if x % 2 == 0 else "odd") for x in range(1, 6)}
# print(num_dict)

# for x in range(1, 6):
#     if x % 2 == 0:
#         print("even")
#     else:
#         print("odd")







# my_dict = {'c': 3, 'a': 1, 'b': 2}
# sorted_dict = sorted(my_dict)
# print(sorted_dict)

# my_dict = {'c': 3, 'a': 1, 'b': 2}
# sorted_dict = {k: my_dict[k] for k in sorted(my_dict)}
# print(sorted_dict)

# my_dict = {'c': 3, 'a': 1, 'b': 2}
# for k in sorted(my_dict):
#     print( my_dict[k] )






# nested_dict = {
#     "student1": {"name": "Alice", "age": 20, "courses": ["Math", "Science"]},
#     "student2": {"name": "Bob", "age": 22, "courses": ["History", "Math"]}
# }
#
# nested_dict["student1"]["age"] = 21
# nested_dict["student2"]["courses"].append("Art")
# print(nested_dict)

# employee = {"id": 101,
#             "details":{"name": "bob",
#                        "department": "IT",
#                        "skills": ["python","java"]
#                        }
#             }
# print(employee["id"])
# print(employee["details"]["name"])
# print(employee["details"]["department"])
# print(employee["details"]["skills"])

# nested_dict = {
#     "first_level":{
#         "second_level":{
#             "third_level":"value"
#         }
#     }
# }
# print(nested_dict['first_level']['second_level']['third_level'])

# nested_dict = {
#     "person":{
#         "name":"john",
#         "age": 30,
#         "address":{
#             "street": "123 Main St",
#             "city": "New York",
#             "pin": "10001"
#         }
#     }
# }
# print(nested_dict["person"]["name"])
# print(nested_dict["person"]["address"]["street"])

# nested_dict = {
#     "employee": {
#         "name": "Bob",
#         "role": "Engineer",
#         "department": "Sales"
#     },
#     "manager": {
#         "name": "John",
#         "role": "Manager",
#         "department": "Development"
#     }
# }
# print(nested_dict["employee"]["name"])
# print(nested_dict["manager"]["name"])
# print(nested_dict["manager"]["role"])






# nested_dict = {
#     'person': {
#         'name': 'John',
#         'age': 30,
#         'address': {
#             'street': '123 Main St',
#             'city': 'New York'
#         }
#     }
# }
# street = nested_dict['person']['address']['city']
# print(street)
# pincode = nested_dict.get('person', {}).get('address', {}).get('pincode', 'Not Found')
# print(pincode)







# data = {
#     "user":{
#         "info":{
#             "name":"john",
#             "age" : 28
#         }
#     }
# }
# data["user"]["info"]["age"] = 30
# print(data)

# data = {
#     "user":{
#         "info":{
#             "name":"john",
#             "age" : 28
#         }
#     }
# }
# data["user"]["info"]["email"] = "john123@gmail.com"
# print(data)

# data = {
#     'user': {
#         'info': {
#             'name': 'john',
#             'age': 28
#         }
#     }
# }
# data['user']['info'].update({'age': 30, 'email': 'john123@gmail.com'})
# print(data)







# dict1 = {'a': 1, 'b': {'x': 10, 'y': 20}}
# dict2 = {'b': {'y': 30, 'z': 40}, 'c': 3}
# merged = dict1 | dict2
# print(merged)

# dict1 = {'a': 1, 'b': {'x': 10, 'y': 20}}
# dict2 = {'b': {'y': 30, 'z': 40}, 'c': 3}
# dict1.update(dict2)
# print(dict1)

# def merge_dicts(dict1, dict2):
#     for key, value in dict2.items():
#         if key in dict1 and isinstance(dict1[key], dict) and isinstance(value, dict):
#             merge_dicts(dict1[key], value)
#         else:
#             dict1[key] = value
#     return dict1
#
# # Example
# dict1 = {
#     'a': 1,
#     'b': {
#         'x': 10,
#         'y': 20,
#         "data": {
#             "key1": 43,
#             "key4": 45,
#         }
#     }
# }
# dict2 = {
#     'b': {
#         'y': 30,
#         'z': 40,
#         "data": {
#             "key2": 43,
#             "key3": 45,
#         }
#     },
#     'c': 3
# }
#
# merged = merge_dicts(dict1.copy(), dict2)
# print(merged)







# data = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "carrot"), ("fruit", "orange"), ("vegetable", "spinach")]
#
# grouped = {}
# for key, value in data:
#     if key not in grouped:
#         grouped[key] = []
#     grouped[key].append(value)
#
# print(grouped)

# from collections import defaultdict
# items = [("fruit", "apple"), ("fruit", "banana"), ("vegetable", "carrot")]
# grouped_items = defaultdict(list)
# for category, item in items:
#     grouped_items[category].append(item)
#
# print(dict(grouped_items))






# my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
# filtered_dict = {k: v for k, v in my_dict.items() if v > 2}
# print(filtered_dict)

# my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
# for k, v in my_dict.items():
#     if v > 2:
#         print(v)

# my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
# filtered_dict = {k: v for k, v in my_dict.items() if k in ['a', 'c']}
# print(filtered_dict)

# my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
# for k, v in my_dict.items():
#     if k in ['a', 'c']:
#         print(v)

# my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
# filtered_dict = dict(filter(lambda item: item[1] > 2, my_dict.items()))
# print(filtered_dict)






# original = {1: 'a', 2: 'b', 3: 'c'}
# inverted = {value: key for key, value in original.items()}
# print(inverted)

# original_dict = {"a": 1, "b": 2, "c": 3}
# inverted_dict = {v: k for k, v in original_dict.items()}
# print(inverted_dict)






# data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# counts = {}
# for item in data:
#     if item in counts:
#         counts[item] += 1
#     else:
#         counts[item] = 1
# print(counts)

# from collections import Counter
#
# data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# counts = Counter(data)
# print(counts)
# print(counts.most_common(2))

# from collections import Counter
# text = "hello world"
# char_counts = Counter(text)
# print(char_counts)
# print(char_counts.most_common(2))



# my_dict = {'b': 2, 'a': 3, 'c': 1}
# sorted_by_key = dict(sorted(my_dict.items()))
# print("Sorted by key:", sorted_by_key)

# my_dict = {'b': 2, 'a': 3, 'c': 1}
# sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[0]))
# print("Sorted by value:", sorted_by_value)





# from collections import ChainMap
#
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# dict3 = {'d': 5}
# merged = ChainMap(dict1, dict2, dict3)
# print(merged['a'])
# print(merged['b'])
# print(merged['c'])
# print(merged['d'])

# from collections import ChainMap
#
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# dict3 = {'d': 5}
# merged = ChainMap(dict1, dict2, dict3)
# print(merged['a'])
# print(merged['b'])
# print(merged['c'])
# print(dict(merged))






# nested_dict = {
#     'a': {
#         'b': {
#             'c':
#                 10
#         }
#     }
# }
#
# result = nested_dict.get('a', {}).get('b', {}).get('c', None)
# print(result)  # Output: 10
#
# result = nested_dict.get('a', {}).get('x', {}).get('c', None)
# print(result)






# def safe_get(d, keys, default=None):
#     for key in keys:
#         d = d.get(key, default)
#         if d == default:
#             return default
#     return d
#
# nested_dict = {
#     'a': {
#         'b': {
#             'c':
#                 10
#         }
#     }
# }
#
# result = safe_get(nested_dict, ['a', 'b', 'c'])
# print(result)
#
# result = safe_get(nested_dict, ['a', 'b', 'x'])
# print(result)