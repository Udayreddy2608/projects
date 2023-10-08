import random
l=[]
output=[0,1,2,3,4,6,"wd","nb","wic"]
team1=input("Enter team_one name: ").upper()
team2=input("Enter team_two name: ").upper()
l.append(team1)
l.append(team2)
overs=int(input("Enter the number of overs: "))
balls=overs*6
wickets=10
toss=random.choice(l)
l.remove(toss)
print(f"{toss} won the toss.")
while True:
    dec=input("press B to bat first or C to bowl first ")
    if dec=='b' or dec=='B':
        bat=toss
        print(f"{toss} won the toss and have decided to bat first")    
        break 
    else:
        bowl=toss
        print(f"{toss} won the toss and have decided to bowl first")
        break
def bat_first(balls,wickets,first_inns):
    score=0
    f=0
    while balls!=0:
        next=input("Press enter to play: ")
        ball=random.choice(output)
        print(ball)
        if ball==0 or ball==1 or ball==2 or ball==3 or ball==4 or ball==6:
            score=score+ball
            print(f"{first_inns}: {score}-{f}")
            balls=balls-1
        elif ball=="wd" or ball=="nb":
            score=score+1
            print(f"{first_inns}: {score}-{f}")
        elif ball=="wic":
            wickets=wickets-1
            balls=balls-1
            f=f+1
            print(f"{first_inns}: {score}-{f}")
        if wickets==0 or balls==0:
            break
    return score
if dec=="b" or dec=="B":
    first_inns=toss
    second_inns=l[0]
else:
    first_inns=l[0]
    second_inns=toss
total=bat_first(balls,wickets,first_inns)
print(f"{first_inns} scored {total} runs in {overs} overs")
target=total+1
print(f"{second_inns} needs {target} runs to win in {balls} balls")

def bat_second(balls,wickets,overs,target):
    score=0
    f=0
    while balls!=0:
        next_ball=input("Press enter to play: ")
        ball=random.choice(output)
        print(ball)
        if ball==0 or ball==1 or ball==2 or ball==3 or ball==4 or ball==6:
            score=score+ball
            print(f"{second_inns}: {score}-{f}")
            balls=balls-1
        elif ball=="wd" or ball=="nb":
            score=score+1
            print(f"{second_inns}: {score}-{f}")
        elif ball=="wic":
            wickets=wickets-1
            balls=balls-1
            f=f+1
            print(f"{second_inns}: {score}-{f}")
        if score>=target:
            j=wickets-f
            print(f"{second_inns} won by {j} wickets with {balls} balls left ")
            break
        if wickets==0 or balls==0:
            return score
    return score
second=bat_second(balls,wickets,overs,target)
if total>second:
    diff=total-second
    print(f"{first_inns} won by {diff} runs ")
elif total==second:
    print("Match drawn!!")


        



