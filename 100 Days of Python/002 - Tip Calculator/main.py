import decimal

print("Welcome to the tip calculator.")
bill_total = float(input("What was the total bill? $"))
party_size = int(input("How many people are splitting the bill?\n"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15 Percent?\n"))

tip_percentage = tip_percentage / 100
tip_addition = bill_total * tip_percentage
bill_total = bill_total + tip_addition
total = bill_total / party_size
total_rounded = round(total, 2)

print(f"Each Person should pay ${total_rounded}")
