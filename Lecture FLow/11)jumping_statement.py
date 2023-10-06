"""
there are 2 types of jumping statement

---> break
---> continue

break -> to break the loop
continue -> to skip the loop

"""

status=True
result=""
while status:
    for i in range (1,6):
        marks=int(input("Enter your marks :- "))
        if marks > 35:
            result="Pass"
            print("Pass")
        else:
            result="Fail"
            print("Fail") 
            break
    name=input("Enter your name :- ")
    print("{} you are {}".format(name,result))
    choice=input("Do you want to add more student detail :- ").upper()
    if choice=="N":
        status=False          
               