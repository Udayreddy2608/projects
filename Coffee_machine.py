logo="""
_________         _____  _____                 ___ ___                                         
\_   ___ \  _____/ ____\/ ____\____   ____    /   |   \  ____  __ __  ______ ____              
/    \  \/ /  _ \   __\\   __\/ __ \_/ __ \  /    ~    \/  _ \|  |  \/  ___// __ \             
\     \___(  <_> )  |   |  | \  ___/\  ___/  \    Y    (  <_> )  |  /\___ \\  ___/             
 \______  /\____/|__|   |__|  \___  >\___  >  \___|_  / \____/|____//____  >\___  > /\  /\  /\ 
        \/                        \/     \/         \/                   \/     \/  \/  \/  \/ 
"""
print(logo)
menu={
    "espresso":{"water":50,"powder":18,"milk":0,"price":120},
    "latte":{"water":200,"powder":24,"milk":150,"price":200},
    "cappuccino":{"water":250,"powder":24,"milk":100,"price":240}
}
resource={"water":1000,"powder":1000,"milk":1000,"money":0}

def selection(menu,resource):
    while True:
        choice=input("Select you coffee preference:\nE-espresso\nL-latte\nC-cappuccino\n").lower()
        if choice=="e" or choice=="l" or choice=="c":
            break
    if choice=="e":
        item="espresso"
        print(f"You opted for {item}")
        k=menu[item]["price"]
        print(f"Price={k}")
        return menu[item]
    elif choice=="l":
        item="latte"
        print(f"You opted for {item}")
        k=menu[item]["price"]
        print(f"Price={k}")
        return menu[item]
    elif choice=="c":
        item="cappuccino"
        print(f"You opted for {item}")
        k=menu[item]["price"]
        print(f"Price={k}")
        return menu[item]

def sufficiency(menu,resource):
    req=selection(menu, resource)
    if req["water"]<=resource["water"] and req["powder"] <= resource["powder"] and req["milk"] <= resource["milk"]:
            return req
    else:
        return False
def collection():
    cash=0
    ten = int(input("Enter no of 10 rs notes: "))
    cash = cash + ten * 10
    twenty = int(input("Enter the no of 20 rs notes: "))
    cash = cash + twenty * 20
    fifty = int(input("Enter the no of 50 rs notes: "))
    cash = cash + fifty * 50
    hundred = int(input("Enter the no of 100 rs notes: "))
    cash = cash + hundred * 100
    hundred2 = int(input("Enter the no of 200 rs notes: "))
    cash = cash + hundred2 * 200
    hundred5 = int(input("Enter the no of 500 rs notes: "))
    cash = cash + hundred5 * 500
    return cash

def transaction(menu,resource):
    while True:
        chosen=sufficiency(menu,resource)
        if chosen==False:
            print("Insufficient Resources")
            break
        else:
            k=chosen["price"]
            paid=collection()
        if k==paid:
            print("Enjoy your coffee!!\nThank you...Visit again!!")
        elif k<paid:
            print("Enjoy your coffee\nThank you...Visit again!!")
            print(f"Please collect your change {paid-k} rs")
        elif k>paid:
            print("Insufficient funds")
        for i in resource:
            if i!="money":
                resource[i]-=chosen[i]
            elif i=="money":
                resource[i]+=k
        print(resource)
        while True:
            customer=input("Is there any customer? (Y-yes/N-no)").lower()
            if customer=="y" or customer=="n":
                    break
        if customer=="y":
            transaction(menu,resource)
        else:
            break

transaction(menu,resource)
