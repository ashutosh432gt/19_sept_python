# Write a Python program to read a file line by line and store it into a list
f=open("file1.txt","r")

lines=f.readlines()
lines_list=[]
for i in lines:
    print(i)
    lines_list.append(i)

print(lines_list)    
