

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