import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True        
    

print("Comp Turn: Snake(s) Water(w) Gun(g) : ")
randNo = random.randint(1,3)
print(randNo)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
elif randNo:
    comp = "g"

you = input("Your Turn: Snake(s) Water(w) Gun(g): ")

a = gameWin(comp,you)

print(f"Computer choose {comp}")
print(f"You choose {you}")
if a == None:
    print("The game is Tie")
elif a:
    print(" You Win!")       
else:
    print("You Loss!")
           
