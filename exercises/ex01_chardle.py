"""EX01 - Chardle -  A cute step toward Wordle."""

__author__ = "730607227"

input_word = input("Enter a 5-character word: ")
if len(input_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
input_char = input("Enter a single character: ")
if len(input_char) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + input_char + " in " + input_word)

count = 0
if input_char == input_word[0]:
    print(input_char + " found at index 0")
    count += 1
if input_char == input_word[1]:
    print(input_char + " found at index 1")
    count += 1
if input_char == input_word[2]:
    print(input_char + " found at index 2")
    count += 1
if input_char == input_word[3]:
    print(input_char + " found at index 3")
    count += 1
if input_char == input_word[4]:
    print(input_char + " found at index 4")
    count += 1

if count == 0:
    print("No instances of " + input_char + " found in " + input_word)
elif count == 1:
    print("1 instance of " + input_char + " found in " + input_word)
else:
    print(str(count) + " instances of " + input_char + " found in " + input_word)