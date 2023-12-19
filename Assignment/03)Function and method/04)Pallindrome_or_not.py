# Write a Python function that checks whether a passed string is palindrome
# or not

def palindrome(word):
    if word==word[::-1]:
        print(f"The Given word {word} Is Palindrome")
    else:
        print(f"The Given word {word} Is Not Palindrome")
    return word

word=input("Enter a Word :- ")
palindrome(word)     
