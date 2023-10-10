# Write a Python program that will return true if the two given integer 
# values are equal or their sum or difference is 5.

a=int(input("Enter First Integer :- "))
b=int(input("Enter Second Integer :- "))
#applying condtion if first integer is equal or thier difference is 5 there result will be true or else false
if a==b or abs(a-b)==5 or a+b==5:
    result=True
    print(result)
else:
    result=False    
    print(result)