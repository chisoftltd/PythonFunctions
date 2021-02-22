#Python Functions
import os
os.system("cls")

def my_function1():
    print("This is a function")
my_function1()
print()

#Arguments
def my_function(fname):
    print("Your name is : " + fname)

my_function("Ben")
my_function("Joy")
my_function("Emma")
my_function1()
print()

#Number of Arguments
def my_function2(fname, lname):
    print(fname + " " + lname)

my_function2("Benjamin", "Joy")
print()

#Arbitrary Arguments, *args
def my_function3(*kids):
    print("The youngest child is " + kids[2])
my_function3("Emma", "Shepherd", "Mikael")
print()

#Keyword Arguments
def my_function4(child3, child4, child1):
    print("The yougest child is " + child4)
my_function4(child1="Mikael", child4="Shepherd", child3="Emma")
print()

#Arbitrary Keyword Arguments, **kwargs
def my_function5(**child1):
    print("His last name is " + child1["child3"])
my_function5(child1="Mikael", child4="Shepherd", child3="Emma")

#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#Return Values
def my_function(x):
  return 5 * x

print(my_function(33))
print(my_function(25))
print(my_function(90))

#The pass Statement
def myfunction():
  pass

#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)