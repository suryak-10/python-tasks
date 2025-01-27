# Python tasks covering variables, operators, conditional statements, loops, functions, and file operations.

# Task 1: Create a program that accepts a list of dictionaries containing details about employees (name, age, salary).
# Calculate the average salary of employees above the age of 30 and store the result in a file.
# Sample Input: [{"name": "John", "age": 35, "salary": 50000}, {"name": "Jane", "age": 28, "salary": 60000}]
# Sample Output File Content: Average salary of employees above 30: 50000

# Task 2: Write a program to perform matrix addition and matrix multiplication on two given matrices.
# Sample Input:
# Matrix A: [[1, 2], [3, 4]]
# Matrix B: [[5, 6], [7, 8]]
# Sample Output: Sum = [[6, 8], [10, 12]], Product = [[19, 22], [43, 50]]

# Task 3: Create a program to find the longest word in a given file.
# Sample Input File Content: "Python programming is interesting."
# Sample Output: Longest word: "programming"

# Task 4: Develop a function that generates all prime numbers within a range and writes them to a file.
# Sample Input: Range 10 to 50
# Sample Output File Content: 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47

# Task 5: Create a program that accepts a text file and calculates the frequency of each word, saving the result in another file.
# Sample Input File Content: "Hello world! Hello Python."
# Sample Output File Content: "Hello: 2, world: 1, Python: 1"

# Task 6: Create a function to parse a CSV file containing student records (name, marks in 3 subjects).
# Calculate the total and average marks for each student and write the result to another CSV file.
# Sample Input File Content:
# Name,Math,Science,English
# John,80,75,90
# Jane,85,95,80
# Sample Output File Content:
# Name,Total,Average
# John,245,81.67
# Jane,260,86.67

# Task 7: Write a program that checks if a folder contains duplicate files based on content.
# If duplicates exist, list the file names and sizes.
# No sample input/output required.

# Task 8: Create a program to zip all .txt files in a folder and extract them to another folder.
# No sample input/output required.

# Task 9: Write a program to generate a list of Fibonacci numbers up to a user-defined number.
# Save the results to a file and include the sum of all numbers in the sequence.
# Sample Input: 50
# Sample Output File Content: Fibonacci Sequence: 0, 1, 1, 2, 3, 5, ..., 34. Sum: 88

# Task 10: Develop a function that finds all anagrams of a word in a given text file.
# Sample Input File Content: "listen silent enlist inlets"
# Sample Input Word: "listen"
# Sample Output: Anagrams: silent, enlist, inlets

# Task 11: Create a program to recursively list all files and folders in a directory and save the output to a file.
# Sample Output File Content:
# Folder: /example
# -- File: file1.txt
# -- File: file2.txt
# -- Folder: subfolder
# ---- File: file3.txt

# Task 12: Write a function to read a large file in chunks and calculate the number of occurrences of a specific word.
# Sample Input: File: "largefile.txt", Word: "Python"
# Sample Output: Occurrences of 'Python': 42

# Task 13: Create a program to merge the contents of multiple text files into one file without duplicates.
# Sample Input: file1.txt, file2.txt, file3.txt
# No sample output required.

# Task 14: Develop a program to validate email addresses from a text file.
# Save all valid email addresses to another file.
# Sample Input File Content: "test@example.com, invalid_email, hello@world.com"
# Sample Output File Content: "test@example.com, hello@world.com"

# Task 15: Write a program to generate a report of the top 5 most frequent characters in a file (excluding spaces).
# Sample Input File Content: "Hello World"
# Sample Output: Most frequent characters: l: 3, o: 2, e: 1, h: 1, r: 1

# Task 16: Create a function that reads a JSON file containing product details (name, price, quantity).
# Calculate the total value of all products and save it to another JSON file.
# Sample Input File Content: [{"name": "A", "price": 10, "quantity": 2}, {"name": "B", "price": 20, "quantity": 1}]
# Sample Output File Content: {"Total Value": 40}

# Task 17: Write a program to encrypt and decrypt a file using a basic cipher (e.g., Caesar cipher).
# Sample Input File Content: "Python is fun"
# Sample Output File Content (Encrypted): "Sbwkrq lv ixq"

# Task 18: Create a program that simulates a simple text-based to-do list application using file operations.
# Options: Add task, View tasks, Delete task, Mark task as complete.
# No sample input/output required.

# Task 19: Write a program to monitor changes in a folder (new file creation, deletion, modification) and log the changes.
# No sample input/output required.

# Task 20: Develop a program to split a large text file into smaller files, each containing a maximum of N lines.
# Sample Input: File: "largefile.txt", Lines per file: 100
# No sample output required.

# Save this file as "advanced_tasks.py" and provide it to your junior to complete each task step by step.







# Task 21: Create a function to detect palindromic sentences from a file, ignoring spaces, punctuation, and case.
# Sample Input File Content: "A man, a plan, a canal, Panama. Hello world."
# Sample Output: Palindromic Sentences: "A man, a plan, a canal, Panama"

# Task 22: Write a program to implement a LRU (Least Recently Used) cache mechanism for file reads.
# No sample input/output required.

# Task 23: Develop a program that reads a text file containing dates in different formats.
# Normalize all dates to the format YYYY-MM-DD and save them to a new file.
# Sample Input File Content: "12/31/2023, 2023-Jan-01, 01-01-2023"
# Sample Output File Content: "2023-12-31, 2023-01-01, 2023-01-01"

# Task 24: Create a function that compresses and decompresses text files using the gzip module.
# Sample Input File Content: "This is a test."
# Sample Output File (Compressed): Binary gzip content
# Sample Output File (Decompressed): "This is a test."

# Task 25: Write a program to find and replace all occurrences of a given word in a text file.
# Save the modified content to a new file.
# Sample Input: Word to replace: "Python", Replace with: "Java"
# Sample Input File Content: "Python is great. Python is fun."
# Sample Output File Content: "Java is great. Java is fun."

# Task 26: Develop a program that calculates the similarity between two text files using cosine similarity.
# Sample Input: file1.txt, file2.txt
# Sample Output: Cosine Similarity: 0.85

# Task 27: Write a program to identify and delete all empty folders in a directory.
# No sample input/output required.

# Task 28: Create a function to generate a random password based on user-defined constraints (length, special characters, etc.).
# Save the generated password to a file.
# Sample Output: Password: "A!3gk9&"

# Task 29: Write a program to calculate the execution time of sorting algorithms (e.g., bubble sort, quick sort) on large datasets.
# Save the results to a file.
# Sample Output File Content: "Bubble Sort: 15.6s, Quick Sort: 2.3s"

# Task 30: Create a program to perform a recursive search for a specific text pattern across all files in a directory.
# Save the results (file name and line number) to a file.
# Sample Input: Pattern: "def"
# Sample Output File Content: "File: script.py, Line: 10"

# Task 31: Develop a function to read two CSV files and find common rows based on a specific column.
# Save the common rows to a new CSV file.
# Sample Input: Column: "ID"
# Sample Output File Content: Rows with matching IDs

# Task 32: Write a program to generate a histogram from the frequency of words in a text file.
# Sample Input File Content: "Apple Apple Banana Orange"
# Sample Output: Histogram displayed in console or saved to a file

# Task 33: Create a function that identifies broken links in an HTML file and saves the report to a new file.
# Sample Input File Content: "<a href='http://example.com'>Example</a> <a href='http://brokenlink.com'>Broken</a>"
# Sample Output File Content: "Broken Links: http://brokenlink.com"

# Task 34: Write a program to scrape weather data from a website (use a mock website or file if internet access isn't available).
# Save the data to a JSON file.
# Sample Output File Content: {"Temperature": "25°C", "Humidity": "60%"}

# Task 35: Develop a program that tracks file changes (additions, deletions, modifications) and automatically syncs the updates to a backup folder.
# No sample input/output required.

# Task 36: Write a program to convert text files to PDF format.
# Sample Input: file.txt
# Sample Output: file.pdf

# Task 37: Create a function to extract the top 10 most frequently occurring phrases (n-grams) in a text file.
# Sample Input File Content: "Data science is fun. Data science is powerful."
# Sample Output: "Top Phrases: ['Data science': 2, 'is fun': 1, 'is powerful': 1]"

# Task 38: Develop a program to generate random test data (e.g., names, emails, dates) and save it to a CSV file.
# Sample Output File Content:
# Name,Email,Date
# John Doe,john@example.com,2023-12-31

# Task 39: Write a program to implement a multi-threaded file downloader.
# No sample input/output required.

# Task 40: Create a program that calculates the Levenshtein distance between strings in a file and writes the results to another file.
# Sample Input File Content: "Python, Java, C++"
# Sample Output File Content: "Python-Java: 5, Python-C++: 6"
