import random

'''
1 for snake
-1 for water
0 for gun 
'''

computer=random.choice([-1,0,1])
youstr=input("Enter your choice: ")
youDict={'s': 1,'w':-1,'g':0}

reverseDict={1:'Snake',-1:'Water',0:'Gun'}
you=youDict[youstr]

print(f"your Choice {reverseDict[you]} \n Computer choice {reverseDict[computer]}")

if computer==you:
    print("Its a draw!!")
else:
    # if(computer==-1 and you==1): computer-you==-2
    #     print("You  Win!! \n Computer lose")
    # elif(computer==-1 and you==0): computer-you==-1
    #     print("You lose!! \n Computer  Win!!")
    # elif(computer==1 and you==-1):computer-you==2
    #     print("You lose!! \n Computer  Win!!")
    # elif(computer==0 and you==-1):computer-you==1
    #     print("You lose!! \n Computer  Win!! ")
    # elif(computer==1 and you==-1):computer-you==1
    #     print("You lose!! \n Computer  Win!! ")
    # elif(computer==1 and you==0):computer-you==1
    #     print("You  Win!! \n Computer lose!!")
    
    
    
    
    if((computer-you) ==-1 or (computer-you) ==2):
        print("You loose")
    else:
        print("You win")