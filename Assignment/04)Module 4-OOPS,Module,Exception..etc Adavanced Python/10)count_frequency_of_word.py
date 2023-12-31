# Write a Python program to count the frequency of words in a file.
f=open("file1.txt","r")
words=f.read()
count=0;
for i in words:
    count+=1

print("Number of Words in File = ",count)    