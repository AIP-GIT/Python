#Give a list of weight and value pairs  for items and a bag with capacity.Calculate the maximum item value that can be carried in the bag . 
#NotItems can be carried in parts/fraction.                    Input:…………. Items as (value , weight) pairs     , 
Items =[(60,10), (100,20),(120,30)]                      
xyz=[(a/b,b) for a,b in Items]
xyz.sort(reverse=True,key=lambda xyz:xyz[0])

total=0
capacity=50
print(xyz)
#xyz=0
for item in xyz:
  if item[1] <=capacity:
    total=total+item[0]*item[1]#60 ,140
    capacity=capacity-item[1]
  else:
    total=total+item[0]*capacity#140+4.0*20=240
    break
print(total)


#Take two list of numbers of products quantities and prices and calculate total price.Use list comprehension and aggregartion .
#Input: product_quantities = [13,5,6,10,11] ; 
#prices = [1.2 , 6.5,1.0,4.8,5.0]  
#output : Total = 157.1
product_quantities = [13,5,6,10,11]
prices = [1.2 , 6.5,1.0,4.8,5.0]
p=sum([a*b for a,b  in zip(product_quantities,prices)])
print(p)

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


#que7.You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. The numbers are in the range of 1 to 6,
 like any ordinary dice. Input a dice face number, and output the opposite face number.
 i=0
while (i>1) or (i<6):
  i=int(input("Enter any number="))
  num=7-i
print(num)


#Find the average of numbers in a list
def average(num):
    sum= 0
    for t in num:
        sum= sum + t           

    avg = sum/ len(num)
    return avg

print("The average is", average([18,25,3,41,5]))


#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included)
for i in range(1500, 2701):
    if (i%7==0) and (i%5==0):
        nl.append(str(x))
print (','.join(nl))


#Perform operations on complex type values.(ie … 10+1.5j)
import cmath
a=10+1.5j
cmath.polar(a)

#Program for minimum of 3 numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
 
if (num1 < num2) and (num1 < num3):
   smallest = num1
elif (num2 < num1) and (num2 < num3):
   smallest = num2
else:
   smallest= num3
 
print("minimum of 3 numbers are:",smallest)

#Find sum of digits in a number
a=int(input("Enter any number:"))
b=int(input("Enter any number:"))
sum=a+b
print("sum of digits:",sum)

#Find if a list is sorted in increasing order
numlist=[]
num=int(input("Enter the total number of list:"))
for i in range(1,num+1):
  value=int(input("Enter the value of %d element:" %i))
  numlist.append(value)




#Write a program which accepts the radius of circle from the user and compute the area.
r=int(input("enter the radius r: "))
pie=3.14
area=2*pie*r
print("area of circle:",area)

#Python program to find the squareroot.
a=int(input("Enter value of a:"))
sq=a*a
print("square root:",sq)

#Python program to swap two variables.
x = 10
y = 50
temp = x 
x = y 
y = temp  
print("Value of x:", x) 
print("Value of y:", y)


#Python program to check whether the number is positive , negative or 0.
number = int(input("Enter number: "))
if number < 0:
   print("The entered number is negative.") 
elif number > 0:
    print("The entered number is positive.")
elif number == 0:
    print("Number is zero.")
else:
    print("The input is not a number")
    
    
 #Give a two integer number and return their product and if the product is greater than 1000,then return their sum.  
def Char(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )
inputStr = input("Enter String ")
print("Orginal String is ", inputStr)
print("Printing only even index chars")
Char(inputStr) 
   



