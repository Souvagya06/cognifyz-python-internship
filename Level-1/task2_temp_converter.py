def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


# Taking input
temp = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").strip().upper()

# Conversion logic
if unit == "C":
    result = celsius_to_fahrenheit(temp)
    print("Temperature in Fahrenheit:", result)

elif unit == "F":
    result = fahrenheit_to_celsius(temp)
    print("Temperature in Celsius:", result)

else:
    print("Invalid unit! Please enter C or F.")