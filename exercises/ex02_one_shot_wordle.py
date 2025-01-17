"""EX02 - One Shot Wordle."""

__author__: str = "730607227"

secret_word: str = "python"

guess: str = input(f"What is your {len(secret_word)}-letter guess? ")  # receiving guess from user
while len(guess) != len(secret_word):  # making sure the guess is the correct length
    guess = input(f"That was not {len(secret_word)} letters! Try again: ") 

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
wordle_result: str = ""  # intializing our output string

while i < len(secret_word):
    if guess[i] == secret_word[i]:  # adding a green box for a correct letter
        wordle_result += GREEN_BOX 
    else:
        does_character_exist: bool = False
        rechecking_indices: int = 0
        while does_character_exist is False and rechecking_indices < len(secret_word):  # checking if the letter is in the secret word
            if guess[i] == secret_word[rechecking_indices]: 
                does_character_exist = True 
            else:
                rechecking_indices += 1
        if does_character_exist is True:  # adding a yellow box if the letter is in the word
            wordle_result += YELLOW_BOX 
        else:  # adding a white box if the ltter is not in the word
            wordle_result += WHITE_BOX
    i += 1
print(wordle_result)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
