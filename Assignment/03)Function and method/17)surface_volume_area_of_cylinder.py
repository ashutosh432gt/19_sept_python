# Write a Python program to calculate surface volume and area of a cylinder
import math
def surface_area(radius,height):
    area=2*math.pi*radius**2 + 2*math.pi*radius*height
    volume=math.pi*radius**2*height
   
    
    return area,volume

r=int(input("Enter Radius of the Cylinder :- "))
h=int(input("Enter height of the Cylinder :- "))


area,volume=surface_area(r,h)

print("Area of Cylinder :- ",area)
print("Area of Cylinder :- ",volume)
    





    
    
    
    

    
    
        