# How to Define a Class in Python? What Is Self? Give An Example Of A
# Python Class

'''To define a class in Python:


class MyClass:
    # Class attributes and methods go here
    pass


self is a convention in Python that represents the instance of the class. 
It is the first parameter in class methods.

Example:

class Dog:
    species = "Pitbull"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

dog1 = Dog(name="Buddy", age=3)
dog2 = Dog(name="Max", age=2)

print(f"{dog1.name} is {dog1.age} years old. Species: {dog1.species}")
print(f"{dog2.name} says: {dog2.bark()}")
'''

