# Write a Python program to find the second smallest number in a list

list1 = [] #creating a blank list
#accepting input/numbers from users
for i in range(1, 6):
    number = int(input("Enter a number: "))
    list1.append(number)

print(list1)
#condition for checking if the list length is more than 2 or not
if len(list1) < 2:
    print("The list has fewer than two elements.")
else:
    smallest = min(list1) #finding minimum number in list using min method
    list1.remove(smallest) #removing minimum number from the list
    second_smallest = min(list1) 

    print("The second smallest number in the list is:", second_smallest)
