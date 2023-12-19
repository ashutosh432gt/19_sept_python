# Write a Python program to append text to a file and display the text.
f=open("file1.txt", "a")
f.write("This is a new line \n")
f.close()

f = open("file1.txt", "r")
print(f.read())