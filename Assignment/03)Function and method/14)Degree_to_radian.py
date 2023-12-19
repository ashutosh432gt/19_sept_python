# Write a Python program to convert degree to radian
import math

def convert(degree):
    radian=degree*(math.pi/180)
    return radian

degree=int(input("Enter Degree value to convert it to radian :- "))
con=convert(degree)
print(f"{degree} degree = {con} radian")

