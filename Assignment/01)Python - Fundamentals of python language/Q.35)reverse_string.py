# Write a Python function to reverses a string if its length is a multiple of 
# 4

string=input("Enter String :- ")
if len(string)%4==0:
#applying loop to reverse the loop
    for i in string[::-1]:
        print(i,end="")
else:
    print(string)
    print("String can not be reversed because lentgh of string is not multiple by 4 ")        