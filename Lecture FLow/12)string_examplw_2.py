#example 1 email validation

'''email=input("Enter your email :- ")

if email.endswith(".com"):
    print("valid email")
else:
    print("Invalid email") ''' 
    
 #example 2 search 
 
'''search= input("Enter your string :- ")

if search.startswith("https://www.") or search.startswith("http://www."):
    print("Searching......")
else:
    if search.endswith(".com"):
        print("Searching....")
    else:
        s="https://www."+search+".com"
        print(f"{s} searching.....") '''          
        
#string indexing

'''s1="welcome"
print(s1)
print(s1[0])
print(s1[-1])
print(s1[2:4]) '''    #string slicing [note:- it ignores last character]   


#example 1

'''s1="My fav subject is python"

subject=input("Enter your subject:- ")

if subject in s1:
    print("Available")
else:
    print("Not available") '''     
    
#example 2 count length of string without using len function

'''s1="hello"
print(s1)    
count=0
for i in s1:
    count+=1
      
print("len ",count) '''    

#example 3
'''s1="hello"
s2="welcome"

#fetch starting two characters from string
print(s1[:2])
#fetch last two characters from string
print(s2[-2:])
print(s1[-2:-1])

s3=s1 + s2 [-2:]
print(s3)
#concatenation
s3= s1[:2] + "good" + s2 [-2:]
print(s3)'''

#example 4 to validate

'''name="asdas"

print(name.isalpha)

name="4456"
print(name.isalpha)

name="4455663"
print(name.isdigit)

name="45asgdah"
print(name.isdigit)
print(name.isalnum)'''

