#  Write a Python class named Circle constructed by a radius and two
# methods which will compute the area and the perimeter of a circle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return 3.14 * self.radius * self.radius

    def circle_perimeter(self):
        return 2 * 3.14 * self.radius
    
r=int(input("Enter the radius of the circle: "))

circle1=Circle(radius=r)

area=circle1.circle_area()
print(f"The area of Circle is : {area}")
perimeter=circle1.circle_perimeter()    
print(f"The perimeter of Circle is : {perimeter}")