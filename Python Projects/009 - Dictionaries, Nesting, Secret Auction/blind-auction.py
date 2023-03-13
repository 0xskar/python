from replit import clear
from art import logo

# HINT: You can call clear() to clear the output in the console.
bidders = []


def add_bid(bidder_name, bidder_bid):
    new_bidder = {
        "Bidder": bidder_name,
        "Bid": bidder_bid,
    }
    bidders.append(new_bidder)


print(logo)
print("Welcome to the secret auction program.")

bidding = True
while bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    add_bid(bidder_name=name, bidder_bid=bid)
    more_bidders = input("Are there any more bidders? Yes/No").lower()
    if more_bidders == "no":
        bidding = False
        clear()
    elif more_bidders == "yes":
        clear()


highest_bid = 0
for bidder in bidders:
    if bidder["Bid"] > highest_bid:
        highest_bidder = bidder["Bidder"]
        highest_bid = bidder["Bid"]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")