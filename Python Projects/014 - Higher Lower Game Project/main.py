from art import logo, vs as vs_art
from game_data import data
import random
from replit import clear

# Higher lower game
#
# TODO-1 - starts the game
# TODO - Have the screen refresh after every input
# TODO - Pull 2 people from data that are not the same and remove them from list so they dont repeat
# TODO - Ask to compare who has more followers and continue until wrong


def compare_people(player_score):
    """ Pull 2 people from data that are not the same and remove them from list so they don't repeat """
    selected_people = []
    if player_score > 0:
        print(f"You're right! Current score: {player_score}")
    while len(selected_people) < 2:
        choice = random.choice(data)
        selected_people.append(choice)
        data.remove(choice)
    # print(selected_people[0])
    print(f"Compare A: {selected_people[0]['name']}, a {selected_people[0]['description']}, from {selected_people[0]['country']}.")
    print(vs_art)
    # print(selected_people[1])
    print(f"Against B: {selected_people[1]['name']}, a {selected_people[1]['description']}, from {selected_people[1]['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if selected_people[0]['follower_count'] > selected_people[1]['follower_count'] and guess == "A":
        return 1
    elif selected_people[0]['follower_count'] < selected_people[1]['follower_count'] and guess == "B":
        return 1
    else:
        return 0


def higher_lower_game():
    playing = True
    player_score = 0
    while playing:
        print(logo)
        if compare_people(player_score) == 1:
            player_score += 1
        else:
            print(f"You lose. Final score: {player_score}")
            return
        clear()
    return


higher_lower_game()
