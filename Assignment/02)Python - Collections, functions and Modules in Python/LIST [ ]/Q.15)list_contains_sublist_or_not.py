# Write a Python program to check whether a list contains a sublist

main_list = []
for i in range(1,11):
    num1=int(input("Enter a number :- "))
    main_list.append(num1)
print("Press Enter to enter numbers in sublist")
input()
print("-----Sublist-----")
sublist = []
for k in range(1,4):
    num2=int(input("Enter a number :- "))
    sublist.append(num2)

print(main_list)
print(sublist)
found = False

for i in range(len(main_list) - len(sublist) + 1):
    if main_list[i:i + len(sublist)] == sublist:
        found = True
        break

if found:
    print("The sublist is present in the main list.")
else:
    print("The sublist is not present in the main list.")
