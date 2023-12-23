# Write a python program to find the longest words.
f=open("file1.txt","r")
line=f.read()
words=line.split()
longest_word=""


for word in words:
    word_length = len(word)
    length = len(longest_word)
    if word_length > length:
        longest_word = word
       
    elif word_length == length:
        longest_word = longest_word + " " + word
       

print("Longest word:", longest_word)
   