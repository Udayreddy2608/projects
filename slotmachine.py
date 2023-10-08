MAX=50000
MIN=1000
LINES=5
import random

line=[2,2,2,2,5,5,5,5,0,0,0,0,0,0,]
def deposit():
    while True:
        balance=int(input("Enter the deposit amount: "))
        if balance<MIN:
            print("You are not eligible to play: ")
        else:
            break
    return balance

def total_lines():
    while True:
        lines=int(input("Enter the number of lines you want to bet on: "))
        if 1<=lines<=LINES:
            break
        else:
            print(f"Enter number of lines from 1 to {LINES}")
    return lines

def bet():
    while True:
        bet=int(input("Enter the amount you want to bet: "))
        if bet<MIN or bet>MAX:
            print(f"enter the bet in the range of {MIN} and {MAX}")
        else:
            break
    return bet
def main(balance):
    lines=total_lines()
    spin=0
    win=0
    while True:
        stake=bet()
        total=lines*stake
        if total>balance:
            print(f"Your bet amount exceeds your wallet balance: Your balance is {balance}")
        else:
            break
    balance=balance-total
    print(f"Your betting amount per line is {stake}, on {lines} lines. Total bet amount is {total}")
    choice=input("Are you ready to spin: [Y/N]")
    if choice=="Y" or choice=='y':
        outcomes=[]
        for i in range(lines):
            spin=random.choice(line)
            outcomes.append(spin)
            win=win+(stake*spin)
        print(outcomes)
        print(f"Your winnings is {win}rs")
    balance=balance+win
    return balance
def choice():
    balance=deposit()
    balance=main(balance)
    print(f"current balance is {balance} rs")
    while True:
        while True:
            play=input("Press p to play again or q to quit")
            if play=="p" or play=="P":
                break
            if play=="q" or play=="Q":
                break
        if play=="p" or play=="P":
            balance=main(balance)
        else:
            break
    print(f"You left with {balance} rs in your wallet")
    cashout=input("Press c to cashout: ")
    while True:
        if cashout=="c" or cashout=="C":
            print(f"Successfully cashed out {balance}/- rs")
            print("Thank You For Playing!!!")
            break
choice()







    
    
