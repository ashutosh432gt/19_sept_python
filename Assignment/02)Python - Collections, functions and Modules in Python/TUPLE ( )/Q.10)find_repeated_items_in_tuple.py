# Write a Python program to find the repeated items of a tuple

my_tuple = (1, 2, 2, 3, 4, 4, 5, 6, 6, 7)


unique_items = set()


repeated_items = []


for item in my_tuple:
    if item in unique_items:
        if item not in repeated_items:
            repeated_items.append(item)
    else:
        unique_items.add(item)


print("Repeated items in the tuple:", repeated_items)
