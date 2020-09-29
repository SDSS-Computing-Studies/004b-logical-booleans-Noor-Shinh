#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
import math
a=input("Enter value 1")
b=input("Enter value 2")
a=int(a)
b=int(b)
if a>b:
    x=a
    y=b
    z=(x/y)
elif a<b:
    x=(b)
    y=(a)
    z=(x/y)
if z==math.floor(z):
    y=str(y)
    x=str(x)
    print(y+" is a factor of "+ x)
else:
    y=str(y)
    x=str(x)
    print(y+" is not a factor of "+x)
