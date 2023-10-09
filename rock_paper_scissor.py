#rock,paper scissors

import random
rock=0
paper=1
scissor=2
list=[rock,paper,scissor]

Your_choice=int(input("Enter your choice: type 0 for rock,1 for paper,2 for scissor):"))
computer_choice=random.choice(list)
print(f"Computer chose {computer_choice}")

if(Your_choice>2 or Your_choice<0):
     print("invalid input")
elif(Your_choice==computer_choice):
    print("It is a Draw")

elif(Your_choice==0):
        if(computer_choice==1):
            print("computer wins!!!")
        else:
            print("You Win!!!")
elif(Your_choice==1):
        if(computer_choice==0):
            print("YOU WIN!!!")
        else:
            print("Computer Wins!!!!!!")
else:
     if(computer_choice==0):
          print("Computer Wins!!!")
     else:
          print("YOU WIN!!!")
        
     
    









    
 
        
    


