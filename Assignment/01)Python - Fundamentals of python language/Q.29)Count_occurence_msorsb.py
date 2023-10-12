#Write a Python program to count occurrences of a substring in a string.

main=input("Enter Main String :- ")
sub=input("Enter Sub String :- ")
#using count method to count how many times substring occuered in a string
count=main.count(sub)

print("{} occurs {} times in the string".format(sub,count))