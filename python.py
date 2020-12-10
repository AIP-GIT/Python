# Write a program to compute simple interest.
p=int(input('Enter the principal amount: '))
r=float(input('Enter the rate: '))
t=int(input('Enter the time in year: '))
SI=(p*r*t)/100
print('Simple interest: ',SI)

# Write a program to find GCD of two numbers
p=int(input("Enter first number: "))
r=int(input("Enter second number: "))
for i in range(1,r+1):
  if (p%i==0 and r%i==0):
    Gcd=i
print(Gcd)

# You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. 
#The numbers are in the range of 1 to 6, 
#like any ordinary dice. Input a dice face number, and output the opposite face number
p=int(input('Enter face: '))
while(p<6 or p>1):
  n=7-p
print(n)

# Find the average of numbers in a list
n = int(input("Enter number of elements : ")) 
b = []
for i in range(n): 
  e=int(input("Enter the numbers: ")) 
  b.append(e) 
s=sum(b)
avg=s/n
print(avg)

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included
n=[]
for num in range(2000,3200):
 if (num%7==0) and (m%5!=0):
  n.append(str(num))
print (','.join(n))

# Perform operations on complex type values.(ie … 10+1.5j)
a=complex(input('Enter First Number: '))
b=complex(input('Enter second Number: '))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# Program for maximum of 3 numbers.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1>num2 and num1>num3:
  print("Maximum Number is: ",num1)
elif num2>num1 and num2>num3:
  print("Maximum Number is: ",num2)
else:
  print("Maximum Number is: ",num3)
  
# Program for minimum of 3 numbers
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1<num2 and num1<num3:
  print("Minimum Number is: ",num1)
elif num2<num1 and num2<num3:
  print("Minimum Number is: ",num2)
else:
  print("Minimum Number is: ",num3)
  
# Find sum of digits in a number
n=int(input("Enter Digit: "))
sum=0
for i in str(n):
 if n!=0:
   sum = int(sum + n % 10)
   n = n/10
print(sum)

# Find if a list is sorted in increasing order
test_list=[1,4,5,8,10]
test_list.sort()
print(test_list)

# Write a program which accepts the radius of circle from the user and compute the area.
r=int(input('Enter Radius: '))
Area=3.14*r*2
print(Area)

# Python program to find the squareroot.
num=int(input('Enter Number: '))
Sr=num*2
print(Sr)

# Python program to swap two variables.
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=a
a=b
b=c
print("First Number After Swap:",a)
print("Second Number After Swap:",b)

# Python program to check whether the number is positive , negative or 0.
num=int(input("Enter number: "))
if (num>0):
       print("Number is Positive")
elif (num==0):
     print("Number is Zero")
else:
     print("Number is Negative")
	 
# Give a two integer number and return their product and if the product is greater than 1000,then return their sum.
p=int(input("Enter first number: "))
r=int(input("Enter second number: "))
product=p*r
if (product>1000):
 sum=p+r
 print("Sum is: ",sum)
else:
 print("Product is: ",product)
 
 # Given a range of first 10 numbers,Iterate from start number to the end number and print the sum of the current number and previous number.
p_num = 0
for i in range(10):
    sum = p_num + i
    print(sum)
    p_num = i
	
# Given a string,display only those characters which are present at an even index number.
num=str(input("Enter string: "))
c=num[0::2]
print(c)

# Given a string and an integer number n , remove character from a string from zero up to n and return  a new string.
str=input("Enter string: ")
def rc(str, n):
  return str[n:]
n=int(input("Enter number of character to be removed: "))
print(rc(str, n))

# Given a list of numbers, return true if first and last number of a list is same .
n = int(input("Enter number of elements : ")) 
b = []
for i in range(n): 
  e=int(input("Enter the numbers: ")) 
  b.append(e)
  res =  [ b [i] for i in (0, -1) ]
firstElement = b[0]
lastElement = b[-1]
if (firstElement == lastElement):
  print("The first and last element of list are : ",res) 
else:
 print('The first and last element are not same')
 
# Given  a list of numbers, Iterate it and print only those numbers which are divisible of 5.
 b = [1,4,2,5,7]
for i1 in b: 
 if (i1%5==0):
  print(i1)

