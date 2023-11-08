menu="""
    Press 1 for Beginner
    Press 2 for Intermediate
    Press 3 for Advanced

"""
status=True
while status:
    print(menu)
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("You have selected Beginner")
        beginner=[
            "1."
            
        ]
