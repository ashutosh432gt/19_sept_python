import pymysql
mydb= pymysql.connect(host="localhost",user="root",passwd="",database="pythondb")
mydbcursor=mydb.cursor()

menu="""
                MENU
            press 1 for add
            press 2 for remove    
            press 3 for update
"""
print(menu)
choice=input("Enter your choice : ")
if choice =="1":
    name=input("Enter the name : ")
    subject = input("Enter the subject : ")
    city = input("Enter the city : ")
    
    query="insert into student (name,subject,city) values('%s','%s','%s')"
    args=(name,subject,city)
    
    mydbcursor.execute(query%args)  
    
    print("Successfully data added")
    
elif choice == "2":
    name=input("Enter Your Name :- ") 
    query="delete From student where name = '%s'"
    
    args = (name)
    mydbcursor.execute(query%args)
    
    mydb.commit()
    print("Successfully deleted")   
elif choice == "3":
    print("Update Record")
    name=input("Enter Your Name :- ")
    newname=input("Enter Updated Name :- ")
    subject=input("Enter Subject :- ")
    city=input("Enter City :- ")
    
    query="update student set name='%s',subject='%s',city='%s' where name='%s' "
    args=(newname,subject,city,name)
    
    mydbcursor.execute(query%args)
    mydb.commit()
    
    print("Successfully Updated")