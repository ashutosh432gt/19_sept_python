# Write a Python program to read last n lines of a file
f=open("file1.txt","r")
n=int(input("Enter the number of lines to be read: "))
lines=f.readlines()
for i in range(1,n+1):
    print(lines[-i])