from art import logo
from replit import clear
import random


def deal_card():
    """ Deals a random card from deck and returns card """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def score_check(hand):
    """ Checks if a score is less than 21 """
    for card in hand:
        if card == 11 and sum(hand) > 21:
            hand.remove(card)
            hand.append(1)
    if sum(hand) > 21:
        return 1
    elif sum(hand) == 21:
        return 0


def game(players_hand, computers_hand):
    player_stand = False
    while sum(players_hand) < 21 and sum(computers_hand) < 21:
        print(f"    Your cards: {players_hand}, current score: {sum(players_hand)}")
        print(f"    Computer's first card: {computers_hand[1]}")
        hit_me = input("Type 'y' to get another card, type 'n' to stand: ").lower()
        if hit_me == "y":
            players_hand.append(deal_card())
            score_check(players_hand)
        else:
            player_stand = True
        if sum(computers_hand) < 16:
            computers_hand.append(deal_card())
            score_check(computers_hand)
        if player_stand == True and sum(computers_hand) <= 21:
            computers_hand.append(deal_card())
            score_check(computers_hand)
    print(f"    Your final hand: {players_hand}, final score: {sum(players_hand)}")
    print(f"    Computer's final hand: {computers_hand}, final score: {sum(computers_hand)}")
    if sum(computers_hand) > 21:
        print("Computer Busts! You win!")
    elif sum(players_hand) > 21:
        print("You bust, you lose.")
    elif score_check(players_hand) == 0:
        print("Player Blackjack!")
    elif score_check(computers_hand) == 0:
        print("Dealer Blackjack!")

play_game = True
while play_game:
    player_hand = []
    computer_hand = []
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game == "y":
        clear()
        print(logo)
        player_hand = [deal_card(), deal_card()]
        computer_hand = [deal_card(), deal_card()]
        game(player_hand, computer_hand)
    else:
        print("Goodbye!")
        play_game = False
