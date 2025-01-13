# storage_tasks.py

# Task 1: Calculate the Average of a List of Numbers
def calculate_average(numbers):
    if not numbers:
        return 0  # Return 0 for an empty list
    return sum(numbers) / len(numbers)




# Task 2: Find the Second Largest Number in a List
def second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements for second largest
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort(reverse=True)  # Sort in descending order
    return unique_numbers[1]




# Task 3: Count Words in a Sentence
def word_count(sentence):
    words = sentence.split()
    counts = {}
    for word in words:
        word = word.lower()  # Make it case-insensitive
        counts[word] = counts.get(word, 0) + 1
    return counts




# Task 4: Check for Prime Numbers in a Range
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True




def primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]




# Task 5: Generate Fibonacci Sequence
def fibonacci(n):
    if n <= 0:
        return []
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]




# Task 6: Validate a Password
def validate_password(password):
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[]{};:'\"|\\,.<>?/" for char in password)
    return all([has_upper, has_lower, has_digit, has_special])




# Task 7: Create a Factorial Using Memoization
factorial_cache = {}

def memoized_factorial(n):
    if n in factorial_cache:
        return factorial_cache[n]
    if n == 0 or n == 1:
        return 1
    result = n * memoized_factorial(n - 1)
    factorial_cache[n] = result
    return result





# Task 8: Find Common Elements in Two Lists
def common_elements(list1, list2):
    return list(set(list1) & set(list2))