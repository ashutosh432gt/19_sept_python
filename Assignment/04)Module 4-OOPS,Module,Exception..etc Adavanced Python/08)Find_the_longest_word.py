# Write a python program to find the longest words.
f=open("file1.txt","r")
line=f.read()
words=line.split()
longest_word=""
max_length=0

for word in words:
    word_length = len(word)
    length = len(longest_word)
    if word_length > length:
        longest_word = word
        max_length = word_length
    elif word_length == length:
        longest_word = longest_word + " " + word
        max_length = word_length

print("Longest word:", longest_word)
   