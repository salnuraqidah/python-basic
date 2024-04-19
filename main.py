import re

def validate_password(password):
    # Check if password contains at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False
    # Check if password contains at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False
    # Check if password contains at least one number
    if not re.search(r"\d", password):
        return False
    # Check if password has at least 6 characters
    if len(password) < 6:
        return False
    return True

while True:
    password = input("Enter your password: ")
    if validate_password(password):
        print("Password is valid!")
        break
    else:
        print("Password is not valid. Please try again.")

