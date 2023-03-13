print(" _____________________________________________ ")
print("|.'',        Choose Your Adventure        ,''.|")
print("|.'.'',                                 ,''.'.|")
print("|.'.'.'',                             ,''.'.'.|")
print("|.'.'.'.'',                         ,''.'.'.'.|")
print("|.'.'.'.'.|                         |.'.'.'.'.|")
print("|.'.'.'.'.|===;                 ;===|.'.'.'.'.|")
print("|.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|")
print("|.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|")
print("|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|")
print("|,',',',',|---|',|'|???????|'|,'|---|,',',',',|")
print("|.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|")
print("|.'.'.'.'.|---|','   /%%%\   ','|---|.'.'.'.'.|")
print("|.'.'.'.'.|===:'    /%%%%%\    ':===|.'.'.'.'.|")
print("|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|")
print("|.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|")
print("|.'.'.','        /%%%%%%%%%%%\        ','.'.'.|")
print("|.'.','         /%%%%%%%%%%%%%\         ','.'.|")
print("|.','          /%%%%%%%%%%%%%%%\          ','.|")
print("|;____________/%%%%%Spicer%%%%%%\____________;|")
print("\nWelcome to Treasure Island.")
print("Your mission is to find the treasure")
print("You're at a cross road, where do you want to go? Type \"left\" or \"right\".")
choice = input()
if choice == "left":
    print("You come to a lake. There is a island in the middle of the lake. Type \"wait\" to wait for a boat or "
          "\"swim\" to swim across.")
    choice = input()
    if choice == "wait":
        print("You arrive at the island unharmed. There is a house with three doors. One red, one yellow, one blue. "
              "Which color do you choose?")
        choice = input()
        if choice == "yellow":
            print("You found the treasure and win!")
        elif choice == "red":
            print("You enter a room full of fire. Game over.")
        else:
            print("the blue door is full of water and you drown, Game over")
    else:
        print("You try to swim across but you get eaten by piranhas. Game over.")
else:
    print("You run into a trap and are killed! Game over.")
