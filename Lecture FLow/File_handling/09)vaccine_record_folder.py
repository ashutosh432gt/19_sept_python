import os
from datetime import datetime

os.mkdir("Vaccination Database")
status = True

while status:
    print("-------------------------------------------")
    date = datetime.now().strftime("%d-%m-%Y")  
    
    name = input("Enter Your Name: ")
    email = input("Enter Your Email (exclude @gmail.com): ")
    contact_no = int(input("Enter Your Contact Number: "))
    gender = input("Enter Your Gender: ")
    age = int(input("Enter your age: "))
    vaccine_name = input("Enter your Vaccine Name: ")
    vaccination_dose = int(input("Enter your vaccination dose: "))

    folder_path = os.path.join("Vaccination Database", date)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    file_path = os.path.join(folder_path, f"{date}.txt")
    f = open(file_path, "a")
    f.write("-------------------------------------------\n")
    f.write("Name: " + name + "\n")
    f.write("Email: " + email + "@gmail.com\n")
    f.write("Contact Number: " + str(contact_no) + "\n")
    f.write("Gender: " + gender + "\n")
    f.write("Age: " + str(age) + "\n")
    f.write("Vaccine Name: " + vaccine_name + "\n")
    f.write("Vaccination Dose: " + str(vaccination_dose) + "\n")
    
    f.close()
    
    choice = input("Do you want to add more data? (y/n): ").lower()
    if choice in ["y", "yes"]:
        continue
    else:
        break
