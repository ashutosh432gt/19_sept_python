"""
List operators :- 

add operation methods :- 

1)append() : using of append we can store data in existing list at the end of the list.

                syntax: list.append(value)

2)extend() : if we want to store more than 1 element in list
             (we can store multiple element in list format)
             
             syntax: list.extend([value])

3)insert() : if we want to store specific element at specific index position 
    
            syntax: list.insert(index,newvalue)
            
remove operation - methods

1) remove() : to remove specific element from the existing list
                
             syntax : list.remove(remove_value)
             
2) pop() :it will remove by default last index position
         
         syntax: list.pop()
         
    =====>pop(index) : it will remove specific element index wise

                        syntax : list.pop(index)
                        
3)clear() : to remove all elements from the list
            
            syntax: list.clear()
            
   =>>>>>completly delete list from the memory
   
        using of del keyword
   
        syntax: del<listname>  
        
==> fetch specific data from list or access specific element from the list

    index() : fetch specific data or element from the list using index
    
            syntax : list.index(index_position) 
            e.g  list.index(1)
            
    list indexing : 
                
                syntax : list[startingposition : endingposition]
                e.g list [2:4]  
                                                             
#example 1 shopping list using append() method

shopping_list=[]

status = True

while status:
    product_name=input("Enter product name :- ")
    shopping_list.append(product_name)
    
    choice=input("Do you want to add more products : Enter Y for yes and N for no :- ").lower()
    
    if choice=="n" or choice=="no":
        status=False
        
        
for items in shopping_list:
    print(items)        

#example 2 using extend

l1=[1,2,3,4,5,6,7]

l1.insert(2,10001)

print(l1)

#searching list

l1=["apple","mango","banana"]

for i in l1:
    print(i)
    
fruit_name=input("Enter fruit")

if fruit_name in l1:
    print("yes,it is available")
else:
    print("no,its not available")  
    
    
#to fetch unique values in list

l1=[23,45,67,2,8,23,2]

l2=[]

for in in l1:
    if i not in l2:
        l2.append(i)
        
print(l2)   

#two list comparision

l1=["tv","mobile","fridge"]
l2=["25000","15000","45000"]

name= input("Enter product name :- ")
index_number=l1.index(name)
print(index_number)
price_value=l2[index_number]
print(f"{name} = Rs.{price_value}")     


##project          
"""



























