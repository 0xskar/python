import random

print("Random Number Generator Game")

player1 = input("Name of Player 1: ")
player2 = input("Name of Player 2: ")
player3 = input("Name of Player 3: ")

player1roll = random.randint(0, 100)
player2roll = random.randint(0, 100)
player3roll = random.randint(0, 100)

print(player1, "rolls a", player1roll)
print(player2, "rolls a", player2roll)
print(player3, "rolls a", player3roll)

if player1roll > player2roll > player3roll :
    print("player1 wins with a", player1roll)

if player2roll > player3roll > player1roll :
    print("player2 wins with a", player2roll)

if player3roll > player2roll > player1roll :
    print("player3 wins with a", player3roll)


