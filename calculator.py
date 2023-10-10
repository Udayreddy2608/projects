#UDAYREDDY
import os
logo=("""
 _____________________
|  _________________  |
| | UDAYREDDY    0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
)

def calculator():
    print(logo)
    def add(n1,n2):
        return n1+n2
    def sub(n1,n2):
        return n1-n2
    def mul(n1,n2):
        return n1*n2
    def div(n1,n2):
        return n1/n2
    def pow(n1,n2):
        return n1**n2
    n1=float(input("enter first number: "))
    while True:
        operation=input("Select operation: \n+\n-\n*\n/\n^\n")
        n2=float(input("enter second number: "))
        cal={"+":add(n1,n2),
            "-":sub(n1,n2),
            "*":mul(n1,n2),
            "/":div(n1,n2),
            "^":pow(n1,n2),
            }
        value=cal[operation]
        print(f"{n1} {operation} {n2} = {value}")
        while True:
            further=input("Do you want to continue further?(Y-Yes/N-No)").lower()
            if further=="y" or further=="n":
                break
        if further=="y":
            n1=value
        else:
            os.system("clear")
            calculator()
calculator()