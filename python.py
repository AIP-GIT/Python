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