import os
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
participats={}
while True:
    name=input("Enter bidder's name:\n")
    amount=int(input("Enter bidding amount in ₹: "))
    participats[name]=amount
    add_bidder=input("Are there any more bidders?:(Y for yes N for no)").lower()
    if add_bidder=="y":
        os.system('clear')
    elif add_bidder=="n":
        break
highest_bid=0
highest_bidder=""
for bidder in participats:
    bid_amount=participats[bidder]
    if bid_amount>highest_bid:
        highest_bid=bid_amount
        highest_bidder=bidder
print(f"Auction won by {highest_bidder} for {highest_bid}/- rs")

    


