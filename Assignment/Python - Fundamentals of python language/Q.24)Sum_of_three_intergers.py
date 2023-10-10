# - Write a Python program to sum of three given integers. 
# However, if two values are equal sum will be zero
a=int(input("Enter First Integer :- "))
b=int(input("Enter Second Integer :- "))
c=int(input("Enter Third Integer :- "))
#applying condition if two variables is equal then sum will be zero or else three given integers will be added
if a == b or b == c or c == a:
    print("Two Integers are equal")
    sum = 0
else:
    sum= a + b + c
    
print("Sum = {} + {} + {} = ".format(a,b,c,sum))