#password generator program
'''
o/p format:
welcome to the password generator!
how many letters would you like in your password?
how many symbols would you like in your password?
how many numbers would you like in you password?
process finished with exit code 0
'''


import random
print("welcome to the password generator!!")
password=[]
yourpassword=""
numberlist=[1,2,3,4,5,6,7,8,9,0]
letterslist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symlist=['!','@','#','$','%','&','*','(',')']
letters=int(input("how many letters would you like in your password?"))
print(letters)
numbers=int(input("how many numbers would you like in you password?"))
print(numbers)
symbols=int(input("how many symbols would you like in your password?"))
print(symbols)
for i in range(letters):
    l=random.choice(letterslist)
    password+=l
for j in range(numbers):
    n=random.choice(numberlist)
    strn=str(n)
    password+=strn
for k in range(symbols):
    s=random.choice(symlist)
    password+=s
print(password)
random.shuffle(password)
for m in password:
    yourpassword=yourpassword+m
print(yourpassword)

