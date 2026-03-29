def is_valid_email(email):
    # Check if '@' exists and only once
    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    # Username and domain should not be empty
    if not username or not domain:
        return False

    # Domain should contain at least one '.'
    if "." not in domain:
        return False

    return True


# Taking input
email = input("Enter an email: ")

# Checking validity
if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")