# Star of Dawn
# Text Based RPG
# Errol Vogt 2023

import random
import time
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle


# Curses Module Commands Reference
#
#   curses.newwin(a, b, c, d)   - creates new window                        a = window cell height from top
#   curses.clear()              - clears screen                             b = window cell width from le
#   curses.refresh()            - refreshes screen                          c = cells from the top
#   curses.getch()              - waits for and gets a user input           d = cells from the right
#
#   rectangle(curses, a, b, c, d)   a = Start (Cells from Top)
#                                   b = Start (Cells from Left)
#                                   c = Rectangle Height
#                                   d = Rectangle Width
#
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
        self.score = 0


class Player2:
    def __init__(self, name: str):
        self.name = name
        self.roll = 0
        self.money = 0
        self.score = 0


# Curses Windows
def window_title(RED_AND_BLACK):
    window_title_location = curses.newwin(5, 50, 0, 0)
    window_title_location.refresh()
    rectangle(window_title_location, 0, 0, 3, 49)
    window_title_location.addstr(1, 17, f'+ Star of Dawn +', RED_AND_BLACK)
    window_title_location.addstr(2, 12, f' Chapter 1: Ashen Queen', RED_AND_BLACK)
    window_title_location.refresh()


def dice_game(player1_name, player1_money, player2_name, player2_money, rounds):
    player1 = Player1(player1_name)
    player2 = Player2(player2_name)

    player1.money = main_character.money
    if player2.name == companion_one.name:
        player2.money = companion_one.money

    # windows and colors
    window_dice_game_title = curses.newwin(0, 37, 0, 55)
    window_dice_game_body = curses.newwin(0, 37, 4, 55)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    RED_AND_BLACK = curses.color_pair(1)
    BLUE_AND_BLACK = curses.color_pair(2)
    GREEN_AND_BLACK = curses.color_pair(3)

    # Title Rectangle and Window
    window_dice_game_title.clear()
    rectangle(window_dice_game_title, 0, 0, 3, 36)
    window_dice_game_title.addstr(1, 14, f'+ Dice +', BLUE_AND_BLACK)
    window_dice_game_title.addstr(2, 11, f'Game of Chance', BLUE_AND_BLACK)
    window_dice_game_title.refresh()
    window_dice_game_body.clear()
    window_dice_game_body.addstr(0, 0, f'How much do you wager?')
    window_dice_game_body.addstr(2, 0, f'You have {player1.money}, and {player2.name} has {player2.money}.')
    window_dice_game_body.refresh()
    window_dice_game_body.getch()

    # Wager Rectangle and window
    while wager is not int:
        try:
            window_dice_game_wager = curses.newwin(0, 20, 14, 55)
            window_dice_game_wager.addstr(0, 0,'Enter a number: ')
            wager_box = Textbox(window_dice_game_wager)
            window_dice_game_wager.refresh()
            wager_box.edit()
            wager = int(wager_box.gather().strip())
            window_dice_game_wager.getch()

            dice_round = 0
            break        
        except :
            ValueError
    
    for i in range(rounds):
        dice_tie = 0
        dice_round += 1
        window_dice_game_body.clear()
        window_dice_game_body.addstr(0, 0, f'Round {dice_round}')
        player1.roll = random.randint(1, 10)
        window_dice_game_body.addstr(2, 0, f'{player1.name} rolls a {player1.roll}.')
        player2.roll = random.randint(1, 10)
        window_dice_game_body.addstr(3, 0, f'{player2.name} rolls a {player2.roll}.')

        #Wager window
        window_dice_game_wager.clear
        window_dice_game_wager.refresh
        window_dice_game_wager.addstr(0,0, f'{player1.name} wagers {wager}.')

        if player1.roll > player2.roll:
            window_dice_game_body.addstr(0, 30, f'WIN!!!', GREEN_AND_BLACK)
            window_dice_game_body.addstr(5, 0, f'{player1.name} wins with {player1.roll}')
            window_dice_game_body.addstr(7, 0, f'{player1.name}: {player1.score}')
            window_dice_game_body.addstr(8, 0, f'{player2.name}: {player2.score}')
            player1.score += 1
            window_dice_game_body.refresh()
            window_dice_game_body.getch()
        elif player1.roll < player2.roll:
            window_dice_game_body.addstr(0, 30, f'LOSS!!!', RED_AND_BLACK)
            window_dice_game_body.addstr(5, 0, f'{player2.name} wins with {player2.roll}')
            window_dice_game_body.addstr(7, 0, f'{player1.name}: {player1.score}')
            window_dice_game_body.addstr(8, 0, f'{player2.name}: {player2.score}')
            player2.score += 1
            window_dice_game_body.refresh()
            window_dice_game_body.getch()
        elif player1.roll == player2.roll:
            window_dice_game_body.addstr(0, 30, f'TIE!!!', BLUE_AND_BLACK)
            window_dice_game_body.addstr(5, 0, f'{player1.name} and {player2.name} tie with a {player1.roll}.')
            window_dice_game_body.addstr(7, 0, f'{player1.name}: {player1.score}')
            window_dice_game_body.addstr(8, 0, f'{player2.name}: {player2.score}')
            window_dice_game_body.refresh()
            window_dice_game_body.getch()

    if player1.score > player2.score:
        window_dice_game_body.clear()
        window_dice_game_body.addstr(5, 0, f'Player 1 wins the game.')
        window_dice_game_body.refresh()
        window_dice_game_wager.clear
        window_dice_game_wager.addstr(0,0, f'{player1.name} wins {wager}.')
        window_dice_game_wager.refresh
        window_dice_game_wager.getch()
    elif player1.score < player2.score:
        window_dice_game_body.clear()
        window_dice_game_body.addstr(5, 0, f'Player 1 loses the game.')
        window_dice_game_body.refresh()
        window_dice_game_wager.clear()
        window_dice_game_wager.addstr(0,0, f'{player1.name} loses {wager}.')
        window_dice_game_wager.refresh()
        window_dice_game_wager.getch()


# Sleep function
def sleep(sec):
    time.sleep(sec)


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
    window_boat_scene.addstr(11, 10, f'--== Press Any Key ==--')

    window_boat_scene.refresh()
    window_boat_scene.getch()

    # meeting companion one in the galley
    window_boat_scene.clear()
    window_boat_scene.addstr(0, 0, f'Meeting {companion_one.name} in the Galley. The Barkeep is there as well.'
                                   f'They challenge you to round of dice, you love dice so accept it with no delay.')
    window_boat_scene.addstr(11, 10, f'--== Press Any Key ==--')
    window_boat_scene.refresh()
    window_boat_scene.getch()

    # ask how much to wager and how many rounds (divisible)
    rounds = 100
    dice_game(main_character.name, main_character.money, companion_one.name, companion_one.money, rounds)

    # calculate if lost a lot of the wager to insult, and if not to congratulate
    window_boat_scene.clear()
    window_boat_scene.addstr(0, 0,
                             f'"What a great way to pass the time there {main_character.name}. Says {companion_one.name}. '
                             f'You big dog you just won that game and should have {main_character.money} now!'
                             f'You two decide to get ready to depart the galley when the cook, who always gave you a '
                             f'bad feeling comes at you with a cleaver!')
    window_boat_scene.refresh()
    window_boat_scene.getch()


# main function. curses and colors and other variables
def main(stdscr):
    # colors
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    RED_AND_BLACK = curses.color_pair(1)
    BLUE_AND_BLACK = curses.color_pair(2)
    GREEN_AND_BLACK = curses.color_pair(3)

    # Screen Boxes

    window_title(RED_AND_BLACK)
    scene_boat()


curses.wrapper(main)

