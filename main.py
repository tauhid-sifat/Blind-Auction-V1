from replit import clear
from art import logo
print(logo)
#HINT: You can call clear() to clear the output in the console.
finish_bid=False
record={}
winner=""
winning_bid=0

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not finish_bid:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    record[name]=price
    next = input("Are there any other bidders? Type 'Y' or 'N'.\n").lower()
    if next=="y":
        clear()
    elif next=="n":
        finish_bid=True
        highest_bidder(record)

"""
FAQ: My console doesn't clear()

This will happen if you’re using an IDE other than replit. 

"""