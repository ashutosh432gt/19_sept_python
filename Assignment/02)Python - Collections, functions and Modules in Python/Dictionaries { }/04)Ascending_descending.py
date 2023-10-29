# Write a Python script to sort (ascending and descending) a dictionary by value
my_dict={"A" : 1, "B" : 2,"D" : 4, "C" : 3,"F" : 6, "E" : 5}

print("Original Dictionary ",my_dict )
#using sorted () function to print dictionary in sequence or ascending order
ascending= sorted(my_dict.items())
print("Ascending Order : ",ascending)
#reversing the sequence sorted dictionary to print in descending order
descending= sorted(my_dict.items(), reverse=True)
print("Descending Order : ",descending)