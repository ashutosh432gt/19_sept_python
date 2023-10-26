# Write a Python program to unzip a list of tuples into individual lists

list_of_tuples = [(1, 'a', 3.0), (2, 'b', 4.0), (3, 'c', 5.0)]


first_elements = []
second_elements = []
third_elements = []


for tup in list_of_tuples:
    first_elements.append(tup[0])
    second_elements.append(tup[1])
    third_elements.append(tup[2])


print("List of first elements:", first_elements)
print("List of second elements:", second_elements)
print("List of third elements:", third_elements)
