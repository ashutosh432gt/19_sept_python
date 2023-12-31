# Inheritance in Python:

# Inheritance allows a class (child/derived) to inherit properties and behaviors
# from another class (parent/base). It promotes code reuse.

# Example:


class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass  # Placeholder for the method

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(species="Dog")
        self.name = name
        self.breed = breed

    def make_sound(self):
        return "Woof!"

# Constructor (`__init__`) in Python:

# The `__init__` method is a special method in a class that initializes its 
# attributes when an instance is created. It is the constructor.

# Example:

class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
