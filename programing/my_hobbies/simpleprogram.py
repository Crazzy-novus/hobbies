import math
n=int(input("enter the value of n"))
print(math.factorial(n))
"""" withut using built in function"""
def fact(n):
    if(n==1 or n==0):

        return 1
    else:
        fact=1
        i=n
        while(n>1):
            fact=fact *n
            n-=1
        return fact
print(fact(n))
""" program to find simple intrest """
p,t,r=float(input("enter the value of p,t,r,")),float(input()),float(input())
def simpleintrest(p,t,r):
    si=((p*t*r)/100)
    return si
print(simpleintrest(p,t,r))
