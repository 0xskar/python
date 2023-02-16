# fightgame.py

import random

class MainCharacter:
    def __init__(self, name: str):
        self.name = name
        self.health_points = 20
        self.strength = 12
        self.constitution = 10
        self.dexterity = 13
        self.intelligence = 8
        self.wisdom = 13
        self.money = 850
        self.experience = 0
        
class Enemy:
    def __init__(self, name: str):
        self.name = name
        self.health_points = 20
        self.strength = 12
        self.constitution = 10
        self.dexterity = 13
        self.intelligence = 8
        self.wisdom = 13
        self.money = 850
        self.experience = 0




player = MainCharacter("Oskarnelsius")
enemy_1 = Enemy("Boar")





def main():

    print("Welcome to the fight.")
    print(f"A fight between {player.name} and {enemy_1.name}")
    print("Good Luck!")


    while True:
        try:
            wager = int(input(f"Enter a wager, you have {player.money}: "))
        except:
            print(f"Enter a correct number less then {player.money}.")
            ValueError


    # Fight 1
    if wager > player.money:
        while True:
            try:            
                wager = int(input(f"Enter a wager less than {player.money}: "))
            except:
                print(f"Enter a correct number less then {player.money}.")
                ValueError



main()