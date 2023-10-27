#take 5 name from users and print it
name=[]

status = True

while status : 
    for i in range(1,6):
        user_name=input("Enter Your Name :- ")
        name.append(user_name)
    status=False
        
for user_name in name:
    print(user_name)
    