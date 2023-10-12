# Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.

a=input("Enter First String :- ")
b=input("Enter Second String :- ")

#applying condition to check the length of the string is greater than two or not

if len(a) >= 2 and len(b) >= 2:
    #swaping first two chracters of First string and Second String
    #creating new string to display and swap both string
    c=b[:2] + a[:2] + '  ' + a[:2] + b[:2]
    print("After Swap = ",c)
else:
    print("Both String length should be greater than 2")    
    