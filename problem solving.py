#create a function that takes two numbers as arguments and returns their sum
'''def add_numbers(a,b):
    return a+b 
print(add_numbers(5,7))'''

'''def add_numbers(a, b):
    
    if b > 0:
        for i in range(b):
            a += 1 
    elif b < 0:
        for i in range(-b):
            a -= 1  
            
    return a

print(add_numbers(9,-6))'''

#Write a function that takes an integer minutes and converts it to seconds.
'''def minutes_to_seconds(minutes):
  return minutes*60
minutes=int(input("enter a number of minutes:"))
seconds=minutes_to_seconds(minutes)
print(minutes_to_seconds(minutes))'''

#Create a function that takes a number as an argument, increments the number by +1 and returns the result.
'''def increment(num):
   return num+1
num=int(input("enter a number:"))
print(increment(num))'''

'''def incremented(number):
 return number+1
number=int(input("enter a number"))
print(incremented(number))'''

#Create a function that takes the age in years and returns the age in days.
'''def age_in_days(years):
   leap_years=years//4
   non_leap_years=years-leap_years
   total_days=(leap_years *366)+(non_leap_years *365)
   return total_days
print(age_in_days(25)) '''

'''age_in_years=30
age_in_days=(age_in_years *365)+(age_in_years //4)
print(age_in_days)'''

#sbi Create a function that takes voltage and current and returns the calculated power.
'''def calculate_power(voltage,current):
    print(voltage*current)
voltage=int(input("enter the voltage value:"))
current=int(input("enter the current value:"))
calculate_power(voltage,current)'''

'''voltage=int(input("enter voltage:"))
current=int(input("enter current:"))
power=voltage*current
print("power:",power)'''

# Write a function that returns the string "something" joined with a space " " and the given argument a.
'''def join_with_something(a):
  return "something " +str(a)
print(join_with_something("new"))'''

'''def add_something(a):
  return"anurag"+" "+"engineering"+" "+ a
a=input("enter a word:")
print(add_something(a))'''

#Create a function that takes two arguments. Both arguments are integers, a and b. Return true if one of them is 10 or if their sum is 10
'''def check_ten (a,b):
    return a==10 or b==10 or (a+b)==10 
print(check_ten(3 , 5))'''

#Create a function that takes two strings as arguments and returns either true or false depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.def eql_length(str1,str2):


'''def length(s1,s2):
  count1=0
  count2=0
  for i in s1:
    count1+=1
  for i in s2:
    count2+=1
  return count1==count2
s1=input("enter firsr string:")
s2=input("enter second string:")
print(length(s1,s2))'''


#Create a function that takes a name and returns a greeting in the form of a string. Don't use a normal function, use an arrow function.
'''greeting=lambda name:f"hello {name}!"
print(greeting("anusha"))'''
 
#Create a function that takes an array of 10 numbers (between 0 and 9) and returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555).
'''def format_phone_number(numbers):
  if len(numbers) !=10:
    raise ValueError("Input list must contain  exactly 10 numbers")
  if not all(0 <= num <= 9 for num in numbers):
    raise ValueError("All numbres must be  between 0 t0 9 ")
  phone_number = f"({numbers[0]}{numbers[1]}{numbers[2]}){numbers[3]}{numbers[4]}{numbers[5]}{numbers[6]}{numbers[7]}{numbers[8]}{numbers[9]}"
  return phone_number
numbers=[1,2,3,4,5,6,7,8,9,5]
print(format_phone_number(numbers))'''


'''def create_phone_number(numbers):
  if len(numbers)!=10:
    return "invalid input"
  phone_number= "("+ numbers [0] + numbers [1] + numbers [2] +") "+ numbers [3] + numbers [4] + numbers [5] + "_" + numbers [6] + numbers [7] + numbers [8] + numbers [9]  
  return phone_number
numbers=["5","5","5","5","5","5","5","5","5","5"]
print(create_phone_number(numbers))'''

#Create a function that returns an array of strings sorted by length in ascending order.
'''def sorted_list(lst):
   return sorted(lst, key=len)
print(sorted_list(["bb","cccc","u"])'''


'''def sort_by_length(arr):
   n=len(arr)
   for i in range(n):
     for j in range(0,n-i-1):
        if len(arr[j])>len(arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j] 
   return arr
string=["aaa","a","aa"]
print(sort_by_length(string))'''  



#Create a function that takes an array of arrays with numbers. Return a new (single) array with the largest numbers of each.
'''def largest_numbers(arrays):
  return [max(array) for array in arrays]
print(largest_numbers([[12,3,4],[1,2,3]]))'''

#Create a function that takes an array of numbers and returns the second largest number.
'''def second_largest(arr):
  if len(arr)<2:
    return None
  first=-float('inf')
  second=-float('inf')
  for num in arr:
    if num>first:
        second=first
        first=num
    elif num>second and num<first:
      second=num
  return second if second !=-float('inf') else None
print(second_largest([1,5,8,19]))'''
#Create a function that takes an array of items, removes all duplicate items and returns a new array in the same sequential order as the old array (minus duplicates).
'''def remove_dup(arr):
    new_array=[]
    for i in range(len(arr)):
       if arr[i] not in new_array:
         new_array.append(arr[i])
    return new_array
arr=[1,2,1,3,2,3,4]
print(remove_dup(arr))'''


#Create a function that takes an array of integers as an argument and returns a unique number from that array. All numbers except unique ones have the same number of occurrences in the array.
'''def unique_number(arr):
    for num in arr:
        count=0
        for other in arr:
           if num==other:  
             count+=1
        if count==1:
           return num  
numbers=[1,2,1,3,2,2,1]
print(unique_number(numbers))'''

#Create a function that takes two strings as arguments and returns the number of times the first string (the single character) is found in the second string.
'''def count_character(char,text):
  if len(char)!=1:
    raise valueError("first argument must must be asingle character ")
  count=0
  for c in text:
    if c==char:
      count+=1
  return count
result=count_character('n','bananaa')
print(result) '''

#Create a function that takes a string and returns the number (count) of vowels contained within it.
'''def count_of_vowels(s):
  vowels={"a","e","i","o","u","A","E","I","O","U"}
  count=0
  for char in s:
     if char in vowels:
         count+=1
  return count
print(count_of_vowels("welioee")) '''


#Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa.
'''def vice_versa(s):
   result=" "
   for char in s:
       if 'a'<=char<='z':
        result+=chr(ord(char)-32)
       elif 'A' <=char<='Z':
         result+=chr(ord(char)+32)
       else:
          result+=char
   return result
print(vice_versa("AnUShA"))'''
  

#Take one integer n, loop till n and pass each value to a function, create a function that takes one integer parameter, and multiply with 2 in every integer.
'''def multiply_by_two(num):
  return num*2
n=int(input("Enter a number:"))
for i in range(1,n+1):
  result=multiply_by_two(i)
  print(f"{i}*2={result}")'''

#Create Function that will take one parameter and return type of the data.
			
'''def type_of_data(value):
  if value is None:
    return"NoneType"
  if value is True or value is False:
      return "bool"
  if isinstance(value,int):
        return"int"
  
  if isinstance(value,str):  
        return "str" 
  if isinstance(value,dict):  
        return "dict"    

print(type_of_data(1)) 
print(type_of_data("Hello"))
print(type_of_data({1:"anu"}))'''

#21. Program to find greatest of three numbers(using ternary operator).
'''a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
largest=(a if a>b else b) if ((a if a>b else b)>c)else c
print("the greatest number is:",largest)'''  

 #C Program to find factorial of number.
		
'''num=int(input("enter a number:"))
fact=1
if num<1:
  print("factorial is not defined for negative numbers.")
elif num==0 or num==1:  
  print("factorial=",fact)
else:
    for i in range(1,num+1):
       fact*=i
    print("factorial=",fact)'''   

#23. C Program to arrange numbers in ascending order
'''def ascending_order(arr):
  n=len(arr)
  for i in range(n-1):
        for j in range(n-i-1):
          if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
n=int(input("enter the number of elements:"))
arr=[]
print(f"enter {n} numbers:")
for i in range(n):
  num=int(input())
  arr.append(num)
ascending_order(arr)
print("numbers in ascending order:")
for num in arr:
  print(num,end=" ")'''

'''arr=[3,4,2,6,7] 
n=len(arr)
for i in range(n-1):
   for j in range(n-i-1):
     if arr[j]>arr[j+1]:
       temp=arr[j]
       arr[j]=arr[j+1]
       arr[j+1]=temp
print("sorted array:",arr) '''

#Print Patter using loop.


'''for i in range(1,6):
  for j in range(1,i+1):
     print(j,end=" ") 
  print()'''

 # C Program to Calculate the Power of a Number(using loop only).

'''base=int(input("enter base:"))
exponent=int(input("enter exponent:"))
result=1
if exponent<0:
  for i in range(-exponent):
    result*=base
    result=1/result
else:
  for i in range(exponent):
    result*=base
print(f"{base}^{exponent}={result}") '''

 #Program to Check Whether a Number is Prime or Not
'''num=int(input("enter a number:"))
if num>1:
  for i in range(2,num):
    if num%i==0:
      print(num,"is not a prime number")
      break
  else:
    print(num,"is a prime number")
else:
   print(num,"is not a prime number")'''  

  
  #Program to find LCM of two numbers using while loop
'''def find_lcm(a,b):
 if a>b:
  max_num=a
 else:
  max_num=b
 while True:
     if max_num%a==0 and max_num%b==0:
        lcm=max_num
        break
     max_num+=1
 return lcm    
num1=int(input("enter a first numner:"))        
num2=int(input("enter secong number:"))
print(f"lcm of {num1} and {num2} is {find_lcm(num1,num2)}")'''

 #Program to Display Characters from A to Z Using Loop with count.
'''alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count=1
for letter in alphabet:
  print(letter+str(count),end=" ")
  count+=1'''

#Program to find a missing number

'''n=7
arr=[4,1,2,5,7,3]
for num in range(1,n+1):
  found=False
  for i in arr:
    if i==num:
      found=True
      break

  if not found:
      print(f"{num} is missing")
      break '''

#Program to count vowels and consonants in a given String.
 
'''string = input("Enter a string: ")
vowels = 0
consonants = 0

for char in string:
    ch = char.lower()
    if 'a' <= ch <= 'z':  # Ensures it's a letter
        if ch in ('a', 'e', 'i', 'o', 'u'):
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)'''

 #program to insert  the elements of an array for specific index.

'''def insert_at_index(arr, index, value):
    # Create a new array with one extra space
    new_arr = [0] * (len(arr) + 1)
    
    # Copy elements before index
    for i in range(index):
        new_arr[i] = arr[i]
    
    # Insert new value
    new_arr[index] = value
    
    # Copy remaining elements
    for i in range(index, len(arr)):
        new_arr[i + 1] = arr[i]
    
    return new_arr

# Given input
arr = [1, 2, 3, 4, 5, 6, 8, 9, 10]
index = 6
value = 7

# Insert the value at the specified index
arr = insert_at_index(arr, index, value)

# Insert another value at index 6

print(arr)	'''	

 #Reverse a number using while Loop
  
'''def reverse_number(n):
  rev_num=0
  while n>0:
    digit=n%10
    rev_num=rev_num*10+digit
    n=n//10
  return rev_num
num=int(input("Enter a number:")) 
print("reversed_number:",reverse_number(num))'''



#33. Count occurrence of number:

''''def count_occurrences(lst, num):
    count = 0
    for item in lst:
        if item == num:
            count += 1
    return count

# Example usage:
numbers = [1, 2, 3, 4, 2, 2, 5, 6, 2,2,2]
target=2
print(count_occurrences(numbers,target))'''


'''def sec_lar(arr):
  if len(arr)<2:
    return None
  first=-float('inf')
  second=-float('inf')
  for num in arr:
    if num>first:
      second=first
      first=num
    elif num>second and num<first:
      second=num
  return second if second!=-float('inf') else None
print(sec_lar([10]))'''



'''def remove_dup(arr):
  uni_itms=[]
  for i in range(len(arr)):
    if arr[i] not in uni_itms:
      uni_itms.append(arr[i])
  return uni_itms
arr=(["the","big","cat","big"])
print(remove_dup(arr))'''
  
'''def uni_num(arr):
  for num in arr:
    count=0
    for other in arr:
      if num==other:
        count+=1
    if count==1:
        return num
arr=([1,2,1,2,1,2,3,3,4,4])        
print(uni_num(arr)) '''


'''def coun_char(char,text):
  if len(char)!=1:
    raise ValueError("first argument of number must be a single character")
  count=0
  for c in text:
      if c==char:
        count+=1
  return count
result=coun_char('c',"Cat in coutrt")
print(result)'''


'''def count_vowels(s):
  vowels={'a','e','i','o','u','A','E','I','O','U'}
  count=0
  for c in s:
    if c in vowels:
      count+=1
  return count
print(count_vowels("welcomei")) '''



'''def vice_versa(s):
  result=""
  for char in s:
     if 'a'<=char<='z':
       result+=chr(ord(char)-32)
     elif'A'<=char<='Z':
        result+=chr(ord(char)+32)
     else:
          result+=char
  return result
print(vice_versa("ANUSHA "))'''               


'''def vice_versa(s):
   result=" "
   for char in s:
       if 'a'<=char<='z':
        result+=char(ord(char)-32)
       elif 'A' <=char<='Z':
         result+=char(ord(char)+32)
       else:
          result+=char
   return result
print(vice_versa("AnUShA"))'''


'''def mul_by_two(num):
  return num*2
n=6  
for i in range(1,n+1):
  print(mul_by_two(i),end=" ") '''  


'''def type_of_data(value):
    if value==None:
      return"nonetype" 
    elif isinstance(value,int):
      return"int"
    elif isinstance(value,float):
      return"float"
print(type_of_data(2))'''       



'''def reverse_in_groups(lst,k):
  first_part=lst[ :k][::-1]
  second_part=lst[k: ][ : :-1]
  return first_part+second_part
n=[1,2,3,4,5,6,7,8]
k=4
output=reverse_in_groups(n,k)
print(output) ''' 
