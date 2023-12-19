"""
                A
                |
                V
        ---------------
        |             |
        |             |
        V             V
        B             C
        
    """
class A:
    num1 = 10
    def displayA(self):
        print("num1 = ",self.num1)

class B(A):
    num2 = A.num1 + 100
    def displayB(self):
        print("num2 = ",self.num2)
        
class C(A):
    num3 = A.num1 + 200
    def displayC(self):
        print("num3 = ",self.num3)
        
objb = B()
objc = C()

objb.displayA()
objb.displayB()


objc.displayA()    
objc.displayC()    