# Task 14: Check if a String Contains Only Letters
# Sample Input:
#     String: "Hello"
# Expected Output:
#     Output: "The string contains only letters."

def alphanumeric(string):
    if string.isalpha():
        return "The string contains only letters."
    else:
        return "The string contains non-letters."
str = "Hello"
print(alphanumeric(str))