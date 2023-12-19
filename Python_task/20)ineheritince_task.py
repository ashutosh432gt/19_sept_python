class A:
    def displayA(self):
        self.a=int(input("Enter the number:"))
        
class B(A):
    def displayB(self):
            s=self.a*self.a
            print("Square",s)
            self.s=s       
    def display(self):
        print(self.s) 
class C(B):
    def displayC(self):
        if self.s%2==0:
            print("Even Number")
        else:
            print("Odd Number")    
                
obj = C()
obj.displayA()
obj.displayB()
obj.displayC()                
                            
        
        