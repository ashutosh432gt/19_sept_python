# Write a Python function to calculate the factorial of a number (a non-negative integer) 

def factorial(num):
    f = 1
    for i in range(1,num+1):
        f=f*i
    print("Factorial = ",f)
    return(f)   
        
num=int(input("Enter a number to find its factorial :- "))
factorial(num)