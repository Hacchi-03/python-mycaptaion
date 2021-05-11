Area of circle code:-
from math import pi
r=float(input("Input The radius of circle"))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


Code for filename:-
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
