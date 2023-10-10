# Write a Python program to count the occurrences of each word in a 
# given sentence

sentence=input("Enter a sentence :- ")
word=input("Enter a Word to count its occurence in a sentence :- ")
#using count method to count how many times word occuered in a sentence
count=sentence.count(word)

print("{} occurs {} times in the given sentence".format(word,count))