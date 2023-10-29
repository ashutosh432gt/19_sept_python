# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
my_dict = {
    1: ['a', 'b'],
    2: ['c', 'd']
}

# values from dictionary
values = list(my_dict.values())

# creating a list to store combined values
combinations = []


for letter1 in values[0]:
    
    for letter2 in values[1]:
        combinations.append(letter1 + letter2)


for combination in combinations:
    print(combination)
