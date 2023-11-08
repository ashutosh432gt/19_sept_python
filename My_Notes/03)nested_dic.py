main_dict = {}

no=int(input("Enter the number of elements in the dictionary: "))

for i in range(no):
    subdict={}
    name=input("Enter the name of the person: ")
    subject=input("Enter the subject name: ")
    marks=int(input("Enter the marks of the subject: "))
    
    subdict['subject']=subject
    subdict['marks']= marks
    
    main_dict[name]=subdict
    
print(main_dict)
    
name=input("Enter name which details you want to fetch : ")

d=main_dict[name]

for k,v in d.items():
    print(f"{k} and {v}")