menu = """
     MENU
  Press 1 for Counsellor
  Press 2 for Faculty
  Press 3 for student
"""

students = {}  # Creating a blank dictionary
status = True

while status:
    print("::::::::::::Student Management System::::::::::::")
    print(menu)
    choice=int(input("Enter Your choice :- "))
    if choice==1:
        role1="""
                1.Add Student
                2.Remove Student
                3.View all student
                4.View Specific Student
        
        """
        print(role1)
        choice=int(input("Enter your choice :- "))
        if choice==1:
            serial_number=int(input("Enter Serial Number :- "))
            fname=input("Enter Your First Name :- ")
            lname=input("Enter Last Name :- ")
            subject=input("Enter Subject :- ")
            marks=int(input("Enter Marks :- "))
            fees=int(input("Enter Fees :- "))
            phone=int(input("Enter Student Contact Number : -"))
            students[serial_number] = {
                'First Name': fname,
                'Last Name': lname,
                'Subject': subject,
                'Marks': marks,
                'phone' : phone,
                'Fees': fees
            }
            
            option=input("Do you want to add more students :Enter yes to add or else enter No :- ").lower()
            if option=="yes" or option=="y":
                status=True
                
                continue
            else:
                continue
        elif choice==2:
            print(students)
            num=int(input("Enter Serial Number of student to remove :- "))
            if num in students.keys():
                students.pop(num)
                print(students)
        elif choice==3:
            print(students)   
        elif choice==4:
            num=int(input("Enter Serial Number of student to view student details :- "))
            if num in students.keys():
                print(f"{students[serial_number]}")
        else:
            print("Invalid Input")        
    elif choice==2:
        faculty="""
                1.Add marks to student
                2.view all students
        """
        print(faculty)            
        choice=int(input("Enter Your choice :- "))        
        if choice==1:
            num=int(input("Enter Students Serial Number :- "))
            if num in students.keys():
                mark = int(input("Enter Marks :- "))
                students[num]['Marks'] = mark
                print("Marks updated successfully.")
                print("Updated Student Database:")
                for serial_number, student_info in students.items():
                    print(f"Serial Number: {serial_number}, Student Info: {student_info}")
        elif choice==2:
            print(students)    
        else:
            print("Invalid serial number")  
              
    elif choice==3:        
        stu="""
            Press 1 View Student details
            Press 2 Raise a Query
        """
        print(stu)
        choice=int(input("Enter your choice :- "))
        if choice==1:
            num1=int(input("Enter Your Serial Number ;- "))
            if num1 in students:
                print(f"{students[serial_number]}")
            else:
                print("Invalid serial Number")    
        elif choice==2:
            query=input("Enter Your Query :- ")
            print("Your Query submitted successfully")
        else:
            print("Invalid choice")
            
    else:
        print("Invalid Input")   
    
    user=input("Do you want to perform more operation : ").lower()
    if user=="y" or user=="yes":
        status=True
    else:
        status=False
             
             