product={}

menu = """
       jay Bhavani
       
       Vadapav : 35
       Dabeli : 30
       Bhel   : 75

"""
print(menu)

status = True
while status:
    specification={}
    product_name=input("Enter Product Name : ")
    qty=int(input("Enter Quantity : "))
    price=int(input("Enter Product Price : "))
    
    specification['qty'] = qty
    specification['price'] = price
    
    product[product_name]=specification
    
    choice=input("Do you want to add more items : ").lower()
    if choice =="y" or choice=="yes":
        status=True
    
    