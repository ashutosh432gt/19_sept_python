# Explain Exception handling? What is an Error in Python?
# Exception Handling in Python:

#Try Block:Contains code where an exception might occur.
  
#try:
#       # Code that might raise an exception

#Except Block:Handles the exception if it occurs.
#except ExceptionType as e:
        # Code to handle the exception

#Else Block (Optional):** Executes if no exceptions occur.
#else:
#       # Code to execute if no exception occurred


#Finally Block (Optional):Executes no matter what, for cleanup.
#   finally:
#       # Code that will be executed no matter what


#Error in Python:

#Syntax Errors:Detected by the parser, result from incorrect syntax.
#Syntax Error example
#   print("Hello, World!"

#Runtime Errors (Exceptions):Occur during program execution.
#Runtime Error (ZeroDivisionError) example
#   result = 10 / 0


#Logical Errors:Lead to unexpected results due to flawed logic.
#Logical Error example
#   num1 = 10
#   num2 = 20
#   average = num1 + num2 / 2  # Incorrect average calculation

#Exception handling helps manage runtime errors gracefully, ensuring programs can handle unexpected situations and continue execution.