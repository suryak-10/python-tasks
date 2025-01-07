# Task 4: Generate a Pyramid Pattern
# Sample Input:
#     Rows: 3
# Expected Output:
#       *
#      * *
#     * * *

import time

start_time = time.perf_counter()

num=1000

old = True

if old:
    for i in range(0,num):
      for j in range(0,num-i-1):
        print(end=" ")
      for j in range(0,i+1):
        stars = "*" * i
        print("* ", end=" ")
      print("\n")
else:
    total_char_len = num + (num - 1)
    for star_count in range(1, num + 1):
        spacing = star_count - 1
        char_len = star_count + spacing
        print(("* " * star_count).center(total_char_len, " "))

end_time = time.perf_counter()

execution_time = end_time - start_time
# Convert to minutes, seconds, and milliseconds
minutes = int(execution_time // 60)
seconds = int(execution_time % 60)
milliseconds = int((execution_time * 1000) % 1000)
microseconds = int((execution_time * 1000000) % 1000)

# Print the execution time in a human-readable format
print(f"Execution time: {minutes} minutes, {seconds} seconds, {milliseconds} milliseconds, {microseconds} microseconds")