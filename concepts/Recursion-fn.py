

nums = [13, 5, 6, 8, [24, 6, 3, 64,[1,5, [1, [1, 2, [2, 4, 3, ]],  2, 4], 6], 93,6,3], 95, 3, 3, ]
print(nums)

# for i in nums:
#     if type(i) == list:
#         for j in i:
#             # print(j)
#             if type(j) == list:
#                 for k in j:
#                     print(k)
#             else:
#                 print(j)
#     else:
#         print(i)

def print_list(elements, level):
    for element in elements:
        if type(element) == list:
            print_list(element, level+1)
        else:
            print(f"{element} in level {level}")

print_list(nums, 0)

def print_str(string, level=0):
    print(string, 1,2, 23, end=" ")
    len
    if level != 900:
        print_str(string, level + 1)

def sum(nums):
    total = 0
    for num in nums:
        total += num
    return  total

def get_total(nums):
    total = sum(nums)
    print(total)

get_total([1, 2, 5, 5])


print_str("Hello")