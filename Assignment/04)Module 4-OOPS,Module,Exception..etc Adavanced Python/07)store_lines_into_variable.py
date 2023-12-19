# Write a Python program to read a file line by line store it into a variable.
f=open("file1.txt","r")
lines=f.readlines()
value=""
for line in lines:
    # print(line)
    value+=line

print(value)    