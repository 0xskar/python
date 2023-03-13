# Write your code below this line 👇
def prime_checker(number):
    prime = 0
    for num in range(1, number + 1):
        if number % num == 0:
            prime += 1
    print(f"The number has {prime} numbers divisible with no remainder")
    if prime > 2:
        print(f"{number} is not a prime number.")
    else:
        print(f"{number} is a prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
