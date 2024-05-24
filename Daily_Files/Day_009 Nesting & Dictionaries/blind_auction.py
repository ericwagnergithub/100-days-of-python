import os
clear = lambda: os.system('cls')

from blind_action_art import logo

print(logo)
print("Welcome to the secret auction program.")

bid_list = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0 
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
    name = input("What is your name?: ")
    bid_amount =  int(input("What's your bid?: $"))
    bid_list[name] = bid_amount
    print(bid_list) #Debugging

    bid_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower
    if bid_continue == "no":
        bidding_finished = True
        print("The bidding is over.")
        find_highest_bidder(bid_list)
    elif bid_continue == "yes":
        clear()