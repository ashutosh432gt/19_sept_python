""""
inheritance : one class derived properties to another class 
              inheritance provide reusability ,using of inheritance we can reduce our code
              inheritance save time 
              
              there are mainly 5 types of inheritance 
              1)Single Level
              2)Multi Level
              3)multiple
              4)hierarchical
              5)hybrid inheritance
"""
#single level inheritance

'''class A:
    num1=10
    num2=20
    
class B(A): #inherit A to B
    def display (self):
        ans = self.num1 + self.num2
        print(ans)
      
#object creation
obj = B()
obj.display()            '''

#example 2

'''class Parent:
    def __init__(self,firstname):
        self.firstname = firstname
    def display(self):
        print(self.firstname)
class Child(Parent):
    def __init__(self,firstname):
            super().__init__(firstname) 
    
    def displayChild(self):
        print("Welcome to sub class")
        
obj = Child("Anjali")
obj.display()
obj.displayChild()     '''                 

#example 3 multilevel

class A :
    def display(self):
        print("A class")
class B(A) :
    def display(self):
        print("B Class")
class C(B) :
    def display(self):
        print("C Class")
        
obj = C()
obj.displayA()
obj.displayB()
obj.displayC()                
                 