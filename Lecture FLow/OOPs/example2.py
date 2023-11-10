"""
self : self is a similar like this keyword
        self is a representation of current class properties
        
Function vs Methods

functions : which is are declare outside the class
            which is independent

method : which is declare inside the class 
        which is dependent on  object
                            
    """
class Student :
    #creating method
    def info(self):
        print("WELCOME TO THE STUDENT INFO")
       
#Object creation
student= Student()   
student.info()     
        