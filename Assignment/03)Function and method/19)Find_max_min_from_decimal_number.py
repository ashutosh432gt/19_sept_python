# Write a Python program to find the maximum and minimum numbers
# from the specified decimal numbers.

def max_min(num):
    max_num=max(num)
    min_num=min(num)
    return max_num,min_num


float_numbers=[1.1,1.2,2.3,5.6,7.8]

maximum,minimum=max_min(float_numbers)

print("The Maximum Number = ",maximum)
print("The Minimum Number is = ",minimum)
