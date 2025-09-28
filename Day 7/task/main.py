import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
win = False
display = []
for i in placeholder:
    display += i
print(display)

while not win:
    guess = input("Guess a letter: ").lower()

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for index in range(len(chosen_word)):
        letter = chosen_word[index]  # char in chosen word
        if letter == guess:
            display[index] = letter
    print(display)

    if "_" not in display:
        print("You won!")
        win = True

