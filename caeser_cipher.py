alphabet=['a','b','c','d','e','f','g','h','i','j','k',
          'l','m','n','o','p','q','r','s','t','u','v',
          'w','x','y','z','a','b','c','d','e','f','g',
          'h','i','j','k','l','m','n','o','p','q','r',
          's','t','u','v','w','x','y','z']
from cipher_art import logo #logo from cipher_art.py
print(logo)
def caeser(text,shift,choice):
    final_text=""
    old_index=0
    new_index=0
    if choice=="e":
        for i in text:
            if i in alphabet:
                old_index=alphabet.index(i)
                new_index=old_index+shift
                final_text=final_text+alphabet[new_index]
            else:
                final_text=final_text+i
            
        print("The encoded message is:\n"f"{final_text}")
    elif choice=="d":
        for i in text:
            if i in alphabet:
                old_index=alphabet.index(i)
                new_index=old_index-shift
                final_text=final_text+alphabet[new_index]
            else:
                final_text=final_text+i
        print("The decoded message is:\n"f"{final_text}")
while True:
    choice=input("type 'e' to encrypt, 'd' to decrypt :").lower()
    text=input("Enter the message:\n").lower()
    shift=int(input("Enter the shift size:\n"))
    shift=shift%26
    caeser(text,shift,choice)
    ask=input("Do you want to test again\n(Y to do again)\n(N to stop):\n").lower()
    if ask=="n":
        print("Thank You\nGoodbye!!!")
        break



    

    
