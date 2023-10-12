#Write a Python program that accepts an integer (n) and computes the value of
#n+nn+nnn.

n=int(input("Enter any Integer :- "))
#convertng integer into string
a=str(n)
b=a+a   
c=a+a+a
#converting string into integer     
x=int(a)
y=int(b)
z=int(c)
total=x+y+z

print("{} + {} + {} = {}".format(x,y,z,total))