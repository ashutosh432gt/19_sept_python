# Write a Python program to add 'ing' at the end of a given string (length 
# should be at least 3). If the given string already ends with 'ing' then add 
# 'ly' instead if the string length of the given string is less than 3, leave it 
# unchanged

string=input("Enter String :- ")

#applying condition to check if the length of the string is greater than 3 or not
if len(string) > 3:
    #applyinf condition if a word already ends with ing then will add ly at end
    if string.endswith("ing"):
        new_string = string + "ly"
        print("After adding ly = ",new_string)
    #applying condition if the string doesn't ends with ing    
    else:
        new_string= string + "ing"
        print("After adding ing = ",new_string)
else:
    print("String remains unchanged")


