print("------------------Welcome To Kalyan Jewellers------------------")
print()
name=input("Enter Your Name :- ")
gender=input("Enter your gender Male/Female :- ")
age=int(input("Enter Your age :- "))
status=True      #Declaring variable for running loop or we can call it intitlization
while status:    #Applying entry condition to run this loop repeatedly

    product_name=input("Enter Product name :- ")
    product_weight=int(input("Enter product weight in grams :- "))
    current_gold_price=int(input("Enter current gold price per grams :- "))
    purchase_value=current_gold_price * product_weight
    making_charges=845  #making charges per gram
    x=200000 
    y=300000
    z=500000
    total_making_charges=product_weight * making_charges  
    total_amount=purchase_value + total_making_charges
    a=purchase_value/100
    print()
    #conditional statement applied if the user's gender is male
    if gender=="male" or gender=="Male":
        #condtional statement for male user if thier age is above 65 (nested)
        if age>65:
            #conditional statement if the total amount of purchase is between 2 Lakh and 3 Lakh
            if total_amount>x and total_amount<y:
                discount=a*20 #20% discount applied
                print()
                #Bill genration
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount 20%                 - INR ",discount)
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - discount)
            #conditional statement if the total amount of purchase is between 3 Lakh and 5 Lakh    
            elif total_amount>y and total_amount<z:
                discount=a*30 #30% discount applied
                print()
                #Bill generation
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount 30%                 - INR ",discount)
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - discount )
            #conditional statement if the total amount of purchase is above 5 Lakh     
            elif total_amount>z:
                discount=a*35 #35% discount applied
                print()
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount 35%                 - INR ",discount)
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - discount )
            #conditional statement if the total amount of purchase is below 2 Lakh
            else:
                print()
                #Bill generation
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount  0%                 - INR     0")
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - 0 )
    
            #conditional statement for the male users below of 65 age    
        else: 
            #conditional statement if the total amount of purchase is between 2 Lakh and 3 Lakh   
            if total_amount>x and total_amount<y:
                discount=a*10 #10% discount applied 
                print()
                #Bill generation
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount 10%                 - INR ",discount)
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - discount )
            #conditional statement if the total amount of purchase is between 3 Lakh and 5 Lakh    
            elif total_amount>y and total_amount<z:
                discount=a*20 #20% discount applied
                print()
                #Bill generation
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount 20%                 - INR ",discount)
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - discount )
            #conditional statement if the total amount of purchase is above 5 Lakh    
            elif total_amount>z:
                discount=a*25 #25% discount applied
                print()
                #Bill generation
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount 25%                 - INR ",discount)
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - discount )
            #conditional statement if the total amount of purchase is below 2 Lakh 
            else:
                print()
                #Bill generation
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount  0%                 - INR     0")
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - 0 )
    #conditional statement applied if the user's gender is Female        
    elif gender=="Female" or gender=="female": 
        #condtional statement for Female user if thier age is above 65 (nested)
        if age>65: 
            #conditional statement if the total amount of purchase is between 2 Lakh and 3 Lakh                  
            if total_amount>x and total_amount<y:
                discount=a*25 #25% discount applied
                print()
                #Bill generation
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount 25%                 - INR ",discount)
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - discount )
            #conditional statement if the total amount of purchase is between 3 Lakh and 5 Lakh    
            elif total_amount>y and total_amount<z:
                discount=a*35 #35% discount applied
                print()
                #Bill generation
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount 35%                 - INR ",discount)
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - discount )
            #conditional statement if the total amount of purchase is above 5 Lakh    
            elif total_amount>z:
                discount=a*40
                print()
                #Bill generation
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount 40%                 - INR ",discount)
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - discount )
            #conditional statement if the total amount of purchase is below 2 Lakh 
            else:
                print()
                #Bill generation
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount  0%                 - INR     0")
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - 0 )
            
        #conditional statement for the Female users below of 65 age    
        else: 
            #conditional statement if the total amount of purchase is between 2 Lakh and 3 Lakh   
            if total_amount>x and total_amount<y:
                discount=a*15 #15% discount applied 
                print()
                #Bill generation
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount 15%                 - INR ",discount)
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - discount )
            #conditional statement if the total amount of purchase is between 3 Lakh and 5 Lakh    
            elif total_amount>y and total_amount<z:
                discount=a*25 #25% discount applied
                print()
                #Bill generation
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount 25%                 - INR ",discount)
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - discount )
            #conditional statement if the total amount of purchase is above 5 Lakh    
            elif total_amount>z:
                discount=a*35 #35% discount applied
                print()
                #Bill generation
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount 35%                 - INR ",discount)
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - discount )        
        
            #conditional statement if the total amount of purchase is below 2 Lakh 
            else:
                print()
                #Bill generation
                print("---------------Kalyan Jewellers---------------")
                print("Total Gold Purchase value      INR ",purchase_value)
                print("Total Gold Making Charges    + INR ",total_making_charges)
                print("                            -----------------")
                print("Total amount                 = INR ",total_amount)
                print("Discount  0%                 - INR     0")
                print("                            -----------------")
                print("Total Net Amount             = INR ",total_amount - 0 )     
            
    else:
        print()
        print("Invalid Input.Please choose gender between Male/Female")                       
    
    #Asking users again if they want to purchase more items
    choice=input("Do yo want to Continue Purchasing : Enter Yes Or No to Exit :- ").upper()

    if choice=="YES" or choice=="Y":
        status=True
    else:
        #Bill genration
        print("---------------Kalyan Jewellers---------------")
        print("Total Gold Purchase value      INR ",purchase_value)
        print("Total Gold Making Charges    + INR ",total_making_charges)
        print("                            -----------------")
        print("Total amount                 = INR ",total_amount)
        print("Discount 20%                 - INR ",discount)
        print("                            -----------------")
        print("Total Net Amount             = INR ",total_amount - discount)
        status=False    