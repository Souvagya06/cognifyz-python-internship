def count_words(filename):
    word_count = {}

    try:
        with open(filename, "r") as file:
            text = file.read().lower()

            # Remove punctuation
            for char in ".,!?;:\"'()[]{}":
                text = text.replace(char, "")

            words = text.split()

            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

        # Sort and display
        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print("File not found!")


# Input file name
filename = input("Enter file name: ")

count_words(filename)