"""
Exception : which is disturb normal flow of the program

Exception handling : to handle such kind of exception is called exception handling    

syntax : 
try:
    statement
except:
    statement
"""
#exception example 1
    # print(a)
    #it will throw exception  
    
#example 2 handling
    # try:
    #     print(a)
    # except:
    #     print("Something Went Wrong")  
    
#example 3 
# try:
#     num=int(input("Enter a number : ")) 
#     print(num)
# except:
#     print("Invalid input")        

#example 4
# try:
#     num=int(input("Enter a number : ")) 
#     print(num)
# except Exception as e:
#     print("Exception",e)  
    
# #example 5
# import sys
# try:
#     num=int(input("Enter a number : ")) 
#     print(num)
# except:
#     print("Invalid Input")  
#     print(sys.exc_info()[0])
#     print(sys.exc_info()[1])       
      
#program 1
# try:
#     num1=int(input("Enter a Number :- "))
#     num2=int(input("Enter a number :- "))
    
#     ans=num1/num2
    
#     print(ans) 
# except ValueError:
#     print("Invalid Input - int number must required")
# except ZeroDivisionError:
#     print("Cannot be divided by zero")

#program 2 userdefined exception

"""
userdefined exception : An exception which is created by user
which is customize by user - we can use it on specific situation or condition
#     """
# class AgeException(Exception):
#     pass

# try:
#     num=int(input("Enter a number : "))
#     if num>=18:
#         print("You are eligible to vote")
#     else:    
#         raise AgeException
    
# except AgeException:
#     print("You are not eligible to vote")    

#example 1
"""
exception handling contain try,except,finally and else block
    """
try:
    num1=int(input("Enter a Number :- "))
    num2=int(input("Enter a number :- "))   
    ans=num1/num2
except:
    print("Invalid Input")
else:
    print("ans = ",ans)
finally:
    print("Thank you for using this application")            