#Write a Python program that accepts an integer (n) and computes the value of
#n+nn+nnn.

n=int(input("Enter any Integer :- "))
#applying calculation to find n+nn+nnn
#if we multiply any number with 1 it remains same for example 2*1=2
#as we can see nn is two digit number so we multiplied it with 11 same way for triple digit
nn=n*11
nnn=n*111
total=n+nn+nnn

print("{} + {} + {} = {}".format(n,nn,nnn,total))