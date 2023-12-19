import pymysql
my_db= pymysql.connect(host="localhost",user="root",password="")

mydbcursor=my_db.cursor()

mydbcursor.execute("create  database if not exists  pythondb")
my_db.commit()

my_db=pymysql.connect(host="localhost",user="root",password="",database="pythondb")
mydbcursor=my_db.cursor()

mydbcursor.execute("Create table if not exists  student(id int primary key auto_increment,name varchar(20),subject varchar (20),city varchar(20))")
my_db.commit()