#Write a Python program to sort three integers without using 
#conditional statements and loops.

x=int(input("Enter First Integer :- "))
y=int(input("Enter Second Integer :- "))
z=int(input("Enter Third Integer :- "))
#using min and max function and adding calculation to sort integers in ascending order
a1=min(x,y,z)
a3=max(x,y,z)
a2=(x+y+z)-a1-a3

print("Sorted integers = ",a1,a2,a3)