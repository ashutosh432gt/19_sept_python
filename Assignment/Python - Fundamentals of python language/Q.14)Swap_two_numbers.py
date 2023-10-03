#Write python program that swap two number with temp variable and
#without temp variable
print("Without using temp variable")
a=10
b=20

a,b=b,a

print(a)
print(b)

print()
print("With using temp variable")
c=5
d=9

temp=c
c=d
d=temp

print(c)
print(d)
