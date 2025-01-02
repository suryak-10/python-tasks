# Task 6: Check if a String Starts with a Specific Substring
# Sample Input:
#     String: "Hello, World!"
#     Substring to Check: "Hello"
# Expected Output:
#     Output: "The string starts with 'Hello'."

string = "Hello, World!"
substring = "Hello"

if string.startswith(substring):
    print(f"The string starts with '{substring}'.")
else:
    print(f"The string does not start with '{substring}'.")