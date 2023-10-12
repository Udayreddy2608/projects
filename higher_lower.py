import random
import game_data
from game_data import data
logo="""
  _    _  _____  _____  _    _  ______  _____                  _       ____ __          __ ______  _____           
 | |  | ||_   _|/ ____|| |  | ||  ____||  __ \                | |     / __ \\ \        / /|  ____||  __ \          
 | |__| |  | | | |  __ | |__| || |__   | |__) |   ___   _ __  | |    | |  | |\ \  /\  / / | |__   | |__) |         
 |  __  |  | | | | |_ ||  __  ||  __|  |  _  /   / _ \ | '__| | |    | |  | | \ \/  \/ /  |  __|  |  _  /          
 | |  | | _| |_| |__| || |  | || |____ | | \ \  | (_) || |    | |____| |__| |  \  /\  /   | |____ | | \ \  _  _  _ 
 |_|  |_||_____|\_____||_|  |_||______||_|  \_\  \___/ |_|    |______|\____/    \/  \/    |______||_|  \_\(_)(_)(_)
                                                                                                                   
                                                                                                                   
"""
print(logo)
def high_low(data):
    a=random.choice(data)
    score=0
    while True:
        print(a["name"],",",a["description"],",",a["country"])
        print(a["follower_count"],"million followers" )
        b=random.choice(data)
        while a==b:
            b=random.choice(data)
        from game_data import vs
        print(vs)
        print(b["name"],",",b["description"],",",b["country"])
        while True:
            choose=input("Select higher(H) of lower(L)").lower()
            if choose=="h" or choose== "l":
                break
        if choose=="h":
            if b["follower_count"]>a["follower_count"]:
                score=score+1
                print(f"Score={score}")
                a=b
            elif b["follower_count"]==a["follower_count"]:
                score=score+1
                a=b
                print(f"Score={score}")
            else:
                print(f"You lose!!\nYour score is {score} points")
                print(b["name"],"has",b["follower_count"],"million followers")
                break
        elif choose=="l":
            if b["follower_count"]<a["follower_count"]:
                score=score+1
                print(f"Score={score}")
                a=b
            elif b["follower_count"]==a["follower_count"]:
                score=score+1
                print(f"Score={score}")
                a=b
            else:
                print(f"You lose!!\nYour score is {score} points")
                print(b["name"],"has",b["follower_count"],"million followers")
                break
    while True:
        play_again=input("Do you want to play again?? (Y/N)").lower()
        if play_again=="y" or "n":
            break
    if play_again=="y":
        high_low(data)
high_low(data)