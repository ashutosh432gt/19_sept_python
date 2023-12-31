# Write a Python program to write a list to a file.
f=open("file1.txt", "a")
list1=["I am From Bihar","I was born on 17th march 2001","My hobbies are playing Musical Instrument and Learning New Skills","I know Hindi,Kannada,Tamil,Telugu,Bengali,English and Little bit of Gujarati and malayalam"]
for i in list1:
    f.write(f"{i}\n")
f.close()

f = open("file1.txt", "r")
print(f.read())