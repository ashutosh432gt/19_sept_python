import datetime
status=True
while status:
    print("-------------------------------------------")
    date=datetime.datetime.now().strftime("%d/%m/%Y")
    
    name=input("Enter Your Name :- ")
    Email=input("Enter Your Email exclude(@gmail.com) :- ")
    Contact_no=int(input("Enter Your Contact Number :- "))
    gender=input("Enter Your Gender :- ")
    age=int(input("Enter your age :- "))
    vaccine_name=input("Enter your Vaccine Name :- ")
    Vaccination_doze=int(input("Enter your vaccination doze :- "))
    
    f=open("Vaccination_record.txt","a")
    f.write("-------------------------------------------\n")
    # f.write(datetime.datetime.now())
    print()
    f.write("Added at "+date+"\n")
    f.write("Name :- "+name+"\n")
    f.write("Email : "+Email+"@gmail.com"+"\n")
    f.write("Contact Number : "+str(Contact_no)+"\n")
    f.write("Gender : "+gender+"\n")
    f.write("Age : "+str(age)+"\n")
    f.write("Vaccine Name : "+vaccine_name+"\n")  
    f.write("Vaccination Doze : "+str(Vaccination_doze)+"\n")
    
    choice=input("Do you want to add more data? (y/n) :- ").lower()
    if choice=="y" or choice=="yes":
        continue
    else:
        f.close()
        break