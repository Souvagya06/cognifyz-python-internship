import random

def number_guesser():
    print("Welcome to Number Guesser Game")

    # User defines range
    low = int(input("Enter lower limit: "))
    high = int(input("Enter upper limit: "))

    number = random.randint(low, high)
    attempts = 0

    print(f"Guess the number between {low} and {high}")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < low or guess > high:
            print("⚠️ Guess is out of range!")
            continue

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break


# Run the game
number_guesser()