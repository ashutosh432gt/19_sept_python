#Write a Python program to get the Factorial number of given number

num=int(input("Enter a number :- "))
f=1 #declaring variable
#applying for loop for multiplication of number in a sequence to find factorial upto user's input given
for i in range(1,num+1):
    f*=i  #multiplying f which represents factorial with i to find factorial
    
print(f)