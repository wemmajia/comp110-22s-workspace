"""Docstring."""

__author__ = "730395239"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

char: str = input("Enter a single character: ")
if len(char) != 1:
    print("Error: Character must be a single character.")
    exit()

print(f"Searching for {char} in {word}")
count: int = 0

if word[0] == char:
    print(f"{char} found at index 0")
    count += 1
if word[1] == char:
    print(f"{char} found at index 1")
    count += 1
if word[2] == char:
    print(f"{char} found at index 2")
    count += 1
if word[3] == char:
    print(f"{char} found at index 3")
    count += 1
if word[4] == char:
    print(f"{char} found at index 4")
    count += 1

if count == 0:
    print(f"No instances of {char} found in {word}")
elif count == 1:
    print(f"1 instance of {char} found in {word}")
else:
    print(f"{count} instances of {char} found in {word}")