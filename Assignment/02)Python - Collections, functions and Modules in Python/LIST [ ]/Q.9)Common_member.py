# Write a Python function that takes two lists and returns True if the
# y have at least one common member

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

#declaring variable 
common_member = False
#sequenced loop for checking if both list have same numbers or not
for item in list1:
    if item in list2:
        common_member = True

if common_member:
    print("List 1 and List 2 have common members")
else:
    print("List 1 and List 2 don't have any common members")
