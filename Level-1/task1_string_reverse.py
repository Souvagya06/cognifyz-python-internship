def reverse_string(text):
    return text[::-1]


# Taking user input
user_input = input("Enter a string: ")

# Calling function
reversed_text = reverse_string(user_input)

# Output
print("Reversed string:", reversed_text)