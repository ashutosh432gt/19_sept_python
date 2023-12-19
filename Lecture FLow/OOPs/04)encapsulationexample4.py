"""
access specifiers or visibility modes 
private variable we can't change it outside the class

private : if we can declare any variable with __
public : by default all variable or member are public
protected : if we declare any variable with _ in prefix
    
    """
class Product:
    def __init__(self):
        self.laptop = 45000
        self.__mobile = 25000
    
    def display(self):
        print("laptop",self.laptop)
        print("Mobile",self.__mobile)

    def changePrice(self,newprice):
        self.__mobile = newprice
        
obj= Product()
obj.display()

obj.laptop=65000
obj.__mobile=25000

obj.display()

obj.changePrice(65000)      
obj.display()  
   