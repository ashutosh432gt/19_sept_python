"""
function : function is a bloc of code are used  again and again

            using of function we can reduce our code
            and reuse our code
            function provide clean and clear coding
            
// types of function
1)built-in function : () --- print() , input (), len()......
2)user-defined function : function which is defined by user

// how we can define or use function or how to implement function

there are three steps to implement function

step 1: function declaration // which is use in c programming
step 2: function definition
step 3: function calling

function definition syntax :
                // bloc of code
                
function calling syntax :

funname()  
'''#example 1
def greetings(): # function define
    print("Hello and welcome to python")
    
greetings() #function calling  '''     


function categories
    there are 4 types of categories
    
    1)function without parameter and function without return type 
    
            syntax: 
                def funname():
                        statement
     example :-
                def sum():
                    num1=int(input("Enter Number 1: "))
                    num2=int(input("Enter Number 2 : "))
                    ans=num1+num2
                    
                sum()    
                        
    2)function with parameter and function without return type
            syntax:
                def funname(parameter)
                    statement
     example 1:- 
                def sum(num1,num2)
                ans=num1+num2
                print(ans)
                
                num1=int(input("Enter Number 1: "))
                num2=int(input("Enter Number 2 : "))    
                
                sum(num1,num2)        
     example 2 ;-
                def checkgreatestdigit(n):
                    large=0
                    while n>0:
                        r=n%10
                        if r > large:
                            large=r
                        n/=10
        
        
                    print("Greatest Digits = ",large)
        
                n = int(input("Enter A number :-"))
                checkgreatestdigit(n) 

                                
    3)function without parameter and function with return type
    
        syntax:
            def funname():
                return statement
        example :-
            def factorial()
            f=1
            n=int(input("Enter a number :- ))
            for i in range (1,n+1)
                f*=i
            return(f)
            
             print(f"Factorial = {factorial()})        
    4)function with parameter and function with return type
    
        syntax :
            def funname(parameter)
                return statement
        
        example :-
            def factorial(n)
            f=1
            for i in range (1,n+1)
                f*=i
            
            return(f)
            n=int(input("Enter a number :- ))
            print(f"Factorial = {factorial()})        

"""
           

 

