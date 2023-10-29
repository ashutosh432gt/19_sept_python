# Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},
# {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

list1 = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

my_dict = {}

for entry in list1:
    item = entry['item']
    amount = entry['amount']

    if item in my_dict:
        my_dict[item] += amount
    else:
        my_dict[item] = amount

print(my_dict)
