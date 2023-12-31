# Write a Python program to copy the contents of a file to another file.
f = open("file1.txt", "r")
content = f.readlines()
f.close()

a = open("file2.txt", "w")

for i in content:
    a.write(f"{i}\n")

a.close()

print("File copied successfully")
print("::::::::::::::::::::::::::::::::::::::::::::")

a = open("file2.txt", "r")
print(a.read())
a.close()


   