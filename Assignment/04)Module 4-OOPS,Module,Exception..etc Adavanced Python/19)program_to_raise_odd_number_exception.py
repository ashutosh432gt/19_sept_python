# Write python program that user to enter only odd numbers, else will raise
# an exception.

def odd_even(a):
    if a % 2 != 0:
        raise ValueError("Odd Number")
    else:
        return True

try:
    user_input = int(input("Enter a number: "))
    if odd_even(user_input):
        print("You entered an Even number.")
except ValueError as e:
    print(e)
finally:
    print("Thank you for using this program.")
    
    