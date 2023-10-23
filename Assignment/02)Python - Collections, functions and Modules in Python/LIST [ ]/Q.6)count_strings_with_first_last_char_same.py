# Write a Python program to count the number of strings where the
# string length is 2 or more and the first and last character are same from a given list of strings.

string_list = ["ayesha", "naman", "yuktha", "anna", "ashutosh"] #creating a list
count = 0 #declaring variable

for string in string_list: #sequenced loop for counting string lentgh
    if len(string) >= 2 and string[0] == string[-1]: #condition if string length is greater than 2 and first and last chracter is same
        count += 1

print("Number of strings with the same first and last character :", count)
