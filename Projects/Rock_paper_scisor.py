import random

game_list=["rock","paper","scissor"]

flag=True

while flag:
    com=random.choice(game_list)
    user=input("Choose rock / paper / scissor :- ").lower()
    for i in range(1,4):
        if user==com:
            print("Tie")
        elif user=="rock" and com=="scissor":
            print("user won the match")
        elif user=="rock" and com=="paper":
            print("Computer won the match")    
        elif user=="scissor" and com=="rock":
            print("computer won the match")    
        elif user=="scissor" and com=="paper":
            print("user won the match")
        elif user=="paper" and com=="rock":
            print("user won the match")           
        elif user=="paper" and com=="scissor":
            print("Computer won the match")    
        else:
            print("Invalid Input")
    
        
    flag=False
    break        

    