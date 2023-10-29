# Write a Python function that takes a list and returns a new list with
# unique elements of the first list
list1=[] #creating a blank list

for i in range(1,6):
    number=int(input("Enter a Number :- "))
    list1.append(number)
    
print("Original List :- ",list1)    

#changing list into set
set= set(list1)

#set to list
unique_list=list(set)

print("Unique List :- ",unique_list)