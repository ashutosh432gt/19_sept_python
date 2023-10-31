'''
conditional statements:-

1)If statement

    if condition:   
        true statement
    
For example :-
    
marks=int(input("Enter your marks :- "))

if marks>70:  #condition
        print("You will get a car")  #true statement        
        
2)If else statement :-
    if condition:        
        True statement
    
    else:
        False statement    
 
For example :-
        
if marks>70:  #condition
        print("You will get a car")  #true statement 
else:
        print("You will get rickshaw")        #False statement      
        
#even or odd number
num=int(input("Enter a number : "))

if num%2==0:
         print("Its a Even number")

else:
        print("Its a odd number")  
        
name & age

name=(input("Enter your name :- "))
age=int(input("Enter your age :-"))

if age>18:
        print("You can not marry")
    
else:
        print("Child marriage is not allowed")             
        
3) elif statement or elif ladder :- 

if condition:        
        statement

elif condition:
        Statement
elif condition:
        Statement            
else:
        statement
        
For example :-
num=int(input("Enter a number :- "))

if num>0:
    print("Positive number")
elif num<0:
    print("Negative Number") 
else:
    print("Number is zero")   
    
4)Nested if statement :
     
      if condition :
        if condition:
                statement
        else:
                statement
      
      else:
        statement                          
 
For example :-
                              

'''
a=100
b=200

if a==100:
    if b==200:
        print("The value of a is 100 and b is 200")
    else:
        print("Nested else") 

else:
      print("Main else")                         
