import random

print("Random Number Generator Game")

player1 = input("Name of Player 1: ")
player2 = input("Name of Player 2: ")
player3 = input("Name of Player 3: ")

print(player1, "rolls a", random.randint(0, 100))
print(player2, "rolls a", random.randint(0, 100))
print(player3, "rolls a", random.randint(0, 100))

