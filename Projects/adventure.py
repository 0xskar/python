# Star of Dawn
# Text Based RPG
# Errol Vogt 2023

import random
import time

# Character Stats  These range from about 3 to 20.
#
# "Physical" statistics
#
#     Strength - measuring physical power and carrying capacity
#     Constitution - measuring endurance, stamina and good health
#     Dexterity - measuring agility, balance, coordination and reflexes
#
# "Mental" statistics

#     Intelligence - measuring deductive reasoning, cognition, knowledge, memory, logic and rationality
#     Wisdom - measuring self-awareness, common sense, restraint, perception and insight
#     Charisma - measuring force of personality, persuasiveness, leadership and successful planning

# Classify main character
class MainCharacter:
    def __init__(self, name: str):
        self.name = name
        self.health_points = 20
        self.strength = 12
        self.constitution = 10
        self.dexterity = 13
        self.intelligence = 8
        self.wisdom = 13
        self.money = 1322
        self.experience = 0


main_character = MainCharacter("Xavendir Alenndin")
print(f"Your character name: {main_character.name}")
print(f"Your wisdom is: {main_character.wisdom}")


# Classify companion 1
class CompanionOne:
    def __init__(self, name: str):
        self.name = name
        self.health_points = 20
        self.strength = 10
        self.dexterity = 13
        self.intelligence = 8
        self.wisdom = 13
        self.money = 1223


companion_one = CompanionOne("Akkar Venvaris")
print(f"Friends name: {companion_one.name}")
print(f"They have {companion_one.wisdom} wisdom.")


# Classify Enemy1
class LevelOneEnemy:
    def __init__(self, name: str):
        self.name = name
        self.health_points = 12
        self.strength = 10
        self.dexterity = 13
        self.intelligence = 8
        self.wisdom = 13


# Level 1 Monsters
barkeep = LevelOneEnemy("Barkeep")
fly = LevelOneEnemy("Fly")
maiden = LevelOneEnemy("Maiden")




# Mini Games
#
# Dice Game
class DicePlayer:
        def __init__(self, name: str):
            self.name = name
            self.score = 0
            self.roll = 0
            self.wager = 0


def dice_game(player1, player2, wager, replay):

    while True:
        try:
            wager = int(input(f'Enter number less than {main_character.money}: '))
            break
        except ValueError:
            print('Enter a correct number.')


    while wager > main_character.money:
        print(f'You dont have enough, try less.')
        while True:
            try:
                wager = int(input(f'Enter number less than {main_character.money}: '))
                break
            except ValueError:
                print('Enter a correct number.')
            

    player1 = DicePlayer(player1)
    player2 = DicePlayer(player2)
    round_counter = 0

    print(f'Dice game.')
    print(f'Wagering {wager}.')

    while (player1.score < 2) and (player2.score < 2):
        print(f'----------------------------------')
        print(f'{player1.name} score: {player1.score}')
        print(f'{player2.name} score: {player2.score}')
        print(f'Round {round_counter + 1}')
        sleep(1)
        player1.roll = random.randint(1, 10)
        print(f'{player1.name} rolls {player1.roll}')
        player2.roll = random.randint(1, 10)
        print(f'{player2.name} rolls {player2.roll}')
        sleep(1)

        if player1.roll > player2.roll:
            player1.score = player1.score + 1
            print(f'{player1.name} wins, has {player1.score}.')
        elif player1.roll < player2.roll:
            player2.score = player2.score + 1
            print(f'{player2.name} wins, has {player2.score}.')
        else:
            print(f'Tis a tie')
        round_counter+=1
    if player1.score == 2:
        print(f'----------------------------------')
        print(f'You won the game! You wagered {wager}.')
        main_character.money = main_character.money + wager
        print(f'You now have {main_character.money}.')
        print(f'----------------------------------')
        print(f'Play again? y/n')
        replay = input('Enter Choice: ')
        if replay == "y":
            dice_game(player1.name, player2.name, main_character.money, replay)
        
    elif player2.score == 2:
        print(f'----------------------------------')
        main_character.money = main_character.money - wager
        print(f'{player2.name} has won the game, you wagered {wager}. Now you have {main_character.money}.')
        print(f'----------------------------------')
        print(f'Play again? y/n')
        replay = input('Enter Choice: ')
        if replay == "y":
            dice_game(player1.name, player2.name, main_character.money, replay)






    


# Sleep function
def sleep(sec):
    time.sleep(sec)

# Game Scenes
def scene_boat():
    print(f'--------------------------')
    print(f'Welcome to Star of Dawn')
    print(f'--------------------------')
    print(f'You are Xavendir, a famous hero from the lands of Veren.')
    print(f'Currently aboard the Ashen Queen, about to arrive at the port of Justiucia.')
    print(f'A shipmate has just woken you up, "Xavendir, we\'ll be at port in a few hours, cap\'n send for ya, '
          f'wants to talk to ya before to depart."')
    print(f'So, you decide that it\'s time to get up, big day ahead of you, as you need to prepare for your contract.')
    print(
        f'Put on your clothes, your sword and sheathe and head on into the galley to see if {companion_one.name}, '
        f'your friend, is up as well.')

    scene = "galley"

    # meeting companion one in the galley
    while scene == "galley":
        print(f'Meeting {companion_one.name} in the Galley. The Barkeep is there as well.')
        print(f'They challenge you to round of dice, you love dice so accept it with no delay.')
        print(f'How much do you wager? You have {main_character.money}')


        # dice game
        dice_game(main_character.name, companion_one.name, main_character.money, 0)



        #calculate if lost a lot of the wager to insult, and if not to congratulate
        print(
            f'"What a great way to pass the time there {main_character.name}. Says {companion_one.name}. '
            f'You big dog you just won that game and should have {main_character.money} now!')
        print(
            f'You two decide to get ready to depart the galley when the cook, who always gave you a bad feeling '
            f'comes at you with a cleaver!')

        scene = "exit"
        if scene == "exit":
            break

    # fighting
    exit("Game Over")

# checks if the code is the main program or imported. it will run if the code is imported in as a module
if __name__ == '__main__':
    # runs through the scenes
    scene_boat()
    exit("Game Over")