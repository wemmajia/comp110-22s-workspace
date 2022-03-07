"""Wordle."""

__author__ = "730395239"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:
    """Search for char in word."""
    assert len(char) == 1
    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns string of emojis."""
    assert len(guess) == len(secret)
    emojis: str = ""
    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            emojis += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        i += 1
    return emojis


def input_guess(length: int) -> str:
    """Prompts for guess of length."""
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    return char(a)


def main() -> None:
    """Entrypoint."""
    secret: str = "codes"
    guess: str = ""
    won: bool = False
    turn: int = 1

    while turn <= 6 and not won:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
        else:
            turn += 1
    if won:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()