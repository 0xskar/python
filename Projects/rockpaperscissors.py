# Rock, Paper, Scissors
# ---------------------
# Simple game using the random module
# made by 0xskar

import random

print("Welcome to Rock, Paper, Scissors!")

machineScore = int(0)
playerScore = int(0)
validOptions = ["Rock", "Paper", "Scissors"]

while(1):
    machineOptions = validOptions
    machineChoice = random.choice(machineOptions)

    playerChoice = input("Enter a choice: Rock, Paper, or Scissors: ")
    playerChoice = playerChoice.capitalize()
    
    while playerChoice not in validOptions:
        print("You have to choose Rock, Paper, or Scissors! Please try again.")
        playerChoice = input("Enter Rock, Paper or Scissors, please: ")
        playerChoice = playerChoice.capitalize()

    print("Computer chooses: " + machineChoice)
    print("Player chooses: " + playerChoice)

    while(machineChoice == playerChoice):
        print("Holy shit, a tie!")
        print("Time for a playoff!")
        machineChoice = random.choice(machineOptions)
        playerChoice = input("Enter a choice for playoff: Rock, Paper, or Scissors: ")
        playerChoice = playerChoice.capitalize()        
        print("Computer chooses: " + machineChoice)
        print("Player chooses: " + playerChoice)        
        if playerChoice != machineChoice:
            break

    if playerChoice == "Rock" and machineChoice == "Scissors":
        print("Rock breaks Scissors! Player wins! +1 for Player.")
        playerScore = int(playerScore + 1)
    if playerChoice == "Scissors" and machineChoice == "Paper":
        print("Scissors cuts Paper! Player wins! +1 for Player.")
        playerScore = int(playerScore + 1)
    if playerChoice == "Paper" and machineChoice == "Rock":
        print("Paper covers Rock! Player wins! +1 for Player.")
        playerScore = int(playerScore + 1)        

    if machineChoice == "Rock" and playerChoice == "Scissors":
        print("Rock breaks Scissors! Computer wins! +1 for Computer.")
        machineScore = int(machineScore + 1)
    if machineChoice == "Scissors" and playerChoice == "Paper":
        print("Scissors cuts Paper! Computer wins! +1 for Computer.")
        machineScore = int(machineScore + 1)
    if machineChoice == "Paper" and playerChoice == "Rock":
        print("Paper covers Rock! Computer wins! +1 for Computer.")
        machineScore = int(machineScore + 1)        


    print("Computer: ", machineScore)
    print("Player: ", playerScore)

    gameStatus = input("Press any key to play again, or type 'exit' to quit. ")
    gameStatus = gameStatus.lower()
    if gameStatus == 'exit':
        break


