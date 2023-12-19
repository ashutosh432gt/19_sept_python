"""
Multiple inheritance :- when one child class derived from more than 2 parent classes its called multiple inheritance.
multiple inheritance is only supported in python
**multiple inheritance not supported in java 
because in real world one child can have one parent only


                A           B
                |           |
                -------------
                      |
                      |
                      V
                      C
                      
    """
class A:
    num1=10
    
    def displayA(self):
        print("num = ",self.num1)
        
class B:
    num2=20
    def displayB(self):
        print("num = ",self.num2)

class C(A,B): #inherit A and B in class C
    def displayC(self):
        ans=self.num1+self.num2
        print("ans = ",ans)

c=C()
c.displayC()
c.displayA()
c.displayB()
            
        
            