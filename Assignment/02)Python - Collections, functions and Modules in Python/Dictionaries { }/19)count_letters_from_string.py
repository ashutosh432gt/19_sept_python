# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
sample_string = 'w3resource'
letter_count = {}

for char in sample_string:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1

print(letter_count)
