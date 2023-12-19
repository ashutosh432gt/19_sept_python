# Write a Python function to check whether a number is in a given range

def range(numbers_range):
    start_range,end_range=numbers_range
    if r >=start_range and r<=end_range:
        print("Entered Number Is In Range")
    else:
        print("Entered Number is Not In range")
    return numbers_range

start_range=int(input("Enter the starting Number :- "))
end_range=int(input("Enter the ending Number :- "))

number_range=(start_range,end_range)

r=int(input("Enter a Number to check it's in range or not :- "))
range(number_range)
            