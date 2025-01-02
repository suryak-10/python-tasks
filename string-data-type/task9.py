# Task 9: Remove Whitespace from a String
# Sample Input:
#     String: "   Hello, Python!   "
# Expected Output:
#     String without leading/trailing whitespace: "Hello, Python!"

string = "   Hello,     Python!   "
a = string.strip()
print(f'String without leading/trailing whitespace: "{a}"')