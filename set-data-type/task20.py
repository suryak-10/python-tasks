# Task 10: Remove All Elements from a Set if it Contains a Specific Element
# Sample Input:
#     Set: {10, 20, 30, 40, 50}
#     Element to Check: 30
# Expected Output:
#     Output: "Set is cleared." (Set: set())

set1 = {10, 20, 30, 40, 50}
element_to_check = 30
if element_to_check in set1:
    set1.clear()
    print("Set is cleared.", "(Set:", set1,")")