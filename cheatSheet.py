#Programing is a process of working with data.

#Data in Python 

#4 atomic data types in python
s = "1"  #this value is a string data type
i = 1	#this value is a integer data type
f = 1.0 #this value is a float decimal data type
b = True #this value is a boolean data type

#real world examples
age = 24 #age is a whole number, so we use int
weight = 162.5 #weight is a decimal precision number, so we use float
greeting = "Hello, " #greetings require words, so we use strings


#Three collection data types (composite data types)
l = [] #empty list
d = {} #dictionaries
t = () #tuples

#real world example
classNames = ["kyle", "ryan", "john", "eric"]
print(classNames[0])

d = {'A1112': 'Kyle', 'A1113': "Eric"}
print(d["A1112"])

#Working with data

#statements vs expressions
print("1 + 1") #statement: literally prints 1+1
print(1+1) #expression: evalutes to 2 and prints that

#arithmetic operators 
print(1+1) #addition
print(2*2) #multiplication
print(3-2) #subtraction
print(4/2) #division

#built in functions/ modules
print(len("keyann")) #Built in function. Returns 6

import random    #built in module
print(random.randint(0,9))  #returns random number from 0,9

#loops
for name in classNames:
	print(name)

#logical comparisons
print(1 == 1) #Equality: True
print(1 == 0) #Equality: False
print(1 != 1) #Does not equal: False	
print(1>0) #Greater than: True
print(1<0) #less than: False
print(1>=0) #Greater than or equal: True
print(1<=0) #less than or equal: False

#logic operators
print(True and True)
print(True or False)
print(not True)


#conditionals/ selections/ logic
classNames = ["kyle", "ryan", "john", "eric"]
#finds longest name in a list
longestName = ""
for name in classNames:
	if(len(name) > len(longestName)):
		longestName = name

print("longest name is: ", longestName)


#functions
def func(param1, param2):
    return param1, param2

#lambda functions 
prod = lambda a, b : a * b
print(prod(5, 6))

#try/catch
a = int(input("Enter a value:"))
try:
    b = 10/a
except ZeroDivisionError:
    print("Zero is an invalid input")
except:
    print("Error")
else:
    print("Everything worked")
finally:
    print("This gets executed regardless of errors")
    
#raise an exception
a = 0

if a <= 0:
  raise Exception("Sorry, no numbers zero or below")

#example 2
a = "A string"

if not type(a) is int:
  raise TypeError("Only integers are allowed")
    




# itertools is memory efficient and quicker

# tabs instead of spaces

# strings and bytes are not interchangeable

# strings are unicode characters, bytes are 8-bit

# concatenation wont work for example. b= byte() s = b.decode('utf-8') or you can s.encode('utf-8')

# template strings for formatting

# built in functions transforms iterators utilities

# use em when possible cuz theyre built in as native code

# argument lists

# from collections,

# dictionaries, deques