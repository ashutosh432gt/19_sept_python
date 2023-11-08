id=int(input("Enter the id of the student: "))
name=input("Enter name of the student :- ")
subject=input("Enter the subject in which student is studying: ")

f=open("mynote.txt","a")

f.write("\n Id = "+str(id))
f.write("\n Name = "+name)
f.write("\n Subject = "+subject)

f.close()