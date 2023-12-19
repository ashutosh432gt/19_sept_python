# Write a Python program to calculate the area of a trapezoid
def trapezoid(base1,base2,height):
     area = 0.5 * (base1 + base2) * height
     return area
 
a=int(input("Enter Length of First Base :- "))
b=int(input("Enter Length of First Base :- ")) 
c=int(input("Enter Height :- ")) 

area_of_trapezoid=trapezoid(a,b,c)

print("Area Of Trapezoid = ",area_of_trapezoid)
 
    