# Write a Python function that takes a list of words and returns the length 
# of the longest one

# Creating a list of words
word_list = ["Bhavin", "Karan", "Himanshu", "Dilip", "Shivarsh"]

# declaring vairbles to store longest length and word 
longest_length = 0
longest_word = ""
#for loop to count the word and its length
for word in word_list:
    length = 0

    # running loop to count the number of alphabets in words
    for alpha in word:
        length += 1

    # Applying condition to Check if the current word is longer than the previous longest word
    if length > longest_length:
        longest_length = length
        longest_word = word

#Applying condition to find longest word and length 
if longest_length > 0:
    print("Longest Length = ",longest_length)
    print("longest word = ",longest_word)

