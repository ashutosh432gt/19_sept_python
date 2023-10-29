# Write a Python program to print all unique values in a dictionary. 
my_dict={
    "A" : 1,
    "B" : 1,
    "C" : 2,
    "D" : 2,
    "E" : 3,
    "F" : 4
}

print("Original Dictionary : ",my_dict)
#dictionary to set to find unique values
dict_values = set(my_dict.values())

print("Unique Values : ",dict_values)