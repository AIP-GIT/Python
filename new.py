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

#que4.Write a program to compute simple interest.
p=int(input("Enter any number for p:"))
r=int(input("Enter any number for r:"))
t=int(input("Enter any number for t:"))
SI=(p*r*t)/100
print(SI)


#que5.write a program to find GCD of two numbers
num1=int(input("enter any num1:"))
num2=int(input("enter any num2:"))
for i in range(1,num2+1):
  if(num1%i==0 and num2%i==0):
    GCD=i
print(GCD)


#que6Program for maximum of 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest= num3
 
print("The maximum of 3 numbers are:",largest)
