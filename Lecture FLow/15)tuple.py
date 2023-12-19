"""
tuple :- tuple is a collection data type
         tuple which is represent by () braces
         tuple which is immutable(we can't change its value)
         tuple is orderable, indexable
         e.g
         t=()
    """
#example 1 length and count
'''t=()     
print(t)

t=(1,2,3,4,6)
print(t)

print(len(t))

# for i in t:
#     print(i)
count=0
for i in t:
    count+=1
    
print(count)   ''' 

#example 2 fetch tuple
'''t=(1,2,3,4,6)

print(t[0])'''

#tuple modification
#tuple cannot be changed it's immutable
t=(10,20,30,40)

#converting tuple to list

l1=list(t)

l1[1]=200

#re-convert into tuple

t=tuple(l1)
print(t)