# .Write a Python program to split a list into different variables.

my_list = []

# Populate the list with user input
for i in range(1, 6):
    num = int(input("Enter a Number: "))
    my_list.append(num)

# Print the list
print("list:", my_list)

# Unpack the list into separate variables
var1, var2, var3, var4, var5 = my_list

# Print the variables
print("var1:", var1)
print("var2:", var2)
print("var3:", var3)
print("var4:", var4)
print("var5:", var5)

