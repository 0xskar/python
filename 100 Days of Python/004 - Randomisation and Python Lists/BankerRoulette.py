import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

number_of_elements = len(names) - 1
bill_payer = names[random.randint(0, number_of_elements)]

print(f"It looks like {bill_payer}, will pay the bill today.")


person_to_pay = random.choice(names)

print(f"looks like {person_to_pay} will actually pay jk")