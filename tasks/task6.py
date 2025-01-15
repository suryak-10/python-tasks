# Task 6: Validate a Password

def validate_password(password):
    if len(password) < 8:
        return False
    is_upper = any(char.isupper() for char in password)
    is_lower = any(char.islower() for char in password)
    is_digit = any(char.isdigit() for char in password)
    is_special = any(char in "!@#$%^&*()-_=+[]{};:'\"|\\,.<>?/" for char in password)
    return all([is_upper, is_lower, is_digit,is_special])
print(validate_password("Vicky09."))
print(validate_password("Vicky."))
print(validate_password("vicky9."))
print(validate_password("Vicky0"))