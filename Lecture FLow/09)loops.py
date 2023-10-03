#loops => to excute a statement repeatedly
#types of loops
#1)for loop -Sequence controlled loop
#range()- to find the range between the numbers. range(starting range,ending range,jump)
#example 1

'''for i in "Python":
    print(i)'''
    
#example 2
    
'''for i in range(1,11):
    print(i)   ''' 
    
#example 3 (even number using jump)

'''for i in range (2,21,2):
    print(i)    '''
    
#example 4 (odd number using jump)

'''for i in range (1,21,2):
    print(i)        '''
 
#example 5 reverse counting 
    
'''for i in range(11,0,-1):
    print(i)  '''  
    
#example 6 user input counting    
    
'''a=int(input("Enter number upto which you want counting :- "))

for i in range(1,a+1):
    print(i)'''
    
#example 7 sum of all numbers

'''a=int(input("Enter a number :- "))
sum=0
for i in range (1,a+1):
    
    sum+=i    
    
print(sum) '''   

#example 8 sum of even and odd numbers seperatly

'''a=int(input("Enter a number :-"))
e_sum=0
o_sum=0

for i in range (1,a+1):
    if i%2==0:
        e_sum+=i
    else:
        o_sum+=i

print("Even sum : ",e_sum)
print("Odd sum : ",o_sum)    '''    

#end parameter
#example 9 of end=" " 

'''for i in range(1,6):
    print(i,end=" ")   #end=" "---->prints output horizontally'''
    
    
#example 10 take 5 name from users

'''for i in range(1,6):
    name=input("Enter your name :- ")'''
 
#nested for loop examples    
#example 11 pattern

'''for row in range (1,6):
    for col in range (1,6):
        print(" * ",end=" ")
    print()  '''    
    
#example 12 pattern 2

'''for row in range (1,6):
    for col in range (1,row+1):
        print(" * ",end=" ")
    print()  ''' 
    
#example 13 number pattern

'''for row in range (1,6):
    for col in range (1,row+1):
        print(row,end=" ")
    print()      
    '''
#example 13 part b 

'''for row in range (1,6):
    for col in range (1,row+1):
        print(col,end=" ")
    print()      '''
    

#example 14 pattern

for row in range(1,6):
    for col in range (1,row+1):
        if row%2==0:
            print(" 0 ",end=" ")
        else:
            print(" 1 ",end=" ")
    print()    
    
#example 15

for row in range (1,6):
    for col in range(1,row+1):
        if col%2==0:
            print(" 0 ",end=" ")
        else:
            print(" 1 ",end=" ")
    print()              
                    
    