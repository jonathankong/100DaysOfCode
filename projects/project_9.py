import os

def create_bid(name, bid, highest_bid):
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    highest_bid = bid if bid > highest_bid else highest_bid
    return name, bid, highest_bid

def main():
    name = ''
    bid = 0
    highest_bid = 0
    bidding_dict = {}
    name, bid, highest_bid = create_bid(name, bid, highest_bid)
    bidding_dict[name] = bid

    while (input("Are there any other bidders? Type 'yes' or 'no'.\n") == "yes"):
        os.system('cls')
        name, bid, highest_bid = create_bid(name, bid, highest_bid)
        bidding_dict[name] = bid

    highest_bidders = []

    for key in bidding_dict:
        if bidding_dict[key] == highest_bid:
            highest_bidders.append(key)

    print(f'The winner{" is"if len(highest_bidders) == 1 else "s are"} {" ,".join(highest_bidders)} with a bid of ${highest_bid}')