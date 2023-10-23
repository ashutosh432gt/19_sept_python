# Write a Python program to generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30

list= [] #creating a blank list

for i in range(1,31) : #sequenced loop for finding square of number upto 30
    list.append(i**2) #calculating square of each number
    
print(list[:5])
print(list[-5:])    
