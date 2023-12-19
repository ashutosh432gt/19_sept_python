"""
Abstraction : Abstraction which is represent only few information
                not allocated background information.

using of abstraction we can provide security between parent and child

in python using of ABC (Abstract Base Class ) we can implement abstraction concept                
"""
from abc import ABC,abstractmethod
class RBI(ABC):
    @abstractmethod
    def roi(self): #abstract method : method without body is called abstract method
        pass
    
class SBI(RBI):
    def roi(self):
        print("7.5")
      
class HDFC(RBI):
    def roi(self):
        print("6.8")
        
class BOI(RBI):
    def roi(self):
        print("5.5")
        
        
obj = SBI()
obj.roi()

obj2 = HDFC()
obj2.roi()

obj3=BOI()
obj3.roi()        
        
        