# What relationship is appropriate for Student and Person?
'''
Inheritance (Subclassing): In many cases, a student is a specialized type of person.
Inheritance can be used to model this "is-a" relationship. The Student class 
can inherit from the Person class, inheriting common attributes and behaviors.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

