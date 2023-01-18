# Star of Dawn
# Text Based RPG
# Errol Vogt 2023

import random
import time
import curses
from curses import wrapper

# Curses Module
# 
#           clear screen:       stdscr.clear()
#           refresh screen:     stdscr.refresh()
#           end program on key: stdscr.getch()
#           new window:         curses.newwin(5, 25, 0, 0)
#
# Curses Colors


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
        self.money = 850
        self.experience = 0


main_character = MainCharacter("Oskar")


# Classify companion 1
class CompanionOne:
    def __init__(self, name: str):
        self.name = name
        self.health_points = 20
        self.strength = 10
        self.dexterity = 13
        self.intelligence = 8
        self.wisdom = 13
        self.money = 2523


companion_one = CompanionOne("Grant")


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




# Mini Games
#
# Dice Game
class Player1:
    def __init__(self, name: str):
        self.name = name
        self.roll = 0
        self.money = 0


class Player2:
    def __init__(self, name: str):
        self.name = name
        self.roll = 0
        self.money = 0



def dice_game(player1_name, player1_money, player2_name, player2_money, rounds):
    player1 = Player1(player1_name)
    player2 = Player2(player2_name)
    window_dice_game = curses.newwin(0,0,0,55)
    window_dice_game.clear()
    for i in range(rounds):
        i = i + 1
        window_dice_game.addstr(0, 0, f'--------------------------------')
        window_dice_game.addstr(1, 0, f'+              Dice            +')
        window_dice_game.addstr(2, 0, f'--------------------------------')
        window_dice_game.addstr(3, 0, f'{player1_name}, {player1_money}. {player2_name}, {player2_money}. Round {rounds}')
        player1.roll = random.randint(1, 10)
        window_dice_game.addstr(4, 0, f'{player1.name} rolls a {player1.roll}.')
        player2.roll = random.randint(1, 10)
        window_dice_game.addstr(5, 0, f'{player2.name} rolls a {player2.roll}.')
        window_dice_game.addstr(15, 0, f'--== Press any key to roll ==--')
        window_dice_game.refresh()
        window_dice_game.getch()
        rounds = rounds - 1
        
    



# Sleep function
def sleep(sec):
    time.sleep(sec)


# Curses Windows
def window_title(RED_AND_BLACK):
    window_title_location = curses.newwin(5, 50, 0, 0)
    window_title_location.clear()
    window_title_location.addstr(0, 0, f'--------------------------------------------------')
    window_title_location.addstr(1, 0, f'+           Star of Dawn - Introduction          +', RED_AND_BLACK)
    window_title_location.addstr(2, 0, f'--------------------------------------------------')
    window_title_location.refresh()
    


# Game Scenes
def scene_boat():
    window_boat_scene = curses.newwin(12, 50, 4, 0)
    window_boat_scene.clear()
    window_boat_scene.addstr(0, 0, f'You are Xavendir, a famous hero from the lands of Veren. '
                                   f'Currently aboard the Ashen Queen, about to arrive at the port of Justiucia. '
                                   f'A shipmate has just woken you up, "Xavendir, we\'ll be at port in a few hours, '
                                   f'cap\'n send for ya, wants to talk to ya before to depart." '
                                   f'So, you decide that it\'s time to get up, big day ahead of you, '
                                   f'as you need to prepare for your contract.'
                                   f'Put on your clothes, your sword and sheathe and head on into the galley to see if {companion_one.name}, '
                                   f'your friend, is up as well.')
    window_boat_scene.addstr(11, 0, f'       --== Press Any Key to Continue ==--')

    window_boat_scene.refresh()
    window_boat_scene.getch()

    # meeting companion one in the galley
    window_boat_scene.clear()
    window_boat_scene.addstr(0,0, f'Meeting {companion_one.name} in the Galley. The Barkeep is there as well.'
                                  f'They challenge you to round of dice, you love dice so accept it with no delay.')
    window_boat_scene.addstr(11, 0, f'       --== Press Any Key to Continue ==--')
    window_boat_scene.refresh()
    window_boat_scene.getch()

    
    # dice game
    dice_game(main_character.name, main_character.money, companion_one.name, companion_one.money, 3)

    # calculate if lost a lot of the wager to insult, and if not to congratulate
    print(
        f'"What a great way to pass the time there {main_character.name}. Says {companion_one.name}. '
        f'You big dog you just won that game and should have {main_character.money} now!')
    print(
        f'You two decide to get ready to depart the galley when the cook, who always gave you a bad feeling '
        f'comes at you with a cleaver!')


# main function. curses and colors and other variables
def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    RED_AND_BLACK = curses.color_pair(1)
    window_title(RED_AND_BLACK)
    scene_boat()
    
    
wrapper(main)

