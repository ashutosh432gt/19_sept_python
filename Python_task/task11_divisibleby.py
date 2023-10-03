a=int(input("Enter a number to check it is divisible by 5 or 11 :-"))

if a%5==0 and a%11==0:
    print("{} divisible by both 5 and 11".format(a))
elif a%11==0:
    print("{} is divisible by 11".format(a)) 
elif a%5==0:
    print("{} is divisible by 5".format(a))
else:
    print("{} not divisible by 5 nor by 11".format(a))           