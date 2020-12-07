# Que1.Write a Python program which accepts the radius of a circle from the user and compute the area. Sample Output :
#r = 1.1
#Area = 3.8013271108436504
from math import pi
r = float(input ("enter the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


#Que2.Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
f_name = input("Input your First Name : ")
l_name = input("Input your Last Name : ")
print ("in reverse" + l_name + " " + f_name)

#que3.Python Program to convert complex numbers to Polar coordinates.... 
import cmath 
c = complex(1+5j) 
print(abs(c)) 

