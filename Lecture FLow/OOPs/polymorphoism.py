"""
Polymorphism : poly means many and morphism means forms

    polymorphism which is derived from the geek word
    
    polymorphism means one method has different different forms
    
    using of polymorphism we can use one named method in different different ways
    
    
    there are 2 types of polymorphism :
    
    1)method overloading
        method overloading : 
                one class contain more than one name methods
                
                note :method overloading is not supported in Python
                
   2)method overriding :
            when parent and child both have same name method
            
            note : method overriding only support in inheritance concept             
"""
#example 1 method overloading

'''class student:
    def display(self):
        print("this is display method")
    def display(self):
        print("this is display method")
        
obj=student()
obj.display()
obj.display(10) '''

#note :- it will throw error because method overloading is not supported in python.           

#example 2 method overriding
#method overriding : when a parent and a child have same name method is called method overriding.

class parent:
    def display(self):
        print("Parent class display method")

class child(parent):
    def display (self):
        parent.display(self)
        print("Child class display method")
        
obj = child()
obj.display()                
