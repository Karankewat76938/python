import random

# Rock Paper Scissors game
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 'r':
        if you=='s':
            return False
        elif you=='p':
            return True
    
    # Check for all possibilities when computer chose w
    elif comp == 'p':
        if you=='s':
            return False
        elif you=='r':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 's':
        if you=='r':
            return False
        elif you=='p':
            return True

print("Comp Turn: rock(r) paper(p) or scissor(s)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: rock(r) paper(p) or scissor(s)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")