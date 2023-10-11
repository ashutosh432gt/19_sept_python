#Write a Python program to get the Fibonacci series of given range 

num=int(input("Enter a number to find Fibonacci series :- "))
a=0
b=1
print(a)
print(b) 
#applying for loop to perform calculation in a sequence 
for i in range (2,num):
    #logic for calculating fibanocci series
    num=a+b
    print(num)
    a,b=b,num