print("----------------------Jay Bhavani Fast Food----------------------")
Item_name=["vadapav","dabeli","bhel"]
Item_price=[30,20,75]
total=0
ordered_items=[]
status=True
while status:
    print("              ---------------Menu---------------")
    menu="""
                 1.Vadapav     INR 30
                 2.Dabeli      INR 20
                 3.Bhel        INR 75
    """
    print(menu)
    choice=input("Enter Product Name  : - ").lower()
    quantity=int(input("Enter Quantity :- "))
    
    index_number=Item_name.index(choice)
    price=Item_price[index_number]
    if choice=="vadapav" and "vadapav" in Item_name :
         print("Thank you For ordering Vadapav")
         sum=quantity*price
         print("{} X {} = INR {}".format(choice,quantity,sum))
    elif choice=="dabeli" and "dabeli" in Item_name :
        print("Thank you For ordering Dabeli")
        sum=quantity*price
        print("{} X {} = INR {}".format(choice,quantity,sum))  
    elif choice=="bhel" and "bhel" in Item_name :
        print("Thank you For ordering Bhel")
        sum=quantity*price
        print("{} X {} = INR {}".format(choice,quantity,sum))  
    else:
        print("{} is not in Menu.Please select items from giving menu below")
        status=True
        continue
    
    total+=sum
    ordered_items.append((choice, quantity))
    
    option=input("Do you want to add more items to your cart : Presee 'Y' for Yes or 'N' for No :- ").upper()
    if option=="Y" or option=="YES":
        status=True
        continue            
    elif option=="N" or option=="NO":
        break

    status=False
    
print("---------Your Bill---------")
for item, quantity in ordered_items:
    index = Item_name.index(item)
    price = Item_price[index]
    print("{} X {} =  INR {}".format(item,quantity,quantity*price))
print("----------------------------")
print("Total Bill = INR", total)