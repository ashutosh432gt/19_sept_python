# Write a Python script to merge two Python dictionaries
dict1 = {'a': 100, 'b': 200}
dict2 = {'x': 300, 'y': 200}

#using copy and update method to merge two dictionary
d = dict1.copy()
d.update(dict2)
print(d)

