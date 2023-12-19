print("Welcome to Amazing Pizza and Pasta Pizzazaria")
#class for main menu
class Main:
    option="""
            1.Order Menu
            2.Exit
    """
    def displayMain(self):
        print(self.option)
#class for sub menu or order menu options
class Sub:
    Pizza_menu="""
                1.1 Large Pizza 10.99 AUD
                2.2 Large Pizza 20.99 AUD
                3.3 Large Pizza 29.99 AUD
                
    """
    Pizza_offer="""
                    Buy 4 or more pizza and get 1.5lt of soft drink free
    """
    
    Pasta_menu="""
                4.1 Large Pasta 9.5 AUD
                5.2 Large Pasta 17.00 AUD
                6.3 Large Pasta 27.50 AUD

    """
    
    offer="""
            Buy 4 or more pastas and get 2 bruschetta Free
            Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free
    """
    
    def displaySub(self):
        print(self.Pizza_menu)
        print(self.Pizza_offer)
        print(self.Pasta_menu)
        print(self.offer)
#declaring variable for storing total order history of each category
pizza=0
pasta=0
soft_drinks = 0
bruschetta = 0
chocco_brownies = 0
pizza_payment=0
pasta_payment=0
        
status=True

while status:
        m=Main()
        m.displayMain()
        option=int(input("Enter Your Choice :- "))
        if option==1:
            s=Sub()
            s.displaySub()    
            name=input("Enter Your Name :- ") 
            print("Welcome ",name)
            quantity=int(input("Enter Pizza Quantity :- "))
            if quantity==1:
                cost=10.99
                pizza_cost=cost*quantity
                pizza+=1
                pizza_payment+=pizza_cost
            elif quantity==2 :
                cost=20.99
                pizza_cost=cost*quantity
                pizza+=2
                pizza_payment+=pizza_cost
                
            elif quantity==3:
                cost=29.99
                pizza+=3
                pizza_cost=cost*quantity
                pizza_payment+=pizza_cost
                
            elif quantity>=4:
                cost=10.99
                pizza_price=quantity*cost
                print("Congratulations !! 1.5lt softdrink free")
                pizza+=quantity
                soft_drinks += 1
                pizza_payment+= pizza_price
            else:
                cost=10.99
                pizza_price=quantity*cost
                pizza+=quantity
                soft_drinks += 1
                pizza_payment += pizza_price
                
            quantity1=int(input("Enter Pasta Quantity :- ")) 
            if quantity1==1:
                cost=9.5
                pasta_cost=cost*quantity1
                pasta_payment+=pasta_cost
                pasta+=1
            elif quantity1==2 :
                cost=17.00
                pasta_cost=cost*quantity1
                pasta_payment+=pasta_cost
                pasta+=2
            elif quantity1==3:
                cost=27.5
                pasta_cost=cost*quantity1
                pasta_payment+=pasta_cost
                pasta+=3
            elif quantity1>=4:
                cost=9.5
                pasta_price=quantity1*cost
                print("Congratulations !! get 2 bruschetta free")
                pasta_cost=cost*quantity1
                pasta_payment+=pasta_cost
                pasta+=quantity1
                bruschetta += 2
            else:
                cost=9.5
                pasta_cost=quantity1*cost
                pasta_payment+=pasta_cost
                pasta+=quantity1
                 
            #if both pizza and pasta order is greater than 4 
            total_offer=quantity+quantity1
            if total_offer>=4:
                print("Congratulations !! get 2 chocco brownies ice cream free") 
                chocco_brownies += 2
            else:
                pass          
            user=input("Do you want to add more customers order? (y/n) :- ").lower()
            if user=="y":
                continue
            else:
                break
        else:
            break    
print("\n----------- Pizza and Pasta Bill --------------")
print(f"Payment received from pizza {pizza_payment} AUD")
print(f"Payment received from pasta {pasta_payment} AUD")
print("payment received today :",pizza_payment+pasta_payment)
print("Number of pizza and pasta sold in one shift : ",pizza+pasta)
print(f"Number of 1.5lt soft drink bottles given : {soft_drinks}")
print(f"Number of bruschetta given to customer : {bruschetta}")
print(f"Number of chocco brownies ice cream given to customer : {chocco_brownies}")
print("Bye Bye!")        
status=False            
            
            