a=int(input("Enter Side 1 of the triangle :- "))
b=int(input("Enter Side 2 of the triangle :- "))
c=int(input("Enter Side 3 of the triangle :- "))

if a==b and a==c and b==c:
    print("Its an Equilateral Triangle")
elif b==a or b==c or a==c:
    print("Its an Isosceles triangle") 
else:
    print("Its an scalane traingle")
      