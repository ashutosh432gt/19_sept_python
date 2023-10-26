#Write a Python program to replace last value of tuples in a list

tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

new_value = int(input("Enter value to replace with last value :- "))


# Using pop () method to replace last value 
for i in range(len(tuple_list)):
    tuple_list[i] = tuple_list[i][:2] + (new_value,)


print(tuple_list)
