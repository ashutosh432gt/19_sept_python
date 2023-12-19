# What is File function in python? What is keywords to create and write file
"""
File function in python is used to perform various file handling operation.such as creating
,writing,reading etc.
"""
#To create a Blank File 
f=open("file1.txt","x")
f.close()

#To write file
f=open("file1.txt","w")
f.write("Hello\n")
f.write("My name is Ashutosh Singh\n")
f.close()
