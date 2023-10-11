#- Write a Python program to find whether a given number is even or odd,
#print out an appropriate message to the user.

num=int(input("Enter a number :- "))
#applying condition if the the reminder of a number after divided by 2 is zero
if num%2==0:
    print("It's a Even Number")
#applying the condtion if the reminder is not zero    
else:
    print("It's a Odd Number")    