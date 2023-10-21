menu = """
     MENU
  Press 1 for product manager
  Press 2 for customer panel
"""

products = {}  # Creating a blank dictionary

flag = True
while flag:
    print(menu)
    choice = int(input("Enter your choice: "))
    status = True
    if choice == 1:
        # Product manager panel
        while status:
            specific_product = {}
            product_name = input("Enter Product name: ")
            product_qty = int(input("Enter Quantity: "))
            product_price = int(input("Enter Product price per 1kg quantity: "))

            if product_name in products:
                # Fetch old qty from the dictionary
                old_qty = products[product_name]['qty']
                specific_product['qty'] = old_qty + product_qty
                specific_product['price'] = product_price
            else:
                specific_product['qty'] = product_qty
                specific_product['price'] = product_price

            products[product_name] = specific_product

            print("Products = ", products)

            choice = input("Do you want to add more products? (yes/no): ").lower()
            if choice == "yes" or choice == "y":
                status = True
            else:
                status = False

    elif choice == 2:
        # Customer panel
        print("::::: PRODUCTS MENU :::::")
        for product_name in products:
            print(f"{product_name} - 1kg price INR {products[product_name]['price']}")

        status = True
        cart = {}
        total_bill = 0  # Initialize the total bill

        while status:
            name = input("Enter Product Name: ")
            if name in products:
                print(f"You have selected: {name} - 1kg price INR {products[name]['price']}")
                quantity = int(input("Enter quantity: "))

                if quantity > products[name]['qty']:
                    print("Insufficient quantity. Available quantity:", products[name]['qty'])
                else:
                    specific_product = {'Product_Name': name, 'Quantity': quantity}
                    cart[name] = specific_product

                    # Calculate the cost for the current item and add it to the total bill
                    item_cost = quantity * products[name]['price']
                    total_bill += item_cost

                choice = input("Do you want to add more items to the cart? (yes/no): ").lower()
                if choice == "yes" or choice == "y":
                    status = True
                else:
                    status = False
            else:
                print("Product not found in the menu. Please choose a valid product.")

        print("Items in your cart:")
        for item, details in cart.items():
            print(f"{details['Product_Name']} - Quantity: {details['Quantity']}")
        
        
        print(f"Total Bill: INR {total_bill}")  # Display the total bill

        

    else:
        print("Invalid choice. Please select a valid option (1 for product manager, 2 for customer panel).")

    