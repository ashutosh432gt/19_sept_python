#Write a Python program to test whether a passed letter is a vowel or not
user=input("Enter any alphabet to check its vowel or not :- ")
#creating a list which includes vowel
vowel=["a","e","i","o","u"]
#applying condtion if to check wheather the users entered alphabet is vowel or not
#if users entered alphabet is in vowel list then its vowel or else it is not a vowel
if user in vowel:
    print("{} is a vowel".format(user))
else:
    print("{} is not a vowel".format(user))    