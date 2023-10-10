#Write a Python program to check if a number is positive, negative or zero.

num=int(input("Enter a number :- "))
#applying condition if num is greater than zero 
if num>0:
    print("Positive number")
#applying condition if num is lesser than zero    
elif num<0:
    print("Negative Number") 
#applying condition if num is neither greater nor lesser than zero    
else:
    print("Number is zero")   