import random
#creating a list of numbers 
all_numbers = list(range(1, 13))
#genrating computers list which contains six numbers
Anjali_Mam = random.sample(all_numbers, 6)

name=input("Enter your name :- ")
#running loop for not getting same number in both lists
for num in Anjali_Mam:
    all_numbers.remove(num)
user = random.sample(all_numbers, 6)
print("Anjali_Mam's numbers = ", Anjali_Mam)
print(f"{name} numbers = {user}")

status=True
#while condition to validate entry and generate random numbers multiple times
while status:
    com = random.randint(1, 12)
    print()
    #applying condtional statement to check and remove numbers from the list
    if com in user:
        print("Random number picked = ",com)
        user.remove(com)
        
        print(f"{name} has {com} \n{name} remaining numbers: {user}")
        #applying conditional statement if user list has no numbers lefts
        if not user:
            print("User wins")
            break

    elif com in Anjali_Mam:
            print("Random number picked = ",com)
            Anjali_Mam.remove(com)
            
            print(f"Anjali_Mam has {com} \nAnjali_Mam's remaining numbers: {Anjali_Mam}")
            #applying conditional statement if computer generated list has no numbers lefts
            if not Anjali_Mam:
                print("Anjali_Mam wins")
                break  
    else:
        print(f"The Number {com} is alredy picked : Press Enter to pick random number again")            
        
    input()
              
   
        