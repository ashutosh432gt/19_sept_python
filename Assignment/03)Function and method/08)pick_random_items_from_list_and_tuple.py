# How can you pick a random item from a list or tuple?
'''
To pick random item from a list or tuple we need to use random module 
for example :
'''
import random

l1=["Ashutosh","Bhavin","Karan","Jaydip","Paras"]
t1=(1,2,3,4,5)

random_list=random.choice(l1)
random_tuple=random.choice(t1)
print("Randomly Picked Item from the List is :- ",random_list)
print("Randomly Picked Item from the Tuple is :- ",random_tuple)


