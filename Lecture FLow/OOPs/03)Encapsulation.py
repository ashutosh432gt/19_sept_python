"""
encapsulation :- one class can contain data members and member functions in single entity encapsulation 
which is similar like capsule  
    """
# class student:
#     def input(self,name,subject,marks):
#         self.name = name
#         self.subject = subject
#         self.marks = marks
        
#     def display(self):
#         print(self.name)
#         print(self.subject)
#         print(self.marks)
        
# student=student()
# student.input("AAA","Python","78")
# student.display()

# student.input("AAA","java",95)
# student.display

#example 2 getter and setter

class student:
    def setName(self,name):
        self.name = name
    
    def getName(self):
        return self.name    

    def setSubject(self,subject):
        self.subject = subject
    
    def getSubject(self):
        return self.subject

    
    # def display(self):
    #     print(self.name)
    #     print(self.subject)
        

student = student()
name= input("Enter Your Name :- ")
student.setName(name)
subject=input("Enter Your Subject :- ")
student.setSubject(subject)

print(student.getName())
print(student.getSubject())