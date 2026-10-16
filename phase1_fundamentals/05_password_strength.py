import string

def is_valid_password(password):
    if len(password) < 8:
        return False
    

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    return all([has_upper, has_lower, has_digit, has_symbol])

password = input("Enter password: ")
print(is_valid_password(password))
    