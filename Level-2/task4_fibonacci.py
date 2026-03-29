def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Taking input
terms = int(input("Enter number of terms: "))

if terms <= 0:
    print("Please enter a positive number")
else:
    fibonacci(terms)