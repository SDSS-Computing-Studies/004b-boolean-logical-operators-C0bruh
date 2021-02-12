#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
x = input("please enter a number: ")

x = int(x)
a = 0

if x > a:
    print(str(x) + " " + "is a positive integer.")
elif x < a:
    print(str(x) + " " + "is not a positive integer")