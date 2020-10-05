
num=input("Enter a number")
num=int(num)
if num>0 or num==0:
    num=str(num)
    print( num+" is a positive integer")
elif num<0:
    num=str(num)
    print(num+ " is not a positive integer")
