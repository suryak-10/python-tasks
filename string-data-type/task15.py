# Task 15: Check if a String Contains Only Alphanumeric Characters
# Sample Input:
#     String: "Hello123"
# Expected Output:
#     Output: "The string contains only alphanumeric characters."

def alphanumeric(string):
    if string.isalnum():
        return "The string contains only alphanumeric characters."
    else:
        return "The string contains non-alphanumeric characters."
str = "Hello123"
print(alphanumeric(str))