# Write a Python class named Rectangle constructed by a length and width
# and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        return self.length * self.width

l=int(input("Enter length of rectangle: "))
w=int(input("Enter width of rectangle: "))
rectangle1 = Rectangle(length=l, width=w)


area = rectangle1.rectangle_area()
print(f"The area of the rectangle is: {area}")
