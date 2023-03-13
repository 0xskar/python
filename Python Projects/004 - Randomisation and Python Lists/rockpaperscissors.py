import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

hands = [rock, paper, scissors]



print("Welcome to rock paper scissors")
choice = int(input("Choose: 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
while choice >= 3 or choice < 0:
    choice = int(input("Invalid number. Choose: 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

print(hands[choice])

if choice == 0 and computer_choice == 1:
    print(f"Computer Chose\n{hands[computer_choice]}\nYou Lose.")
elif choice == 1 and computer_choice == 2:
    print(f"Computer chose\n{hands[computer_choice]}\nYou Lose.")
elif choice == 2 and computer_choice == 0:
    print(f"Computer chose\n{hands[computer_choice]}\nYou Lose.")
elif choice == 0 and computer_choice == 2:
    print(f"Computer chose\n{hands[computer_choice]}\nYou Win!")
elif choice == 1 and computer_choice == 0:
    print(f"Computer chose\n{hands[computer_choice]}\nYou Win!")
elif choice == 2 and computer_choice == 1:
    print(f"Computer chose\n{hands[computer_choice]}\nYou Win!")
else:
    print(f"Computer chose\n{hands[computer_choice]}\nIt's a tie.")


