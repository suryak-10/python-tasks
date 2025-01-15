# Task 8: Find Common Elements in Two Lists

def common_elements(list1, list2):
    return list(set(list1) & set(list2))
print(common_elements([2,4,7,3],[4,8,2,6]))