# Write a Python program to find the highest 3 values in a dictionary

my_dict = {
    'a': 10,
    'b': 25,
    'c': 15,
    'd': 30,
    'e': 5
}


values = list(my_dict.values())

#sort the values in descending order
values.sort(reverse=True)

#print the first three values from dictionary
highest_3_values = values[:3]

print("The highest 3 values in the dictionary are:")
for value in highest_3_values:
    print(value)
