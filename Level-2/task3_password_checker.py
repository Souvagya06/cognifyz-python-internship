import string

def check_password_strength(password):
    strength = 0

    # Conditions
    if len(password) >= 8:
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    # Strength levels
    if strength <= 2:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Medium"
    else:
        return "Strong"


# Taking input
password = input("Enter your password: ")

# Checking strength
result = check_password_strength(password)

print("Password Strength:", result)