

number = int(input("What number do you want to check? "))

is_equal = number % 2

if is_equal == 1:
    print(f"{number} is not equal.")
else:
    print(f"{number} is equal.")