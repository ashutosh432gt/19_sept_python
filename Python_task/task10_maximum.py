num1=int(input("Enter First Number :- "))
num2=int(input("Enter Second Number :- "))
num3=int(input("Enter Third Number :- "))

if num1>num2 and num1>num3:
    print("{} is greater than {} and {}".format(num1,num2,num3))
elif num2>num1 and num2>num3:
    print("{} is greater than {} and {}".format(num2,num1,num3)) 
elif num3>num1 and num3>num2:
    print("{} is greater than {} and {}".format(num3,num1,num2))
else:
    print("All are equal")    