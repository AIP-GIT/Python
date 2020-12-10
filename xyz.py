#que1.Give a list of weight and value pairs  for items and a bag with capacity.Calculate the maximum item value that can be carried in the bag . 
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


#que2.Take two list of numbers of products quantities and prices and calculate total price.Use list comprehension and aggregartion .
#Input: product_quantities = [13,5,6,10,11] ; 
#prices = [1.2 , 6.5,1.0,4.8,5.0]  
#output : Total = 157.1
product_quantities = [13,5,6,10,11]
prices = [1.2 , 6.5,1.0,4.8,5.0]
p=sum([a*b for a,b  in zip(product_quantities,prices)])
print(p)

#que3.Write a program to compute simple interest.
p=int(input("Enter any number for p:"))
r=int(input("Enter any number for r:"))
t=int(input("Enter any number for t:"))
SI=(p*r*t)/100
print(SI)


#que4.write a program to find GCD of two numbers
num1=int(input("enter any num1:"))
num2=int(input("enter any num2:"))
for i in range(1,num2+1):
  if(num1%i==0 and num2%i==0):
    GCD=i
print(GCD)


#que5.Program for maximum of 3 numbers
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


#que6.You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. The numbers are in the range of 1 to 6,
 like any ordinary dice. Input a dice face number, and output the opposite face number.
 i=0
while (i>1) or (i<6):
  i=int(input("Enter any number="))
  num=7-i
print(num)


#que7.Find the average of numbers in a list
def average(num):
    sum= 0
    for t in num:
        sum= sum + t           

    avg = sum/ len(num)
    return avg

print("The average is", average([18,25,3,41,5]))


#que8.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included)
for i in range(1500, 2701):
    if (i%7==0) and (i%5==0):
        nl.append(str(x))
print (','.join(nl))


#que9.Perform operations on complex type values.(ie … 10+1.5j)
import cmath
a=10+1.5j
cmath.polar(a)

#que10.Program for minimum of 3 numbers.
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

#que11.Find sum of digits in a number
a=int(input("Enter any number:"))
b=int(input("Enter any number:"))
sum=a+b
print("sum of digits:",sum)

#que12.Find if a list is sorted in increasing order
numlist=[]
num=int(input("Enter the total number of list:"))
for i in range(1,num+1):
  value=int(input("Enter the value of %d element:" %i))
  numlist.append(value)




#que13.Write a program which accepts the radius of circle from the user and compute the area.
r=int(input("enter the radius r: "))
pie=3.14
area=2*pie*r
print("area of circle:",area)

#que15.Python program to find the squareroot.
a=int(input("Enter value of a:"))
sq=a*a
print("square root:",sq)

#que16.Python program to swap two variables.
x = 10
y = 50
temp = x 
x = y 
y = temp  
print("Value of x:", x) 
print("Value of y:", y)


#que17.Python program to check whether the number is positive , negative or 0.
number = int(input("Enter number: "))
if number < 0:
   print("The entered number is negative.") 
elif number > 0:
    print("The entered number is positive.")
elif number == 0:
    print("Number is zero.")
else:
    print("The input is not a number")
    
    
#que18.Give a two integer number and return their product and if the product is greater than 1000,then return their sum.  
def Char(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )
inputStr = input("Enter String ")
print("Orginal String is ", inputStr)
print("Printing only even index chars")
Char(inputStr) 
   

#que19.Given a range of first 10 numbers,Iterate from start number to the end number and print the sum of the current number and previous number.
previous_num = 0
for i in range(10):
    sum = previous_num + i
    print(f'Current number {i} Previous Number {previous_num} is {sum}')
    previous_num = i

#que20.Given a string,display only those characters which are present at an even index number.
def Char(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )

inputStr = "cherima" 
print("Orginal String is: ", inputStr)

print("even index chars:-")
Char(inputStr)

#que21.Given a string and an integer number n , remove character from a string from zero up to n and return  a new string.
def removeChars(str, n):
  return str[n:]

print("Removing n number of chars")
print(removeChars("pynative", 4))

#que22.Given a list of numbers, return true if first and last number of a list is same .
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

#gue23.Given  a list of numbers, Iterate it and print only those numbers which are divisible of 5.
lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
n=int(input("Enter the number to be divided by:"))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)
        
#que24.Return the total count of sub-string "Emma" appears in the appears in the given string.               
#Given string is"Emma is good developer .Emma is a writer."        
sampleStr = "Emma is good developer. Emma is a writer"
cnt = sampleStr.count("Emma")
print(cnt)

#que25.Print the following pattern:  
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
    
#que26.Reverse a given number and return true if it is the same as the original number.
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
  
#que27.Given a two list of numbers create a new  list such that new list should contain only odd numbers from the first list and even 
numbers from the second list.  
from numpy import array
a=array([1,2,3,4,5,6]) 
b=array([7,8,9,10,11,12]) 

c = [*a[a%2 == 0], *b[b%2 != 0]]
print(c)

#que28.Write a code to extract each digit from an integer, in the reverse order.
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


#que29.Write a program to compute simple interest.
p=int(input("Enter any number for p:"))
r=int(input("Enter any number for r:"))
t=int(input("Enter any number for t:"))
SI=(p*r*t)/100
print(SI)


#que30.write a program to find GCD of two numbers
num1=int(input("enter any num1:"))
num2=int(input("enter any num2:"))
for i in range(1,num2+1):
  if(num1%i==0 and num2%i==0):
    GCD=i
print(GCD)


#que31.Program for maximum of 3 numbers
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


#que32.Python program to check leap year 
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
else:
    print(year, "is not a Leap Year")
    
#que33.Python program to check odd or even .
a=int(input("enter any number:"))
if a%2==0:
  print("it is even number")
else:
  print("it is odd number")  
  
#que34.Find the maximum element in the list without using max function
def minmax1 (x):
    minimum = maximum = x[0]
    for i in x[1:]:
        if i < minimum: 
            minimum = i 
        else: 
            if i > maximum:
              maximum = i
    return (minimum,maximum)

print(minmax1([9,8,7,6,5,4,3,2,1,11,12,13,14,15,16,17,18,19]))


#que35.Find if the substring exists in the string without using in operator  
str="cherima momin is a student of Engineering discipline."
sub1="cherima"
sub2="Engineering"
 
print(str.find(sub1)) 
 
print(str.find(sub2))

#que36.Take an integral number N as an input and calculate the sum of first N natural numbers.  
num = int(input("Enter the value of n: "))
hold = num
sum = 0

if num <= 0: 
   print("Enter a whole positive number!") 
else: 
   while num > 0:
        sum = sum + num
        num = num - 1;
print("Sum of first", hold, "natural numbers is: ", sum)

#gue 37.Write a program which can generate and print a list and tuple where the value are square of numbers between 1 and 20(both included).
def printValues():
        l = list()
        for i in range(1,20):
                l.append(i**2)
        print(l)
printValues()
                
#que38.Write a program that accepts a sentence and calculate the number of letters and digits.
#Example: Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3  
phrase = input("Type in: ")
phrase = list(phrase)

l, d = 0, 0
for i in phrase:
    if i.isalpha():
        l = l + 1
    if i.isdigit():
        d = d + 1
    else:
        pass

print("Letters:", l)
print("Digits:", d)

#que39.Write a program that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the program should print both the strings line by line.
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
      print ("Larger string is:")
      print (string1)


#que40.Check for Palindrome in a string without using loop statement.
def isPalindrome(s):
    return s == s[::-1]
 
 s = "mikkim"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
   
#que41.Sort an unsorted array in increasing order without using sort function
#Example: If the input is [2, 5, 1, 6, 4] output should be [1, 2, 4, 5, 6]   
sorted([2, 5, 1, 6, 4])

#que42.Write a program to find Leap year
year = int(input("Enter Year: "))
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
else:
    print(year, "is not a Leap Year")
    
    
#que43.Input a comma separated list from console. Write a program to print this list afterremoving all duplicate values with 
#original order reserved in python 
def Repeat(x): 
    size = len(x) 
    repeated = [] 
    for i in range(size): 
        k = i + 1
        for j in range(k, size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated  
list1 = [10, 20, 30, 20, 20, 30, 40,  
         50, -20, 60, 60, -20, -20] 
print (Repeat(list1)) 


#que44.Write a program to find palindromic numbers between 2 numbers
#Hint: Palindromic number between 10 to 50 are 11, 22, 33, 44
def isPalindrome(n: int) -> bool: 
    rev = 0
    i = n 
    while i > 0: 
        rev = rev * 10 + i % 10
        i //= 10
    return (n == rev) 
def countPal(minn: int, maxx: int) -> None: 
    for i in range(minn, maxx + 1): 
        if isPalindrome(i): 
            print(i, end = " ") 
if __name__ == "__main__": 
    countPal(10, 50) 
    
#que45.What is the output of tuple [1:3] if tuple =('abcd', 786,2.23,"john",70.2)?                                             
#('abcd' , 786,2.23,"john",70.2) abcd(786,2.23) , None of the above     
(786,2.23)

#que46.Given a list A and a number n, find the n’th largest number.
Example: If the input list is [5, 2, 1, 7, 4] and n is 3. The 3rd largest number is 4
def Nmaxelements(list1, N): 
    final_list = [] 
  
    for i in range(0, N):  
        max1 = 0
          
        for j in range(len(list1)):      
            if list1[j] > max1: 
                max1 = list1[j]; 
                  
        list1.remove(max1); 
        final_list.append(max1) 
          
    print(final_list) 
list1 = [5,2,1,7,4] 
N = 3
Nmaxelements(list1, N)


#que47.Accept number from user and calculate the sum of 
#all number between 1 and given number
def sumOfDigits(x) : 
    sum = 0
    while (x != 0) : 
        sum = sum + x % 10
        x   = x // 10
      
    return sum 
n = 50
print("Sum of digits in numbers from 1 to", n, "is", sumOfDigitsfrom1toN(n)) 


#que48.Print multiplication table of given number 
num = int(input("Enter the number: "))

print("Multiplication Table of", num)
for i in range(1, 11):
   print(num,"X",i,"=",num * i)

#que49.Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for item in list1:
    if (item > 150):
        break
    if(item % 5 == 0):
        print(item)

#que50.Print  the words that are  in sonnet_words.txt but not in sowpods.txt
import time
fopen =open(r"drive/My Drive/abcde/scrabble/sowpods.txt")
words=fopen.readlines()
fopen_son=open(r"drive/My Drive/abcde/scrabble/sonnet_words.txt")

words_cln=fopen_son.readlines()
                                                              
words={word.strip() for word in words}
words_cln=[word.strip() for word in words_cln]

tic=time.time()
for word in words_cln:
  if word not in words:
   print(word)
print(time.time()-tic)


#que51.Given a string of odd length greater 7, return a string made of the middle three chars of 
#a given String. Given: str1 = "JhonDipPeta"     str2 = "JaSonAy"        
def getMiddleThreeChars(sampleStr):
  middleIndex = int(len(sampleStr) /2)
  print("Original String is:", sampleStr)
  middleThree = sampleStr[middleIndex-1:middleIndex+2]
  print("Middle three chars are:", middleThree)
  
getMiddleThreeChars("JhonDipPeta")
getMiddleThreeChars("Jasonay")


#que52.Given 2 strings, s1 and s2, create a new string by appending s2 
in the middle of s1.Given   :   s1 = "Ault" s2 = "Kelly" 
def appendMiddle(s1, s2):
  middleIndex = int(len(s1) /2)
  print("Original Strings are", s1, s2)
  middleThree = s1[:middleIndex:]+ s2 +s1[middleIndex:]
  print("After appending new string in middle", middleThree)

#que53.Given 2 strings, s1, and s2 return a new string made of the first, 
#middle and last char each input string  . Given:     s1 = "America"s2 = "Japan"
def mix_string(s1, s2):
    first_char = s1[:1] + s2[:1]
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
    res = first_char + middle_char + last_char
    print("Mix String is ", res)

s1 = "America"
s2 = "Japan"
mix_string(s1, s2)


#que54.Write a program to solve a classic ancient Chinese puzzle: We count 35 heads
#3and 94 legs among the chickens and rabbits in a farm. How many rabbits and
#how many chickens do we have?
#Hint: Use for loop to iterate all possible solutions.
def solve(numheads,numlegs):

    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if (2*i)+(4*j)==numlegs:
            return i,j
    return ns,ns


numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print (solutions)

#que55.Find the total factors for a given integer N.
#Ex: 24 has 1, 2, 3, 4, 6, 8, 12, 24 total 8 factors. So if the input is 24 output
#should be 8

def divCount(n): 
    hh = [1] * (n + 1); 
      
    p = 2; 
    while((p * p) < n): 
        if (hh[p] == 1): 
            for i in range((p * 2), n, p): 
                hh[i] = 0; 
        p += 1; 
    total = 1; 
    for p in range(2, n + 1): 
        if (hh[p] == 1): 
            count = 0; 
            if (n % p == 0): 
                while (n % p == 0): 
                    n = int(n / p); 
                    count += 1; 
                total *= (count + 1); 
                  
    return total; 
n = 24; 
print(divCount(n));


#que56.Check if a given input number is a perfect square
#Ex: 16 is a perfect square 4 * 4 , while 15 is not
def is_perfect_square(n):
    x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y: return False
        y.add(x)
    return True

print(is_perfect_square(15))
print(is_perfect_square(16))


#que57.Find if a number is present in a list
values = input("Input some comma seprated numbers : ")
list = values.split(",")
print('List : ',list)


#que58.Give a list of tickets for candidates, find out who is the winner
#Ex: [‘a’, ‘b’, ‘a’, ‘c’, ‘a’] Here there are total 3 candidates contesting ‘a’, ‘b’ and ‘c’.
#And winner is ‘a’ as he got the highest votes
from collections import Counter 
votes =['a','b','a','c','a']
vote_count=Counter(votes)
max_votes=max(vote_count.values()) 
lst=[i for i in vote_count.keys() if vote_count[i]==max_votes]
print(sorted(lst)[0]) 


#gue59.Find the sub-string exists in the string  without using in operator 
s=input('Enter string: ')
s1=input('Enter substring: ')
if (s.find(s1)!=-1):
  print(s1)
  
  
#que60.Find if a string is palindrome. Hint: use reverse function [::-1]
def isPalindrome(s):
    return s == s[::-1]
s = "malayalam"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")

#que61.Given a string containing just the characters '(', ')', '{', '}', '['and ']', determine if the
input string is valid.
Examples:
Input: "()" Output: Valid
Input: "()[]{}" Output: Valid
Input: "([)]" Output: Not Valid


#62.Given a string containing just the characters '(', ')', '{', '}', '['and ']', determine if the
#input string is valid.
#Examples:
#Input: "()" Output: Valid
#Input: "()[]{}" Output: Valid
#Input: "([)]" Output: Not Valid
class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))    
  

#que63.Merge two sorted input list to generate a single sorted list
#If the input is [2, 5, 8] and [1, 3, 7]
#Output should be [1, 2, 3, 5, 7, 8]
from heapq import merge 
  
def mergeArray(arr1,arr2): 
    return list(merge(arr1, arr2)) 
  
# Driver function 
if __name__ == "__main__":
  arr1 = [2,5,8]   
  arr2 = [1,3,7] 
print(mergeArray(arr1, arr2)) 

#que64.Run below code that will generate a matix as an input and print all the even numbers in it import random    :                                                                                                                                                                              
#mat= [[random .randint(1,10) for i in range (4)] for row in range(4)] print(mat) 
import random
mat= [[random .randint(1,10) for i in range (4)] for row in range(4)]  
print(mat)

#que65.Assume a fair dice roll using a similar random integer  generation code above roll for 500 times and print  
#the number of times 1 to 6 has appeared. 
import random

while True:
  sample_size = int(input("Enter the number of times:"))
  if sample_size > 0:
    break

roll_with_6 = 0
roll_count = 0

while roll_count < sample_size:
  roll_count += 1
  n = random.randint(1, 6)
  #print(n)
  if n == 6:
    roll_with_6 += 1

print(f'Probability to get a 6 is = {roll_with_6/roll_count}')


#que66.Using Dictionary, write a program that accepts a sentence and calculate the
#number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3  
s = input("Input a string: ")
d=l=0
for c in s:
  if c.isdigit():
     d=d+1
  elif c.isalpha():
      l=l+1
print("Letters:", l)
print("Digits:", d)


#que67.With a given integral number n, write a program to generate a dictionary that
#contains (i, i*i) such that is an integral number between 1 and n (both included).
#and then the program should print the dictionary.
#Suppose the following input is supplied to the program: 8
#Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
n = int(input("Enter the value of n: "))
squares = {i : i*i for i in range(1, n+1)}
print(squares)


#que68Find the total factors for a given integer N.   Ex: 24 has 1, 2, 3, 4, 6, 8, 12, 24 total 8 factors
def divCount(n): 
    hh = [1] * (n + 1); 
      
    p = 2; 
    while((p * p) < n): 
        if (hh[p] == 1): 
            for i in range((p * 2), n, p): 
                hh[i] = 0; 
        p += 1; 
    total = 1; 
    for p in range(2, n + 1): 
        if (hh[p] == 1): 
            count = 0; 
            if (n % p == 0): 
                while (n % p == 0): 
                    n = int(n / p); 
                    count += 1; 
                total *= (count + 1); 
                  
    return total; 
n = 24; 
print(divCount(n));


#que69With a given integral number n, write a program to generate a dictionary that [contains (i, i*i) such that 
#is an integral number between 1 and n (both include and then the program should print the dictionary.Suppose the 
#following input is supplied to the program: 8  . Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 6}
n=int(input("Enter a number:"))
for x in range(1,n+1):
 d={i:i*i }
 print(d)
 
 
#que70.Calculate avg marks of the student Example: ##Note - some of the marks are None that is student did not appear for the exam and that should be excluded from average calculation
#student ={'A': {'PHY': 88, 'CHEM': 71, 'MATH': 88},
#'B': {'PHY': 52, 'CHEM': 99, 'MATH': 21},
#'C': {'PHY': 56, 'CHEM': 59, 'MATH': 28},
#'D': {'PHY': 15, 'CHEM': 61, 'MATH': 79},
#'E': {'PHY': 18, 'CHEM': 61, 'MATH': 82},
#'F': {'PHY': 41, 'CHEM': 70, 'MATH': 59},                                
#'G': {'PHY': None, 'CHEM': 61, 'MATH': 54},
#'H': {'PHY': 71, 'CHEM': None, 'MATH': 10},
#'I': {'PHY': 65, 'CHEM': 9, 'MATH': 65},                                                        
#'J': {'PHY': 69, 'CHEM': 39, 'MATH': 75},
#'K': {'PHY': 92, 'CHEM': 11, 'MATH': None},
#'L': {'PHY': None, 'CHEM': None, 'MATH': None}
#}
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
# Avg marks of student L 0 

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
PHY=0
CHEM=0
MATH=0
PHY_APPEARED=0
CHEM_APPEARED=0
MATH_APPEARED=0
for j in student.values():
  if (j['PHY'] is not None):
    PHY=PHY+j['PHY']
    PHY_APPEARED=PHY_APPEARED+1
  if (j['CHEM'] is not None):
    CHEM=CHEM+j['CHEM']
    CHEM_APPEARED=CHEM_APPEARED+1
  if (j['MATH'] is not None):
    MATH=MATH+j['MATH']
    MATH_APPEARED=MATH_APPEARED+1
P=PHY/PHY_APPEARED
C=CHEM/CHEM_APPEARED
M=MATH/MATH_APPEARED

print('PHY MARKS',P)
print('CHEM MARKS',C)
print('MATH MARKS',M)


#que71.# Assume a fair dice roll using a similar random integer generation code above roll for 500 times and print the number 
#of times 1 to 6 has appeared.
import random
 
test_data = [0, 0, 0, 0, 0, 0] 
n = 1000 
 
for i in range(n):
  result = random.randint(1, 6)
  test_data[result - 1] = test_data[result - 1] + 1
 
for i in range(0, 6):
  print ("Number of ", i+1, "'s: ", test_data[i])
  
#que72.# Take two list of numbers and generate a list of tuples that are comobo of the n  such that two numbers in the pair are not equal .
#Use list comprehension.# Input: X=[1,2,3] ; Y=[1,2,3]            #Output :[(1,2) ,(1,,3) ,(2,1),(2,3),(3,1),(3,2)]
X=[1,2,3]
Y=[1,2,3] 
output = [[a, b] for a in X 
          for b in Y if a != b]
print(output)   


#que73.Take a sentence and output a dictionary [Mark-2] with word as the key and number of characters in the word as value. 
#Use dictionary comprehension.
def Count(my_list):  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
  
    for key, value in freq.items(): 
        print ("% d : % d"%(key, value)) 
if __name__ == "__main__":  
    my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2] 
  
    Count(my_list) 
    
    
#que74.Fibonaci and Factorial through recursion.
fibo_series = [0, 1]

def fibonacci(n):
        if n<=len(fibo_series) and n>0:
                return fibo_series[n-1]
        else:
                fn = fibonacci(n-1) + fibonacci(n-2)
                if n>len(fibo_series):
                        fibo_series.append(fn)
                return fn

n = int(input('Enter a number, N, N>=2 : '))

fibonacci(n)

print(fibo_series)

#que75.Take a sorted list A and key to search
x = [2, 8, 1, 4, 6, 3, 7]  
  
print ("Sorted List returned :"),  
print (sorted(x))  
  
print ("\nReverse sort :"),  
print (sorted(x, reverse = True))

#que76.Given a list of products, print out the name of all the products with a price higher than 10 Hint: Use Dictionary products = [ 
#{'name': 'orange', 'price': 20}, 
#{'name': 'apple', 'price': 8}, 
#{'name': 'banana', 'price': 10}, 
#{'name': 'kiwi', 'price': 30} 
#]
 products=[{'name': 'orange', 'price': 20},
{'name': 'apple', 'price': 8},
{'name': 'banana', 'price': 10},
{'name': 'kiwi', 'price': 30}
]
for i in products:
  if (i['price']>10):
    print(i['name'])

#que77.Write a program to take integral numbers and calculate the factorial. 
# If factorial is not defined return -1 
# ================== 
# Main program and output format 
# print (My_factorial(-1)) 
# print (My_factorial(0)) 
# print (My_factorial(1)) 
# print (My_factorial(5)) 
#==================== 
# -1 
# 1 
# 1 
# 120

def My_factorial(num):
 factorial=1
 if num < 0:
   return -1
 elif num == 0:
   return 1
 else:
   for i in range(1,num + 1):
       factorial = factorial*i
   return factorial

print (My_factorial(-1)) 
print(My_factorial(0))
print (My_factorial(1)) 
print (My_factorial(5))


#que78.Implement Binary search by using recursion .
def binary(a, fir, las, term):

    mid=int((fir+las)/2)

    if term>a[mid]:

        binary(a, mid, las, term)

    elif term<a[mid]:

        binary(a,fir, mid, term)

    elif term==a[mid]:

        print("Number found at", mid+1)

    else:

        print("Number is not there in the array")

b=[1,2,3,4,5]

fir=0

las=len(b)

term=4

binary(b,fir,las,term)



#que79.Write a function to check if input number is a prime?
num = 11 
if num > 1: 
   for i in range(2, num): 
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number")


#que80.One file will be shared : You will need to read the files and solve following problems:-                                            
#1.)Find  all the words which contains 'uu' in the file .   
fopen =open(r"drive/My Drive/abcde/scrabble/sowpods.txt")
words=fopen.readlines()
for word in words:
 if "UU" in word:
  print(word.strip())
fopen.close()
  