principle_amount=int(input("Enter Principle amount :- "))
rate_of_intrest=int(input("Enter rate of intrest % :- "))
time_period=int(input("Enter time period in years :- "))

a=principle_amount*rate_of_intrest*time_period

simple_intrest=a/100

print("Simple Intrest = {} * {} * {} / 100 = {}".format(principle_amount,rate_of_intrest,time_period,simple_intrest))