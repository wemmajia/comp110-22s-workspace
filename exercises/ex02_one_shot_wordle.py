"""One shot wordle."""

__author__ = "730395239"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "python"

guess: str = input(f"What is your {len(secret)}-letter guess? ")

while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

i: int = 0
emojis: str = ""

while i < len(secret):
    if secret[i] == guess[i]:
        emojis += GREEN_BOX
    else:
        exists: bool = False
        j: int = 0
        while not exists and j < len(secret):
            if guess[i] == secret[j]:
                exists = True
            else:
                j += 1
        if exists:
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
    i += 1

print(emojis)

if secret == guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")