print("------------------Welcome To Kalyan Jewellers------------------")
print()
name=input("Enter Your Name :- ")
gender=input("Enter your gender Male/Female :- ").upper()
age=int(input("Enter Your age :- "))
#declaring variable for calculation of final bill
purchase_value1=0  
total_purchase=0
total_amount1=0
total_making_charges1=0
discount1=0
status=True      #Declaring variable for entry validation loop or we can call it intitlization
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
    discount=0
    
    print()
    #conditional statement applied if the user's gender is male
    if gender=="male" or gender=="M":
        #condtional statement for male user if thier age is above 65 (nested)
        if age>65:
            #conditional statement if the total amount of purchase is between 2 Lakh and 3 Lakh
            if total_amount>x and total_amount<y:
                discount=0.20*purchase_value #20% discount applied
                
            #conditional statement if the total amount of purchase is between 3 Lakh and 5 Lakh    
            elif total_amount>y and total_amount<z:
                discount=0.30*purchase_value #30% discount applied
                
            #conditional statement if the total amount of purchase is above 5 Lakh     
            elif total_amount>z:
                discount=0.35*purchase_value  #35% discount applied
                
            #conditional statement if the total amount of purchase is below 2 Lakh
            else:
                discount=0*purchase_value #0% discount applied
    
            #conditional statement for the male users below of 65 age    
        else: 
            #conditional statement if the total amount of purchase is between 2 Lakh and 3 Lakh   
            if total_amount>x and total_amount<y:
                discount=0.10*purchase_value  #10% discount applied 
                
                
            #conditional statement if the total amount of purchase is between 3 Lakh and 5 Lakh    
            elif total_amount>y and total_amount<z:
                discount=0.20*purchase_value  #20% discount applied
                
            #conditional statement if the total amount of purchase is above 5 Lakh    
            elif total_amount>z:
                discount=0.25*purchase_value   #25% discount applied
                
            #conditional statement if the total amount of purchase is below 2 Lakh 
            else:
                discount=0*purchase_value #0% discount applied
    #conditional statement applied if the user's gender is Female        
    elif gender=="Female" or gender=="female": 
        #condtional statement for Female user if thier age is above 65 (nested)
        if age>65: 
            #conditional statement if the total amount of purchase is between 2 Lakh and 3 Lakh                  
            if total_amount>x and total_amount<y:
                discount=0.25*purchase_value #25% discount applied
                
            #conditional statement if the total amount of purchase is between 3 Lakh and 5 Lakh    
            elif total_amount>y and total_amount<z:
                discount=0.35*purchase_value #35% discount applied
                
                
            #conditional statement if the total amount of purchase is above 5 Lakh    
            elif total_amount>z:
                discount=0.40*purchase_value #40% discount applied
                
                
            #conditional statement if the total amount of purchase is below 2 Lakh 
            else:
                discount=0*purchase_value #0% discount applied
                
            
        #conditional statement for the Female users below of 65 age    
        else: 
            #conditional statement if the total amount of purchase is between 2 Lakh and 3 Lakh   
            if total_amount>x and total_amount<y:
                discount=0.15*purchase_value #15% discount applied 
                
                
            #conditional statement if the total amount of purchase is between 3 Lakh and 5 Lakh    
            elif total_amount>y and total_amount<z:
                discount=0.25*purchase_value #25% discount applied
                
                
            #conditional statement if the total amount of purchase is above 5 Lakh    
            elif total_amount>z:
                discount=0.35*purchase_value #35% discount applied
                
                       
        
            #conditional statement if the total amount of purchase is below 2 Lakh 
            else:
                discount=0*purchase_value     #0%discount applied
    #If users input is wrong        
    else:
        print()
        print("Invalid Input.Please choose gender between Male/Female")                       
    
    #added calculation to calculate final bill after several purchases
    purchase_value1+=purchase_value
    total_making_charges1+=total_making_charges
    total_amount1+=total_amount
    discount1+=discount   
    #Asking users again if they want to purchase more items
    print()
    choice=input("Do yo want to Continue Purchasing : Enter Yes Or No to Exit :- ").upper()
    
    if choice!="YES" and choice!="Y":
        status=False
        
    
#printing bill outside the loop for final calculation to avoid repetition     
print("---------------Kalyan Jewellers---------------")
print("Total Gold Purchase value      INR ",purchase_value1)
print("Total Gold Making Charges    + INR ",total_making_charges1)
print("                            -----------------")
print("Total amount                 = INR ",total_amount1)
print("Discount                     - INR ",discount1)
print("                            -----------------")
print("Total Net Amount             = INR ",total_amount1 - discount1 )        