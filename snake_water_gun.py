# Snake vs Water → Snake drinks water → Snake wins
# Water vs Gun → Water damages gun → Water wins
# Gun vs Snake → Gun kills snake → Gun wins
# Same choice → It’s a Draw

import random

choices = ["snake", "water", "gun"]

user = input("choose, snake/water/gun: ")

computer = random.choice(choices)

print(f"you choose [{user}] and,\n computer choose [{computer}]")

if user == computer:
    print("its a draw")
    
elif(user == "snake" and computer == "water" ) or (user == "gun" and computer == "snake") or (user == "water" and computer == "gun"):
    print("you win😎, computer loose")
    
else:
    print("computer win, you loose😿")