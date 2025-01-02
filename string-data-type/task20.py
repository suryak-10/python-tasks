# Task 20: Check if a String is a Palindrome
# Sample Input:
#     String: "madam"
# Expected Output:
#     Output: "The string is a palindrome."

string = input("enter the word:")
if string== string[::-1]:
     print(string, "is a palindrome")
else:
     print(string, "is not a palindrome")