physics=int(input("Enter your marks obtained in physics out of 100 :- "))
chemistry=int(input("Enter your marks obtained in chemistry out of 100 :- "))
biology=int(input("Enter your marks obtained in biology out of 100 :- "))
maths=int(input("Enter your marks obtained in maths out of 100 :- "))
english=int(input("Enter your marks obtained in english out of 100 :- "))

total=physics+chemistry+biology+maths+english
total1=total/500
percentage=total1*100

print("Marks obtained in percentage % = {} + {} + {} + {} + {} / 500 *100 = {}".format(physics,chemistry,biology,maths,english,percentage))

if percentage>=70:
    print("Distinction")
elif percentage>=60:
    print("First class")
elif percentage>=50:
    print("Second class")
elif percentage>=40:
    print("Pass class") 
else:
    print("Fail")               