from art import logo
import random
from replit import clear

# Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


EASY_MODE = 10
HARD_MODE = 5


def game_mode():
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if mode == "easy":
        return EASY_MODE
    else:
        return HARD_MODE


def guessing(mode, number):
    rounds_left = mode + 1
    for r in range(0, mode):
        rounds_left -= 1
        print(f"You have {rounds_left} attempts remaining to guess the answer.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print("You win!")
            return
        elif guess > number:
            print("Number is Lower...")
        elif guess < number:
            print("Number is higher...")
    print("You Lose :(")


def game():
    playing = True
    while playing:
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        number = random.randint(1, 100)
        guessing(mode=game_mode(), number=number)
        clear()


game()
