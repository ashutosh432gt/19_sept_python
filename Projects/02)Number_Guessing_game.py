print("-------------------Tops Lottery Game-------------------")

import random  #importing random module to pick random numbers

status = True #initlization for validation of users entry

com = random.randint(1, 10)  #to pick random numbers between 1 to 10
com1 = random.randint(1, 15) #to pick random numbers between 1 to 15
com2 = random.randint(1, 20) #to pick random numbers between 1 to 20
lifelines=2 #users can use three lifelines to get hint and continue the level
print()
print("-----------------Game Rules-----------------")
print("1.You will be given limited attempts to guess the right number in each level")
print("2.You will be having two lifelines")
print("3.After redeeming Lifeline game will restart from level 1")
print()
while status:
    #limiting the attempt of user to 5
    for i in range(1, 6): 
        print("---------------Level 1---------------")
        print("Guess Number between 1 to 10")
        user = int(input("Guess a Number :- "))
        #if users guess is greater than random number picked by computer
        if user > com:
            print("Hint: Guess lower number")  #providing hint to users
        #if users guess is greater than random number picked by computer    
        elif user < com:
            print("Hint: Guess upper number") #providing hint to users
        #if users guess is right    
        else:
            print("Right guess")
            print("You are promoted to Level 2")
            print()
            print("---------------Level 2---------------")
            print("Now you have 4 attempts to clear Level 2")
            #limiting for the second level (nested loop)
            for j in range(1, 5):
                print("Guess Number between 1 to 15")
                user = int(input("Guess a Number :- "))
                #if users guess is greater than random number picked by computer
                if user > com1:
                    print("Hint: Guess lower number")  #providing hint to users
                    
                elif user < com1:
                    print("Hint: Guess upper number") #providing hint to users
                #if users guess is right     
                else:
                    print("Right guess")
                    print("You are promoted to Level 3")
                    print()
                    print("------Level 3------")
                    print("Now you have 2 attempts to clear Level 3")

                    for k in range(1, 3):
                        print("Guess Number between 1 to 10")
                        user = int(input("Enter your guess: "))
                        #if users guess is greater than random number picked by computer
                        if user > com2:
                            print("Hint: Guess lower number")  #providing hint to users
                        elif user < com2:
                            print("Hint: Guess upper number") #providing hint to users
                        #if users guess is right     
                        else:
                            print("Right Guess")
                            print("Congratulations! You have won the game")
                            status = False  #if the users guesses the right status changes to false to exit the loop
                            break   #end the loop
                    status = False #status false to stop the loop to run again
                    break #to end the loop
            status = False  
            break

    print()
    print("You have no attempts left")
    #conditional statement to end the loop
    if lifelines > 0:
        use_lifeline = input("Redeem lifeline? (yes/no): ").upper()
        if use_lifeline == "YES":
            lifelines -= 1
            print(f"You have {lifelines} lifelines left.")
            if i == 5:
                print("The correct guess for Level 1 = ",com)
            elif j == 4:
                print("The correct answer for Level 2 = ",com1)
            else:
                print("The correct answer for Level 3 = ",com2)
                
        status=True #if the users redeem's lifeline the loop runs again
        continue #to let the loop keep
    #condition if the user loose all lifelines and attempt
    if i == 5:
        print("Better Luck Next Time!")
        print("No lifelines remaining")
    elif j == 4:
        print("Better Luck Next Time!")
        print("No lifelines remaining")
    elif k == 3:
        print("Better Luck Next Time!")
        print("No lifelines remaining")
    status = False
