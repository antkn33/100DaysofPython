# key=name, bid=key
import art
print(art.logo)
# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    #max(bidding_dictionary) max function
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

all_bids = {}

# TODO-3: Whether if new bids need to be added
contine_bidding = True
while contine_bidding:
    user = input("Enter your name: ").lower()
    bid = int(input("Enter your bid: $"))
    all_bids[user] = bid
    should_continue = input("Is there another user? yes or no: \n").lower()
    if should_continue == "no":
        contine_bidding = False
        find_highest_bidder(all_bids)
    elif should_continue == "yes":
        print("\n" * 20)

# TODO-4: Compare bids in dictionary



