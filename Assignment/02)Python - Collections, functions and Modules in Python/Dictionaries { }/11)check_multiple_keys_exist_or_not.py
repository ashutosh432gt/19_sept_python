# Write a Python program to check multiple keys exists in a dictionary 
my_dict={
    1:'a',
    2:'b',
    3:'c',
    4:'d',
    5:'e'
}
count=0
for k in my_dict:
    count+=1

if count>1:    
    print(f"There are {count} keys present in the dictionary : (Multiple Keys are present)")    
else:
    print(f"There are {count} keys present in the dictionary : (Multiple Keys are not present)")    
        