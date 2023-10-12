#Write python program that swap two number with temp variable and
#without temp variable
print("Swapping Two Numbers Without using temp variable")
#storing data in a variable
a=10 
b=20
#exchanging the value stored in variable
a,b=b,a

print(a)
print(b)

print()
print("Swapping Two Numbers With using temp variable")
#declaring variable
c=5
d=9
#declaring a third varibale for interchanging the values stored in two different variables
temp=c
c=d
d=temp

print(c)
print(d)
