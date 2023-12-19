# What is lambda function in python? What we call a function which is
# incomplete version of a function?

'''
Incomplete or Partial Function : a function which is incomplete or partially specified
version of another function is called as partial function.

for example:
'''
from functools import partial

#creating a function
def add(x,y):
    return x+y
    
#creating partial function from function created above
par_func=partial(add,3)

print(par_func(5))
'''
Lambda Function :- Function without any name is known as lambda function.
for example:
'''

x= lambda a,b : a*b
num1=int(input("Enter a Number :- "))
num2=int(input("Enter a Number :- "))

print(x(num1,num2))