"""
Dictionary :- it is a collection datatype
              which contain key and values in pair
              dictionary which is represented by {} braces
              
    Syntax:
            dictionary_name={
                "Key" : Value,
                "Key" : Value,
                "Key" : Value
            }    
                  
    """
#example 1

'''student = {
    "Name" : "Ashutosh",
    "Subject" : "Python",
    "Score" : 75
}

print(student)'''

#Example 2 quiz

quiz = {
    1 : {
        "que" : "Who is prime minister of india ?",
        "ans" : "Narendra Modi",
    },
    2 : {
        "que" : "Who is most popular cricketer ?",
        "ans" : "MS Dhoni",
    }
}

# print(quiz[1]["que"])
# print(quiz[1]["ans"])
# print(quiz[2]["que"])
# print(quiz[2]["ans"])

score = 0

for i in range(1,len(quiz)+1):
    print(f"Que. : {quiz[i]['que']}")
    ans=input("Enter your answer :-")
    input()
    
    if ans == quiz[i]['ans']:
        print("Right answer")
        score+=50
    else:
        print("Wrong answer")
        score-=20        

#Example 3

'''student = {
    "Name" : "Ashutosh",
    "Subject" : "Python",
    "Score" : 75
}

for k in student.keys():
    print(k)
    
for v in student.values():
    print(v)    
    
print(len(student.keys()))  '''
