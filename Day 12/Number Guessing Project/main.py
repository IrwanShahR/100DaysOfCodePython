
import random

EASY_TURNS = 10
HARD_TURNS = 5

def generate_number():
    random_number = random.randint(1,100)
    return random_number


def select_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS


def process(user_number, random_number, lives_left):
    if user_number > random_number:
        print("Too high")
        return lives_left -1
    elif user_number < random_number:
        print("Too low")
        return lives_left -1
    else:
        print("You guessed the number! Congratulations")


def game():
    print("Welcome to the Number Guessing Game!"
    print("I'm thinking of a number between 1 and 100")
    answer = generate_number()
    turns = select_difficulty()
    guess = 0
    while guess != answer and turns >0:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = process(guess,answer,turns)

    print("Game Over")


game()