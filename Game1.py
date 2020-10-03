import random

def decide_win(comp_choice,player_choice):
    if comp_choice=='r':
        if player_choice=='r':
            return None
        elif player_choice=='p':
            return True
        else:
            return False

    elif comp_choice=='p':
        if player_choice=='p':
            return None
        elif player_choice=='r':
            return False
        else:
            return True

    elif comp_choice=='s':
        if player_choice=='s':
            return None
        elif player_choice=='r':
            return True
        else:
            return False

random_no=random.randint(0,2)
#print(comp_choice)

player_choice=input("Enter your choice r-rock, p-paper, s-scissors: ")
if random_no==0:
    comp_choice='r'
elif random_no==1:
    comp_choice='p'
elif random_no==2:
    comp_choice='s'



if player_choice=='r' or player_choice=='p' or player_choice=='s':
    w=decide_win(comp_choice,player_choice)
else:
    print("Invalid choice, pls enter r/p/s !!!")

print(f"You have entered {player_choice}")
print(f"Computer has entered {comp_choice}")

if (w==None):
    print("Game tied!")
elif (w):
    print("You won!!!!!")
else:
    print("Sorry, better luck next time!")

