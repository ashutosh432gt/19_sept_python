# Write a Python program to remove duplicates from a list

original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6] #creating a list

#changing list to set
unique_list = set(original_list)
#set to list
removed_duplicates=list(unique_list)

print("List before Duplicates Removed",original_list)
print("List after Duplicates Removed: ",removed_duplicates)
