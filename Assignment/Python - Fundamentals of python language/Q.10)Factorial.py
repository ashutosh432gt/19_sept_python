#Write a Python program to get the Factorial number of given number

num=int(input("Enter a number :- "))
f=1
for i in range(1,num+1):
    f*=i
    
print(f)