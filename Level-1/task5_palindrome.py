def is_palindrome(text):
    # Normalize: remove spaces and make lowercase
    text = text.replace(" ", "").lower()
    return text == text[::-1]


# Taking input
user_input = input("Enter a string: ")

# Checking
if is_palindrome(user_input):
    print("It is a palindrome")
else:
    print("Not a palindrome")