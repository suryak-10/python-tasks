# Task 7: Check if a String Ends with a Specific Substring
# Sample Input:
#     String: "Hello, World!"
#     Substring to Check: "World!"
# Expected Output:
#     Output: "The string ends with 'World!'."

string = "Hello, World!"
substring = "World!"

if string.endswith(substring):
    print(f"The string ends with '{substring}'.")
else:
    print(f"The string not ends with '{substring}'.")