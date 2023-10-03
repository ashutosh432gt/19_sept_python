# Write a Python program that compute the area of following
#1) Triangle (accepts base and height)
#2) Circle (accept radius)

#1)Area of Triangle

base=int(input("Enter the base of the triangle :- "))
height=int(input("Enter the height of the triangle :- "))

a=base*height
area=1/2*a

print("The area of triangle = {} * {} = {}".format(base,height,area))

#2)Area of Circle
print()
radius=float(input("Enter radius of Circle :-"))

pi=3.14159
area=pi*radius*radius

print("Area of circle = {} * {} * {} ={}".format(pi,radius,radius,area))