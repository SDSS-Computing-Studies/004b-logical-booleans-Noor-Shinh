#! python3
"""
Ask the user to enter a name. 
If the name is one of the names on a list of special users, greet them by name.
(2 points) 

Inputs:
Name (string)

Outputs:
You are not a VIP.
Hi xxxxxx! You are a VIP!

Example:
Enter your name=>Gertrude
Hi Gertrude! You are a VIP!

Enter your name=>Gordon
You are not a VIP.
"""

VIPNames = ("Guile","Blanka","Christine","Carol","Richard","Daniel","Chun-Li")
name=input("Enter your name")
if ("Guile")==name or ("Blanka")==name or ("Christine")==name or ("Carol")==name or ("Richard")==name or ("Daniel")==name or ("Chun-li")==name:
    print("hi "+name+'! You are are a Vip!')
else:
    print("You are not a VIP.")