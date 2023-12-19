# Write a Python program to read a random line from a file
import random
def read_random(filename):
    f= open(filename,"r")
    lines=f.readlines()
    if not lines:
        print("File is empty")
    random_line=random.choice(lines)
  
    return random_line    

name="read_random_line.txt"

random_line=read_random(name)

print(f"Random Line: {random_line}")
        