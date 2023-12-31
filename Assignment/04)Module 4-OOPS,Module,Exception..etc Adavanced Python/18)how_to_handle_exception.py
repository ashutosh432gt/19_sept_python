# How Do You Handle Exceptions With Try/Except/Finally In Python?
# Explain with coding snippets.

"""In Python, the `try`, `except`, and `finally` blocks are used for exception handling. 
   The basic structure is as follows:

try:
    # Code that may raise an exception
    # ...
except SomeException as e:
    # Code to handle the exception
    # ...
finally:
    # Code that will be executed no matter what, whether an exception occurs or not
    # ...
"""

#for example


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        result = None
    finally:
        print("This will always be executed, regardless of whether an exception occurred or not.")
    
    return result

