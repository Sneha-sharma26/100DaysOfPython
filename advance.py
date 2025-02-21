## Walrus Operator (:=)
# if ( n := len([1,2,3,4,5])) > 3 :       # n is assigned the value of list & then used in the comparison within if stmt
#     print(f"List is too long ({n} elements, expected <= 3)")
# # it is same as :
# n = len([1,2,3,4,5])
# if n>3 :
#     print(f"List is too long ({n} elements, expected <= 3)")
    
## Type Hints/Type Definiton (Help the other programmers to easily get the datatype of a variable or fn)
# age : int = 19      # variable type hints
# # age.  # this will show a list of all the integer builtin functions
# # fn type hint
# def sum(a: int, b: int) -> int :
#     return a+b
# print(sum(3,5))  #this will show the required datatype of the inputs and tell the o/p datatype

## Advance type hints using "typing" module (allow developers to understand the data structues at a glance)
# from typing import List, Tuple, Dict, Union
# numbers: List[int] = [1,2,3,4,5]      # List of integers
# person: Tuple[str, int] = ("Sneha", 19)  # Tuple of a string & an integer
# scores: Dict[str, int] = {"Sneha": 94, "Amisha": 95} # dict of string keys & int values
# # Union for variables that can hold multiple types
# identifier: Union[int, str] = "ID123"
# identifier = "12345"  # also valid

## Match Case
# def http_status(status):
#     match status:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "Internal Server Error"
#         case _:
#             return "Unknown status"
# print(http_status(200))
# print(http_status(2008))

## Dictionary Merge(|) & Update(|=)
# dict1 = {"a":1, "b":2}
# dict2 = {"b":3, "c":4}
# merged_dict = dict1 | dict2    # dict merge
# print(merged_dict)
# dict1 |= dict2 #dict update (No need to create a new variable to add new key-value pairsfrom other dicts)
# print(dict1)

## Multiple file opening/ managing using single with stmt
# with (
#     open('File.txt') as f1,
#     open('poems.txt') as f2
# ) :
#     # Perform operations with the files
#     content1 = f1.read()
#     content2 = f2.read()

#     print("Content of File.txt:")
#     print(content1)

#     print("\nContent of poems.txt:")
#     print(content2)

## Exception Handling
# try: 
#     a = int(input("Enter a no.: "))
#     print(a)
# except Exception as e:
#     print(e)
# print("Thank You!")
# # if user enters a str or something invalid input, then error will occur
# # to handle that error except block is executed & so the exception is printed(due to print(e)), instead of crashing the program
# # & then Thank YOu stmt is executed successfully => code flow is not broken
# a = int(input("Enter a no.: "))
# print(a)
# print("Thank You!")    # in this compiler will throw error if i/p is not int, & so this stmt is not executed!! 

# 1. we can also handle a particular type of error by specifying the particular error type in 'except' block
# try: 
#     a = int(input("Enter a no.: "))
#     print(a)
# except ValueError as v:
#     print("A ValueError occurred! Please enter a valid input.")
# print("Thank You")

# 2. Raising Custom Exceptions using 'raise' keyword
# a = int(input("Enter a no. : "))
# b = int(input("Enter 2nd no. : "))
# if b == 0 :
#     raise ZeroDivisionError("Division by zero is not defined! Try again!!")
# else :
#     print(f"The division = {a/b}")

# 3. try with else 
# try:
#     a = int(input("Enter a no.: "))
# except Exception as e:
#     print(e)
# else:     # Executed only if 'try' was successful
#     print("Thank You!")

# 3. try with finally
# try:
#     a = int(input("Enter a no.: "))
# except Exception as e:
#     print(e)
# finally:   # run irrespective of try was successful or not
#     print("I'm into finally block!")

# we can simply run the finally code without finally block but
# finally mainly tab use hota h jab kisi fn ko define krte h 
# & if usme try ya except kuch return kre to without finally code run ni hota
# so to run that code on compulsory basis, finally is used

# def main():
#     try:
#         a = int(input("Enter a no.: "))
#         print(a)
#         return a
#     except Exception as e:
#         print(e)
#         return 
#     # finally:    # with finally
#     #     print("I'm into finally block!")
#     # without finally block 
#     print("I'll not run without finally block!")
# main()

## __name__ == "__main__"
# I've created a module named 'module.py' & in this file I'm importing that module's function(myFunc)
# from module import myFunc     # if I run this => return "Hello World!"
# # after executing (if __name__ == "__main__") code in module.py file, now we cann't access the myFunc functionality

## Global vs Local Keyword
# a=48    # global variable ((defined outside the fn)
# def func():
#     global a   # now this will make 'a' global var and so outside the fn it's value will be 3 
#     a = 3     # local variable
#     print(a)
# # a=48    # global var (defined outside the fn)
# func()
# print(a)

## Enumerate Function
# l = [2,34,55,4]
# index = 0
# for item in l:
#     print(f"The item at index {index} is {item}")
#     index += 1

# # This can be executed by enumerate fn (returns items of any list/tuple with index)
# for index, item in enumerate(l):
#     print(f"The item at index {index} is {item}")

## List Comprehensions (creating lists from exisitng lists)
# list1 = [1,2,3,4,5]

# squaredList = []
# for i in list1 :
#     squaredList.append(i*i)
# print(squaredList)

# This can be done using list comprehensions
# squaredList = [i*i for i in list1] 
# print(squaredList)

## Printing 3rd, 5th & 7th element from a list using enumerate fn
# l1 = [1,2,3,4,5,6,7]
# for index, item in enumerate(l1):
#     if index ==2 or index == 4 or index == 6 :
#         print(item)

## To print a list which contains the multiplication table of a user entered no. using list comprehension & storing it into a file
# n = int(input("Enter a no. : "))
# table = [i*n for i in range(1,11)]
# # print(table)
# with open('table.txt','a') as f:
#     f.write(f"Table of {n}: {str(table)} \n")

## Lambda Function 
# def square(n):
#     return n*n
# print(square(3))
# Now, this can be done by using lambda fn in which we create expression instead of fn
# square = lambda n : n*n
# print(square(2))

# sum using lambda fn
# sum = lambda a,b,c : a+b+c
# print(sum(8,3,5))

## Join Method(strings)
# l1 = ['Shruti','Sneha','Amisha']
# final = "__".join(l1) 
# print(final)

## Format Method (NOt much used due to f strings)
# info = "{} is a good {}".format("Sneha","girl")
# print(info)
# info = "{1} is a good {0}".format("Sneha","girl")
# print(info)

## Map, Filter & Reduce
# 1. Map =>
# l = [1,2,3,4,5,6]
# cube = lambda x: x**3
# cubeList = map(cube,l)  # Mapped a fn to all the items of an iterable
# print(list(cubeList))         # list is written to convert o/p into list otherwise the o/p was of form '<map object at 0x000002B469AB49A0>'

# 2. Filter => 
# def even(n):
#     if (n % 2 == 0) :
#         return True
#     return False    # No need to write else, as in case 'if' not executed, this will automatically run

# # even = lambda n: n % 2 == 0   # lambda fn of above fn

# onlyEven = filter(even,l)    # created a list of items for which fn returns true
# print(list(onlyEven))

# 3. Reduce => 
# from functools import reduce
# l = [1,2,3,4]
# sum = lambda a,b : a+b 
# output = reduce(sum, l)    # applies rolling computation to sequential pairs of input iterable
# print(output)  # 1 + 2 = 3 + 3 = 6 + 4 = 10

## seek() & tell() fn of file
# with open("File.txt",'r') as f:
#     print(type(f))
#     f.seek(5)   # move the cursor to 6th char of the file
#     print(f.tell())   # 0/P= 5 -> tells the current position of the cursor in a file
#     print(f.read(3))  # read the next 3 char/bytes
#     print(f.tell())  # 0/P= 8 
    
## truncate() fn
# with open('sample.txt','w') as f:
#     f.write("Hello World!")
#     f.truncate(3)
    
# with open('sample.txt','r') as f:
#     print(f.read())

## '==' vs 'is'
# a = 4
# b = 4
# print(a is b)  # compares identity of 2 objects or exact location of object in memory
# print(a == b)  # compares the values of the objects
# # o/p true bcoz 4 ke liye 1 baar hi location assign hogyi
# a = [12,2,4]
# b = [12,2,4]
# print(a is b)  # False, bcoz b k liye alag location assign hogi bcoz it is mutable
# print(a == b) 

## Access Specifiers (In py, agar __ use hoga to mangling hogi otherwise _ doesn't provide any protection)
# class Employee:
#     def __init__(self):
#         self.name = "Harry"   # by default, public variable
#         self.__age = 19     # using '__' before var name, makes it private 
#         self._location = "Rewari"  # protected(_) var
# a = Employee()
# print(a.name)
# print(a._location)
# # print(a.age)  # cann't be accessed directly
# print(a._Employee__age)  # can be access indirectly in py due to 'Name Mangling'
# # Name Mangling is used to protect private class & superclass from being overwritten by subclasses 

## dir(), __dict__ and help methods
# 1. dir() method =>
# x = [1,2,3]
# print(dir(x))    #return attributes and methods of an object
# print(x.__add__) 

# 2. __dict__ =>
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.version = 1
# p = Person("John", 30)
# print(p.__dict__)     # Returns object's attributes(given by self) as dictionary 
# # 3. help() method =>
# print(help(Person))     # returns a help document for an object including description of it's attributes & methods
# print(help(str))

## Method Overriding 
# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def area(self):
#         return (self.x * self.y)
    
# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r
#     def area(self):
#         return (3.14 * self.r**2)  
    
# rec = Shape(3,6)
# print(rec.area())
# c = Circle(4)
# print(c.area())

# # Instead of rewriting the area() method in child class, we can override it as :
# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def area(self):
#         return (self.x * self.y)
    
# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r
#         super().__init__(r, r)  # x=r & y=r => Shape's area() = self.r * self.r = self.r**2
#     def area(self):
#         return (3.14 * super().area())   # override the method area() of parent class 'Shape'
# c = Circle(4)
# print(c.area())

## Time Module
# import time
# def usingwhile():
#     i = 0
#     while i<50:
#         i = i+1
#         print(i)
    
# def usingfor():
#     for i in range(50):
#         print(i)
# init = time.time()   # return current time in seconds since the Epoch(when time starts 1 Jan 1970) 
# usingwhile()
# print(time.time()-init) # here, it shows time after program run - time before program run = time taken by program to execute
# usingfor()
# print(time.time()-init)

# print(4)
# time.sleep(2)  # sleep() fn delays the execution after 2
# print("This is printed after 2 seconds")

# t = time.localtime()
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
# print(formatted_time)

## requests module
# import requests
# response = requests.get("https://www.google.com")
# print(response.text)

## Command Line Utility
# 1. eg: curl 
# step1: copy any online image path
# step2: open command prompt & type "curl image-path --output destination-name"
# step3: we'll get the output on the destination

# 2. To create our own command line utility, "argparse"(built-in) module is used
# import argparse
# import requests

# # code for download file using requests
# def download_file(url,local_filename):
#     with requests.get(url,stream=True) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size = 8192):
#                 f.write(chunk)
#     return local_filename

# parser = argparse.ArgumentParser()

# # add command line arguments
# # syntax: parser.add_argument("arg2", help="description of argument 2")
# parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="by which name do you want to save your file? ")
# # parse the arguments
# args = parser.parse_args()
# # Use the arguments in your code
# print(args.url)
# print(args.output)
# download_file(args.url, args.output)   # to download any file type "python advance.py(i.e., filename.py) link-of-any-image/file outputname.jpg"

## Generators (Generates on-the-fly values instead of creating & storing the entire sequence)
# def my_generator():
#     for i in range(3):
#         yield i         # yield stmt returns a value from generator & suspends the exexution until next value is requested
# gen = my_generator()
# print(next(gen))    # 0    # next() fn is used to request the next value from generator
# print(next(gen))    # 1
# print(next(gen))    # 2
# # o/p can be generated using for loop :
# for j in gen:
#     print(j)
