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
   



#Given a range of first 10 numbers,Iterate from start number to the end number and print the sum of the current number and previous number.
previous_num = 0
for i in range(10):
    sum = previous_num + i
    print(f'Current number {i} Previous Number {previous_num} is {sum}')
    previous_num = i

#Given a string,display only those characters which are present at an even index number.
def Char(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )

inputStr = "cherima" 
print("Orginal String is: ", inputStr)

print("even index chars:-")
Char(inputStr)

#Given a string and an integer number n , remove character from a string from zero up to n and return  a new string.
def removeChars(str, n):
  return str[n:]

print("Removing n number of chars")
print(removeChars("pynative", 4))

#Given a list of numbers, return true if first and last number of a list is same .
def ckeckList(lst):
  list= lst[0] 
  abc = True  
  for item in lst:
    if list != item:
      abc = False
      break; 
              
    if (abc == True):
       print("Equal") 
    else: 
      print("Not equal")             
lst = ['ABCD', 'ABCD', 'ABCD', 'ABCD', ] 
ckeckList(lst)

#Given  a list of numbers, Iterate it and print only those numbers which are divisible of 5.
lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
n=int(input("Enter the number to be divided by:"))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)
        
#Return the total count of sub-string "Emma" appears in the appears in the given string.               
#Given string is"Emma is good developer .Emma is a writer."        
sampleStr = "Emma is good developer. Emma is a writer"
cnt = sampleStr.count("Emma")
print(cnt)

#Print the following pattern:  
1
22
333
4444
55555

rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end=" ")
    print(" ")  
    
 #Reverse a given number and return true if it is the same as the original number.
def rev_number(n):
  s = 0
  while True:
    k = str(n)
    if k == k[::-1]:
      break
    else:
      m = int(k[::-1])
      n += m
      s += 1
  return n 
print(rev_number(1473))
  
#Given a two list of numbers create a new  list such that new list should contain only odd numbers from the first list and even 
numbers from the second list.  
from numpy import array
a=array([1,2,3,4,5,6]) 
b=array([7,8,9,10,11,12]) 

c = [*a[a%2 == 0], *b[b%2 != 0]]
print(c)

#Write a code to extract each digit from an integer, in the reverse order.
num = int(input("Enter any Number: "))
Result = 0
def Result_Int(num):
    global Result
    if(num > 0):
        Reminder = num %10
        Result = (Result *10) + Reminder
        Result_Int(num //10)
    return Result
 
Result = Result_Int(num)
print("Reverse of entered number is = %d" %Result)