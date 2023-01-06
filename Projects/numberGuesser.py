# 2 games in 1
#
# Player chooses a number
# Program tries to guess players number
# 

import random

redo = 1

while(redo == 1):
    randomNum = int(input("Input a number between 1 and 10 and the program will try to guess... "))

    while(redo) == 1:
        if int(randomNum) < 1 or int(randomNum) > 10:
            redo = 1
            print("Sorry, you have to guess betweenn 1 and 10")
            randomNum = input("Try again...Enter another: ")
        else:
            redo = 0 

    randomNumGuess = random.randint(1, 10)
    print("Computer guesses:", randomNumGuess)

    if randomNumGuess == randomNum:
        print("The computer guessed your number!")
    else:
        print("The computer couldn't guess your number!")

    tryagain = input("Try again? Y/N: ")
    if tryagain == "Y" or tryagain == "y": 
        redo = 1
    else:
        exit