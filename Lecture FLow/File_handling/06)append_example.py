status=True
f=open("logfile.txt","a+")
while status:
    name=input("Enter your name :- ")
    subject=input("Enter your subject :- ")
    
    f.write("\n name = "+name)
    f.write("\n subject = "+subject)
    
    choice=input("Do you want to enter more data : press y for yes ")
    if choice=="y" or choice=="yes":
        status=True
    else:
        status=False    
        
f.close()        