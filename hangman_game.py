'''
RULES:

'''
import random
generated=[]
wordlist=["mercedes","porsche","bugatti","alfaromeo","audi","toyota","suzuki","nissan","hyundai","kia"]
word=random.choice(wordlist)
lives=6
count=len(word)
for i in range(count):
    generated+='_'
print(generated)
while(lives!=0):
    guess=input("Please guess a letter: ")
    for j in range (count):
        if(guess==word[j]):
            generated[j]=guess
    print(generated)
    if(guess not in word):
        lives=lives-1
        if(lives==0):
            print("out of lives...GAME OVER!!")
    if('_' not in generated):
        print("You Win")
        lives=0
 
    
        
    





        






