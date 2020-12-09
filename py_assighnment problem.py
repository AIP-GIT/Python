Q.Take two list of numbers of products quantities and prices and calculate total price.Use list comprehension and aggregartion . #Input: product_quantities = [13,5,6,10,11] ; prices = [1.2 , 6.5,1.0,4.8,5.0]

product_quantities = [13,5,6,10,11]
prices = [1.2 , 6.5,1.0,4.8,5.0]
lst.append(prices)
print("Sum of elements in given list is :", sum(prices)) 
output:
Sum of elements in given list is : 18.5

Q.2 Write a Python program which accepts the radius of a circle from the user and compute the area. 
x = int(input("Enter x value : "))
y = int(input("Enter y value : "))
r = int(input("Enter radius : "))

print("Area : " ,3.14*r**2)
print("d : ",(x**2+y**2)**0.5-r)

output:Enter x value : 2
Enter y value : 4
Enter radius : 5
Area :  78.5
d :  -0.5278640450004204

Q.3Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

firstname = input("Input your First Name : ")
lastname = input("Input your Last Name : ")
print ("hey  " + lastname + " " + firstname)

output:
Input your First Name : aliya
Input your Last Name : siddiki
hey  siddiki aliya

Q 4.Python Program to convert complex numbers to Polar coordinates.... 

mport cmath 
  
  
x = -1.0
y = 0.0
z = complex(x,y);  
  
# printing phase of a complex number using phase()  
print ("The phase of complex number is : ",end="")  
print (cmath.phase(z)) 
output:
The phase of complex number is : 3.141592653589793

Q 5.Write a program to compute simple interest.

p=int(input('Enter the principal amount: '))
r=float(input('Enter the rate: '))
t=int(input('Enter the time in year: '))
SI=(p*r*t)/100
print('Simple interest: ',SI)

Q.6 Write a program to find GCD of two numbers

p=int(input("Enter first number"))
r=int(input("Enter second number"))
for i in range(1,r+1):
  if (p%i==0 and r%i==0):
    Gcd=i
print(Gcd)

Q.7 You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. The numbers are in the range of 1 to 6, like any ordinary dice. Input a dice face number, and output the opposite face number

p=int(input('Enter face: '))
if p==1 :
  print(6)
elif p==2:
    print(5)
elif p==3:
  print(4)
elif p==4:
    print(3)
elif p==5:
  print(2)
else:
  print(1)
  
 Q.8 Find the average of numbers in a list
  
  n = int(input("Enter number of elements : ")) 
b = list()
for i in range(n): 
  e=int(input("Enter the numbers ")) 
  b.append(e) 
s=sum(b)
avg=s/n
print(avg)

Q.10 Program for maximum of 3 numbers.

um1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1>num2 and num1>num3:
  print("Maximum Number is",num1)
elif num2>num1 and num2>num3:
  print("Maximum Number is",num2)
else: print("Maximum Number is",num3)

Q.11 Perform operations on complex type values.(ie … 10+1.5j)

a=complex(input('Enter First Number: '))
b=complex(input('Enter second Number: '))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

Q.12 Program for minimum of 3 numbers

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1<num2 and num1<num3:
  print("Minimum Number is",num1)
elif num2<num1 and num2<num3:
  print("Minimum Number is",num2)
else:
  print("Minimum Number is",num3)
  
Q.13 Find sum of digits in a number

def getSum(n):  
     
    sum = 0
    for digit in str(n):   
      sum += int(digit)        
    return sum
    
 Q.14 Write a program which accepts the radius of circle from the user and compute the area.

r=int(input('Enter Radius:'))
Area=3.14*r*2
print(Area)

Q.15 Python program to find the squareroot.
um=int(input('Enter Number:'))
Sr=num*2
print(Sr)

Q.16 Python program to swap two variables.
 a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=a
a=b
b=c
print("First Number After Swap:",a)
print("Second Number After Swap:",b)

Q.17 Python program to check whether the number is positive , negative or 0.

um=int(input("Enter number:"))
if (num>0):
       print("Number is Positive")
elif (num==0):
     print("Number is Zero")
else:
     print("Number is Negative")
     
Q.18 Give a two integer number and return their product and if the product is greater than 1000,then return their sum.
p=int(input("Enter first number"))
r=int(input("Enter second number"))
product=p*r
if (product>1000):
 sum=p+r
 print("Sum is",sum)
else:
 print("Product is",product)
 
 Q.19 Given a string,display only those characters which are present at an even index number.
 
 num=str(input("Enter string: "))
c=num[0::2]
print(c)

Q,20 Given a list of numbers, return true if first and last number of a list is same .

n = int(input("Enter number of elements : ")) 
b = list()
for i in range(n): 
  e=int(input("Enter the numbers ")) 
  b.append(e)
  res =  [ b [i] for i in (0, -1) ]
print ("The first and last element of list are : " +  str(res)) 

Q.21 Given  a list of numbers, Iterate it and print only those numbers which are divisible of 5.
 = int(input("Enter number of elements : ")) 
b = list()
for i in range(n): 
  e=int(input("Enter the numbers ")) 
  b.append(e)
for i1 in b: 
 if (i1%5==0):
  print(i1)
  
  Q.21 Return the total count of sub-string "Emma" appears in the appears in the given string.   Given string is"Emma is good developer .Emma is a writer."
  
  s=input('Enter string')
s1=input('Enter substring')
t=s
c=t.count(s1)
print(s1,c)

Q.22 Reverse a given number and return true if it is the same as the original number.

n = int(input('Enter Number: ')); 
rev = 0
orig=n
for i in range (n):
  if (n>0):
    a = n % 10
    rev = rev * 10 + a 
    n = n//10
if orig == rev:
 print(orig)
  
  Q.23 Python program to check leap year 
  
  if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
    
    Q.24 Python program to check odd or even.
    
    m = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
   
  Q.25 Find the maximum element in the list without using max function.
  list1 = [10, 20, 4, 45, 99] 
  
# sorting the list 
list1.sort() 
  
# printing the last element 
print("Largest element is:", list1[-1]) 

Q.26 Find if the substring exists in the string without using in operator
test_str = "aliya"
  
# using str.find() to test 
# for substring 
res = test_str.find("ya") 
if res >= 0: 
    print ("for is present in aliya") 
else : 
    print ("for is not present in aliya")
    
    Q.27 Take an integral number N as an input and calculate the sum of first N natural numbers.
    
    num = 7
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
   
   Q 28.Write a program which can generate and print a list and tuple where the value are square of numbers between 1 and 20(both included).
   
   n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)
Program Explanation

Q.29 Write a program to find consonants in a string .

nput1 =("aliya")
x=('aeiou')
S=[]
for i in input1:
  if i lower function not in x:
    (S.append(i))
print(S)

Q.30 .Write a program that accepts a sentence and calculate the number of letters and digits.
Example: Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

q.31.Write a program that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the program should print both the strings line by line.

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
count1 = 0
count2 = 0
for i in string1:
      count1 = count1 + 1

for j in string2:
      count2 = count2 + 1

if (count1 < count2):
      print ("Larger string is:")
      print (string2)

elif (count1 == count2):
      print ("Both strings are equal.")
else:
      print ("not equal length:")
      print (string1)
      
      Q.32 Check for Palindrome in a string without using loop statement.
      
      s = "malayalam"
ans = isPalindrome(s)
if ans:
    print("yes")
else:
    print("No")
    
    Q.33 Sort an unsorted array in increasing order without using sort function
Example: If the input is [2, 5, 1, 6, 4] output should be [1, 2, 4, 5, 6]

def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90] 
  
bubbleSort(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]), 

Q.34 Write a program to find Leap year

ear = int(input("Enter the Year: "))
if (Year % 400==0): 
    print(Year,"is a leap Year")
elif (Year % 4==0 and Year % 100 != 0):
    print(Year,"is a leap year")
else:
    print(Year,"is a not leap year")
    
  Q.35 Input a comma separated list from console. Write a program to print this list afterremoving all duplicate values with original order reserved.
    
    tr = str (raw_input ("Enter comma separated integers: "))
print ("Input string: ", str)

# conver to the list
list = str.split (",")
print "list: ", list

# convert each element as integers
li = []
for i in list:
 li.append(int(i))

# print list as integers
print "list (li) : ", li

Q 36.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Suppose the following input is supplied to the program:
Hello world Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

from string import *

lines = []
print() "Enter sequence of lines")

while True:
 line = raw_input("")
 if not line:
  break
 lines.append(line.upper())

print lines:

Q.37 Write a program to find palindromic numbers between 2 numbers
Hint: Palindromic number between 10 to 50 are 11, 22, 33, 44

def isPalindrome(n: int) -> bool: 
  
    # Find reverse of n 
    rev = 0
    i = n 
    while i > 0: 
        rev = rev * 10 + i % 10
        i //= 10
  
    # If n and rev are same,  
    # then n is palindrome 
    return (n == rev) 
  
# prints palindrome between min and max 
def countPal(minn: int, maxx: int) -> None: 
    for i in range(minn, maxx + 1): 
        if isPalindrome(i): 
            print(i, end = " ") 
  
# Driver Code 
if __name__ == "__main__": 
    countPal(10, 15) 
    


Q 40.What is the output of tuple [1:3] if tuple =('abcd', 786,2.23,"john",70.2)? 

  786,john
  
Q.41 Given a list A and a number n, find the n’th largest number.
Example: If the input list is [5, 2, 1, 7, 4] and n is 3. The 3rd largest number is 4

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for item in list1:
    if (item > 150):
        break
    if(item % 5 == 0):
        print(item)
        
        Q.42 Print  the words that are  in sonnet_words.txt but not in sowpods.txt
        
        open('/content/drive/My Drive/AIP batch 1/sowpods.txt')
sowp_words= sowp_obj.readlines()

sown_obj = open('/content/drive/My Drive/AIP batch 1/sonnet_words.txt')
sown_words= sowp_obj.readlines()

sowp_words_cln = [word.strip()for word in sowp_words]
sown_words_cln = [word.strip() for word in sown_words]
for word in sowp_words_cln:
  if word not in sown_words_cln:
    print(word)

sowp_obj.close()
sown_obj.close()

43.Given a string of odd length greater 7, return a string made of the middle three chars of a given String. Given: str1 = "JhonDipPeta"     str2 = "JaSonAy"

ef getMiddleThreeChars(sampleStr):
  middleIndex = int(len(sampleStr) /2)
  print("Original String is", sampleStr)
  middleThree = sampleStr[middleIndex-1:middleIndex+2]
  print("Middle three chars are", middleThree)
  
getMiddleThreeChars("JhonDipPeta")
getMiddleThreeChars("Jasonay")

44.Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1.Given: s1 = "Ault" s2 = "Kelly"

def appendMiddle(s1, s2):
  middleIndex = int(len(s1) /2)
  print("Original Strings are", s1, s2)
  middleThree = s1[:middleIndex:]+ s2 +s1[middleIndex:]
  print("After appending new string in middle", middleThree)
  
appendMiddle("Ault", "Kelly")

45.Given a list of strings find the longest common prefix for them
Example: Input: ["flower","flow","flight"]
Output: "fl"

i=0
while(i<len(a)):
  if (a[i]==b[i]):
       print(a[i],end="")
       i+=1
  else:
     break
     
     46.Write a program to solve a classic ancient Chinese puzzle: We count 35 heads
and 94 legs among the chickens and rabbits in a farm. How many rabbits and
how many chickens do we have?
Hint: Use for loop to iterate all possible solutions.

ef animals(heads,legs):
  Ns = 'No solution'
  for i in range (heads+1):
    j=heads-i
    if (2*i)+(4*j)==legs:
      return i,j
  return Ns

heads = 35
legs = 95
X= animals(heads,legs)
print(X)

47. Find the total factors for a given integer N.
Ex: 24 has 1, 2, 3, 4, 6, 8, 12, 24 total 8 factors. So if the input is 24 output
should be 8

 p = 2; 
    while((p * p) < n): 
        if (hh[p] == 1): 
            for i in range((p * 2), n, p): 
                hh[i] = 0; 
        p += 1; 
  
    # Traversing through  
    # all prime numbers 
    total = 1; 
    for p in range(2, n + 1): 
        if (hh[p] == 1): 
          # power in factorization 
            count = 0; 
            if (n % p == 0): 
                while (n % p == 0): 
                    n = int(n / p); 
                    count += 1; 
                total *= (count + 1); 
                  
    return total;
    
    48.Give a list of tickets for candidates, find out who is the winner
Ex: [‘a’, ‘b’, ‘a’, ‘c’, ‘a’] Here there are total 3 candidates contesting ‘a’, ‘b’ and ‘c’.
And winner is ‘a’ as he got the highest votes

from collections import Counter  
  
votes =['john','johnny','jackie','johnny','john','jackie', 
    'jamie','jamie','john','johnny','jamie','johnny','john']  
  

vote_count=Counter(votes) 
  
#Find the maximum number of votes 
max_votes=max(vote_count.values()) 
  
#Search for people having maximum votes and store in a list 
lst=[i for i in vote_count.keys() if vote_count[i]==max_votes]

49.Find the sub-string exists in the string  without using in operator 

test_str = "aliyasiddiki"
  
# using str.index() to test 
# for substring 
try :  
    res = test_str.index("sid") 
    print ("sid exists in GeeksforGeeks") 
except : 
    print ("sid does not exists in GeeksforGeeks") 
    
    50.Given a string containing just the characters '(', ')', '{', '}', '['and ']', determine if the
input string is valid.
Examples:
Input: "()" Output: Valid
Input: "()[]{}" Output: Valid
Input: "([)]" Output: Not Valid

est_list1 = [1, 5, 6, 9, 11] 
test_list2 = [3, 4, 7, 8, 10] 
  
# printing original lists  
print ("The original list 1 is : " + str(test_list1)) 
print ("The original list 2 is : " + str(test_list2)) 
  
# using sorted() 
# to combine two sorted lists 
res = sorted(test_list1 + test_list2) 
  
# printing result 
print ("The combined sorted list is : " + str(res)) 

51.Run below code that will generate a matix as an input and print all the even numbers in it import random    :                                                                                                                                                                              mat= [[random .randint(1,10) for i in range (4)] for row in range(4)]                                                   print(mat)    

for i in range(3):
  for j in "ABC":
      print(i,j)
  print()
  
  52.Assume a fair dice roll using a similar random integer  generation code above roll for 500 times and print  the number of times 1 to 6 has appeared.
  
  import random

sample_size = int(input("Enter the number of times you want me to roll the die: "))

if (sample_size <=0):

    print("Please enter a positive number!")

else:
    counter1 = 0

    counter2 = 0

    final = 0

    while (counter1<= sample_size):

        dice_value = random.randint(1,6)

        if ((dice_value) == 6):
            counter1 += 1

        else:
            counter2 +=1

    final = (counter2)/(sample_size)  # fixing indention 


print("Estimation of the expected number of rolls before pigging out: " + str(final))

53.With a given integral number n, write a program to generate a dictionary that
contains (i, i*i) such that is an integral number between 1 and n (both included).
and then the program should print the dictionary.
Suppose the following input is supplied to the program: 8
Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

number = int(input("Type a number: "))

numberDict = {}
for i in range(1, number+1):
    numberDict[i] = i*i

print(numberDict)

54.Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?  Hint: Use for loop to iterate all possible solutions.

def animals(heads,legs):
  Ns = 'No solution'
  for i in range (heads+1):
    j=heads-i
    if (2*i)+(4*j)==legs:
      return i,j
  return Ns

heads = 35
legs = 95
X= animals(heads,legs)
print(X)

55.Find the total factors for a given integer N.   Ex: 24 has 1, 2, 3, 4, 6, 8, 12, 24 total 8 factors

ef divCount(n): 
  
    # sieve method for 
    # prime calculation 
    hh = [1] * (n + 1); 
      
    p = 2; 
    while((p * p) < n): 
        if (hh[p] == 1): 
            for i in range((p * 2), n, p): 
                hh[i] = 0; 
        p += 1; 
  
    # Traversing through  
    # all prime numbers 
    total = 1; 
    for p in range(2, n + 1): 
        if (hh[p] == 1): 
          # power in factorization 
            count = 0; 
            if (n % p == 0): 
                while (n % p == 0): 
                    n = int(n / p); 
                    count += 1; 
                total *= (count + 1); 
                  
    return total; 
  
# Driver Code 
n = 24; 
print(divCount(n));

56.With a given integral number n, write a program to generate a dictionary that [contains (i, i*i) such that is an integral number between 1 and n (both include and then the program should print the dictionary.Suppose the following input is supplied to the program: 8  . Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 6}

  
  umber = int(input("Type a number: "))

numberDict = {}
for i in range(1, number+1):
    numberDict[i] = i*i

print(numberDict)

57.alculate avg marks of the student Example: ##Note - some of the marks are None that is student did not appear for the exam and that should be excluded from average calculation
student ={'A': {'PHY': 88, 'CHEM': 71, 'MATH': 88},
'B': {'PHY': 52, 'CHEM': 99, 'MATH': 21},
'C': {'PHY': 56, 'CHEM': 59, 'MATH': 28},
'D': {'PHY': 15, 'CHEM': 61, 'MATH': 79},
'E': {'PHY': 18, 'CHEM': 61, 'MATH': 82},
'F': {'PHY': 41, 'CHEM': 70, 'MATH': 59},
'G': {'PHY': None, 'CHEM': 61, 'MATH': 54},
'H': {'PHY': 71, 'CHEM': None, 'MATH': 10},
'I': {'PHY': 65, 'CHEM': 9, 'MATH': 65},
'J': {'PHY': 69, 'CHEM': 39, 'MATH': 75},
'K': {'PHY': 92, 'CHEM': 11, 'MATH': None},
'L': {'PHY': None, 'CHEM': None, 'MATH': None}
}
##### Output
# Avg marks of student A 82.33333333333333
# Avg marks of student B 57.333333333333336
# Avg marks of student C 47.666666666666664
# Avg marks of student D 51.666666666666664
# Avg marks of student E 53.666666666666664
# Avg marks of student F 56.666666666666664
# Avg marks of student G 57.5
# Avg marks of student H 40.5
# Avg marks of student I 46.333333333333336
# Avg marks of student J 61.0
# Avg marks of student K 51.5
# Avg marks of student L 

for i,j in student.items():
  Avg =0
  total = 0
  for q in j.values():
    if (q is not None):
      total = total+q
  print("Marks secured by student", i , '=' ,total+q)
  [j].value_add()
  num_rows = details.shape[0] 
  print ("Dict key-value are : ") 
for q in student : 
    print(i, student[q]) 
    
58. Take two list of numbers and generate a list of tuples that are comobo of the n  such that two numbers in the pair are not equal .Use list comprehension.# Input: X=[1,2,3] ; Y=[1,2,3]            #Output :[(1,2) ,(1,,3) ,(2,1),(2,3),(3,1),(3,2)]

transposed=[]
matrix=[[1,2,3],[1,2,3]]
for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

59.Take two list of numbers of products quantities and prices and calculate total price.Use list comprehension and aggregartion . #Input: product_quantities = [13,5,6,10,11] ; prices = [1.2 , 6.5,1.0,4.8,5.0]   #output : Total = 157.1

product_quantities = [13,5,6,10,11]
prices = [1.2 , 6.5,1.0,4.8,5.0]
lst.append(prices)
print("Sum of elements in given list is :", sum(prices)) 

60.Run the code below to generate a matrix take an input character as target
print the row index and column index if the character is found Else print "Not found" .                           # Input:Enter Target character :h       ;        #Output: 2  4  ;   table = [list("abcd"), list("efgh"),list("ijkl")]

import random
mat= [[random .randint(1,10) for i in range (4)] for row in range(4)]
print(mat)
for i in range(3):
  for j in "ABC":
      print(i,j)
  print()
 
 61.Try explaining this with exception as well to write clean code. Will anyways be explaining that in the class. But atleast below code is expected from the students.
 
 ry:
  print(1)
  print(5/0)
  print(2)
except:
  print(3)
else:
  print(4)
finally:
  print(9)
  
  62.Fibonaci and Factorial through recursion.
  
  ef recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
 
nterms = 10
 
# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
       
       63.Discuss the exception when -ve numbers
       
       try:
  print(1)
  print(-4)
  print(2)
except:
  print(3)
else:
  print(4)
finally:
  print(9)
  
  64.Take a sorted list A and key to search
  
  x = [2, 8, 1, 4, 6, 3, 7]  
  
print ("Sorted List returned :"),  
print (sorted(x))  
  
print ("\nReverse sort :"),  
print (sorted(x, reverse = True)) 
  
print ("\nOriginal list not modified :"),  
print (x)  

66.Create an add function that is agnostic to number of inputs Example: My_Custom_Add (1, 2, 3, 4, 5)
 
def add(*args):
     print(sum(args))
    
add(5,5,6)



67. Implement Binary search by using recursion .

def binary(a, fir, las, term):

    mid=int((fir+las)/2)

    if term>a[mid]:

        binary(a, mid, las, term)

    def elif term<a[mid]:

        binary(a,fir, mid, term)

  def  elif term==a[mid]:

        print("Number found at", mid+1)

    else:

        print("Number is not there in the array")

b=[1,2,3,4,5]

fir=0

las=len(b)

term=4

binary(b,fir,las,term)

68.Write a function to check if input number is a prime?

num = 11
  
# If given number is greater than 1 
if num > 1: 
      
   # Iterate from 2 to n / 2  
   for i in range(2, num): 
         
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number") 
   
   69.One file will be shared : You will need to read the files and solve following problems:- 1.)Find  all the words which contains 'uu' in the file .
   
   fopen=open("/content/drive/My Drive/AIP batch 1/scrabble/sowpods.txt")
words= fopen.readlines()
#words [:20]
for word in words:
  if "UU" in word:
    print(word.strip())
fopen .close()    

70.Print all alphabets that never appear double in sequence (back  to back) in the words in the files.

import string
fopen = open("/content/drive/My Drive/AIP batch 1/scrabble/sowpods.txt")

#words [:20]
words=[word.strip()for word in words]
for alpha in string.ascii_uppercase:
  flag=True
  if alpha*2 in words:
    flag = False
  if (flag):
      print(alpha)
fopen.close()

71.Print words in the file contains all the vowels 

sowp_obj =open("/content/drive/My Drive/AIP batch 1/sowpods.txt")
sowp_words= sowp_obj.readlines()
for word in sowp_words:
  flag = True
  for alpha in "AEIOU":
    if  alpha not in word:
      flag = False

  if(flag==True):
    print(word)

sowp_obj.close()

75.)Print all palindrome words in the file.

import string
fopen =open("/content/drive/My Drive/AIP batch 1/sowpods.txt")
words= fopen.readlines()
words=[word.strip() for word in words]
fopen.close()
for word in words:
    revstr=(word[::-1])
    if revstr==word:
      print(word)
      
fopen.close()

       import string
fopen =open("/content/drive/My Drive/AIP batch 1/sowpods.txt")
words= fopen.readlines()
words=[word.strip() for word in words]
fopen.close()
for word in words:
    revstr=(word[::-1])
    if revstr==word:
      print(word)
      
fopen.close()

76.Join two sorted lists such that the final list is also  sorted 

n1= int(input("Enter number of elements: ")) 
b1= []
for i in range(n1): 
  e=int(input("Enter the numbers: ")) 
  b1.append(e) 
b1.sort() 
print(b1)

n2= int(input("Enter number of elements: ")) 
b2= []
for i in range(n2): 
  e=int(input("Enter the numbers: ")) 
  b2.append(e) 
b2.sort() 
print(b2)

b3= []
for num in b1 :
    b3.append(num)
for num in b2:
    b3.append(num) 
b3.sort() 
print(b3)

     


  
                           




 
  

    
    
    


        
        
        

  

      


   
   

 
 

 