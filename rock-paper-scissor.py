import random

list_of_move = ["rock", "paper", "scissor"]

while True:
    user_choice = input("enter your move: ").lower()  # added () to call lower()
    
    if user_choice == "exit":
        print("game exited")
        break
    
    if user_choice not in list_of_move:
        print("try again!")
        continue

    comp_choice = random.choice(list_of_move)  # moved inside the loop after input validation
    print(f"you have choose: {user_choice} & computer choose: {comp_choice}")

    if user_choice == comp_choice:
        print("its a draw")
    elif user_choice == "paper":
        if comp_choice == "rock":   #condition 1
            print("paper win")
        else:                       #condition 2
            print("scissor win")
            
    elif user_choice == "rock":
        if comp_choice == "paper":  #condition 1
            print("paper win")
        else:                        #condition 2
            print("rock win")
            
    elif user_choice == "scissor":
        if comp_choice == "paper":  #condition 1
            print("scissor win")
        else:                        #condition 2
            print("rock win") 
    else:
        print("something went wrong")
