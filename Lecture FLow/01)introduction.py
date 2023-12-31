# print("Welcome to the new world of python programming")
# print("\thello \bstudents")

l1=[1,2,3,4,5,5,6,6,7,7]
l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)
        
print(l2)        