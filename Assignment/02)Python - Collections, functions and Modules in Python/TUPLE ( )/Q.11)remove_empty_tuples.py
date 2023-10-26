# Write a Python program to remove an empty tuple(s) from a list of tuples

l1 = [(1, 2, 3), (), (4, 5, 6), (), (7, 8, 9), ()]

empty_tuples = []
for i in l1:
    if len(i) < 1:
        empty_tuples.append(i)

for empty_tuple in empty_tuples:
    l1.remove(empty_tuple)

if not empty_tuples:
    print("No Empty Tuple Present in the list")

print(l1)
