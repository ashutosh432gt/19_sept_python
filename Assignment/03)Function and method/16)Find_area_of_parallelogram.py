# Write a Python program to calculate the area of a parallelogram

def parallelogram(base,height):
    area=base*height
    
    return area

base=int(input("Enter Base Of the parallelogram :- "))
height=int(input("Enter Height Of the Parallelogram :- "))

a=parallelogram(base,height)

print("The area of Parallelogram :- ",a)
