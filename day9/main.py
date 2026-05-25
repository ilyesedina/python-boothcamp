# Run python code with: python3 main.py
from art import logo

print(logo)
print("Welcome to the Silent Bidding Auction Program!")

# Todo 1: Ask the user to input a word
# name = input("What is your name? ")
# price = int(input("What is your bid? $"))

# Create a dictionary to store the name and bid
bids = {}

# Todo 2: Save the input in a dictionary 
# bids[name] = price

# Todo 3: Whether if new bids need to be added or not 

continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n ").lower()
    if should_continue != "yes":
        continue_bidding = False

# Todo 4: Find the highest bidder and print the result
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

find_highest_bidder(bids)