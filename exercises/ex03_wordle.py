"""EX03 - Structured Wordle."""

__author__ = "730607227"

def contains_char(search_string: str, letter: str) -> bool:
    """Determine if a letter is contained within a string."""
    assert len(letter) == 1
    i: int = 0
    while i < len(search_string):
        if search_string[i] == letter:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns string of emojis based on the same system as exercise 2."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    output_string: str = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            output_string += GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                output_string += YELLOW_BOX
            else:
                output_string += WHITE_BOX
        i += 1
    return output_string


def input_guess(expected_length: int) -> str:
    """Obtaining a guess of the correct length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 1
    has_user_won: bool = False

    while turn < 7 and has_user_won is False:  # running each turn
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            has_user_won = True
        else:
            turn += 1

    if has_user_won:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()