# Write a Python function to check whether a number is perfect or not.

def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    
    if sum==num:
        print(f"{num} is a Perfect Number")
    else:
        print(f"{num} is not a Perfect Number")         
    
    return sum == num

num=int(input("Enter a Number to Find it's Perfect Number or Not :- "))  
perfect(num)         