# Write a Python program to convert a list of tuples into a dictionary

list_of_tuples = [(1, 'one'), (2, 'two'), (3, 'three')]

dictionary = {}

for item in list_of_tuples:
    key, value = item
    dictionary[key] = value


print(dictionary)
