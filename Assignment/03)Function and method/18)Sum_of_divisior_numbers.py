# Write a Python program to returns sum of all divisors of a number
def sum(num):
    sum_of_all_divisors=0
    for i in range(1,num+1):
        if num%i==0:
            sum_of_all_divisors+=i
    return sum_of_all_divisors

n=int(input("Enter a Number :- "))
result=sum(n)
print(f"The sum of all divisors of a {n} = {result}")        
