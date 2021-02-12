#! python3
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue
"""

x = input("Please enter a number: ")

x = int(x)
a = 6
b = 8

if x%6 == 0 and x%8 !=0:
    print(str(x) + " " + "is frue")
else:
    print(str(x) + " " + "is not frue")