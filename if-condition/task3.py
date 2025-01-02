# Age Group Identifier


# 1. Ask the user to input their age.
# 2. Determine their age group:
#    - 0-12: Child
#    - 13-19: Teenager
#    - 20-59: Adult
#    - 60 and above: Senior

import sys
age = int(input("Please enter a age:"))
if age < 0:
    print("negative numbers not accepted")
    sys.exit()
if age >= 0 and age < 12:
    print("child")
elif age >= 13 and age < 19:
    print("teenager")
elif age >= 20 and age < 59:
    print("adult")
else:
    print("senior")