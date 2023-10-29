# Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={} #creating a blank dictionary

#copying d1 keys and values in d3 
d3=d1.copy()
#combining both dictionary  using update method
d3.update(d2)
#adding two dictionary values of common keys
for key in d2:
    if key in d1:
        d3[key]= d2[key] + d1[key]
        
print(d3)        
