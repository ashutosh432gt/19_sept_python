#calculator

def addition ():
    a=int(input("Enter Number 1 :- "))
    b=int(input("Enter Number 2 :- "))
    
    ans= a+b
    
    print("Addition of {} + {} = {}".format(a,b,ans))
    
def substraction ():
    a=int(input("Enter Number 1 :- "))
    b=int(input("Enter Number 2 :- "))
    
    ans= a-b
    
    print("Substraction of {} + {} = {}".format(a,b,ans))
    
def Multiplication ():
    a=int(input("Enter Number 1 :- "))
    b=int(input("Enter Number 2 :- "))
    
    ans= a*b
    
    print("Multiplication of {} + {} = {}".format(a,b,ans))
    
def Division ():
    a=int(input("Enter Number 1 :- "))
    b=int(input("Enter Number 2 :- "))
    
    ans= a/b
    
    print("Division of {} + {} = {}".format(a,b,ans))    
    
menu="""
        MENU
      1)Addition
      2)Substraction
      3)Multiplication
      4)Division  
"""       
print(menu)     

choice=int(input("Enter your choice :- "))

if choice==1:
    addition()
elif choice==2:
    substraction()
elif choice==3:
    Multiplication()
elif choice==4:
    Division()
else:
    print("Invalid Input")                