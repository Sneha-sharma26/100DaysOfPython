# print("Hello")
# #that's comment
# print("I \"am\" a \n Sneha")
# print("hey",7,9,sep="~",end="null\n")

# a=20+30j
# b=None
# print(type(a))
# print(type(b))

# print(dir(str))

# b= "Sneha"
# print(len(b))
# print(b[2:5:1])

# b=input("Enter your name: ")
# print('my \"name\" is',b)
# # print(f"my name is {b}")

# a= """my
# name
# is sneha
# jeehe"""
# for i in a:
#     print(i)
# print(a[9])

# nm="sneha is a amazing python teacher"
# print(nm[-4:-2])
# print(len(nm))
# print(nm.startswith('ha')) #returns false bcoz of H and h

# letter='''
#         Dear <|Name|>,
#         You are selected!
#         <|Date|>
#         '''
# print(letter.replace("<|Name|>","Sneha Sharma").replace("<|Date|>","26th June"))

# list=["sneha",33,False,9,True]
# b="Hehe"
# print(dict.fromkeys(list,b))
# list[2]=True
# print(list)    #can change a particular value in list unlike strings

# tuple=(1) 
# print(type(tuple))    #output will be 'int' but if we put ',' after 1 then 'tuple'

#marks of 6 students entered by user in sorted manner
# marks=[]
# s1=int(input("Enter marks of student 1: "))
# marks.append(s1)
# s2=int(input("Enter marks of student 2: "))
# marks.append(s2)
# s3=int(input("Enter marks of student 3: "))
# marks.append(s3)
# s4=int(input("Enter marks of student 4: "))
# marks.append(s4)
# s5=int(input("Enter marks of student 5: "))
# marks.append(s5)
# s6=int(input("Enter marks of student 6: "))
# marks.append(s6)
# marks.sort()
# print(marks)

# dict= { "Sneha": 99,"Ram":22}
# dict.setdefault("ram")
# print(dict)
# print(type(dict.items()))

# list=["sneha",33,False,9,True]
# b="Hehe"
# print(dict.fromkeys(list,b))

# s={}         #it will be a empty dictionary
# print(type(s)) 
# s=set()       #this will form a empty set
# print(type(s)) 

# set={3,6,23,66,"ram"}
# s2={66,3,9}
# set.difference_update(s2)
# print(set)

# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))  #not =3 it's =2

# s = {8,7,12,"sneha",[1,2]}     #cann't have a list in set & change the value of list in the set

## Student passed only if got marks in each subject > 33 and total percentage >=40
# m1 = int(input("Enter marks of subject 1: "))
# m2 = int(input("Enter marks of subject 2: "))
# m3 = int(input("Enter marks of subject 3: "))
# perc = ((m1 + m2 + m3)/300 ) * 100
# if (perc <= 40):
#     print("Oops! You are failed.")
# elif (perc >= 40 ): 
#     if (m1>33 and m2>33 and m3>33):
#         print("Yay! You've passed.")
#     else:
#         print("Oops! You are failed.")
# else:
#     print("Enter valid marks.")

## --- Spam Detector ---
# list=["Make a lot of money","buy now","subscribe this","click this"]
# m1="Make a lot of money"
# m2="buy now"
# m3="subscribe this"
# m4="click this"
# msg = input("Enter your msg: ")
# if ((m1 in msg) or (m2 in msg) or (m3 in msg)):
#     print("It's a spam msg !!")
# else:
#     print("You are good to go!!")

## Greet people whose name starts from S
# l= ["sneha","Soham","Sachin","Rahul"]
# for i in l:
#     if i.startswith("S"):
#         print(f"Hi {i}")

## print reverse table of a no.
# n = int(input("Enter a no. to print reverse table: "))
# # for i in range(1,11):
#     # print(f"{n} * {11-i} = {n*(11-i)}")        # 11-i will tend to 1->10 , 2->9 , 3->8
# for i in range(10,0,-1):               # alternate method
#     print(f"{n} * {i} = {n*i}")

# n= int(input("no. to find fibonacci seq upto: "))
# seq1=0
# seq2=1
# seq=seq2
# print(seq1, end=" ")
# for i in range(0,n+1):
#     print(seq2,end=" ")
#     seq1,seq2= seq2, seq
#     seq= seq1+seq2

##Calc sum of the digits of a no.
# n=int(input("Enter a no.: "))
# s=0
# while n>0:
#     s+=int(n%10)
#     n=int(n/10)
# for i in n:             #alternate method but take the i/p as string
#     s += int(i)
# print(s)

## Short hand if else  result = value_if_true if condition else value_if_false
# a = 330
# b = 3308
# print("A") if a>b else print("B") if a == b else print("C")

## match case
# x= int(input("Enter a no.: "))
# match x:
#     case 1:
#         print("hehe")
#     case 2:
#         print("sneha")
#     case 3:
#         print("it is 3")
#     case _ if x!=8:
#         print("kriti")

##non parameterized function
# def greet():   
#     name= input("Enter ur name: ")
#     print(f"Good Day Miss/Mr. {name.title()}")
# greet()

## parameterized fn
# def greet(name):
#     print(f"Good Day Miss/Mr. {name.title()}")
# greet("sneha")

# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     return n * fact(n-1) 
# n=int(input("Enter a no. to find factorial: "))
# print(f"Factorial of the no. is {fact(n)}")

## func to check if a no. is prime
# def prime(n):
#     if n>1:
#         for i in range(2,(n//2)+1):
#             if (n%i==0):
#                 return
#         else:
#             print("it is a prime no.")
# prime(51)

#reverse the str func
# def reverse(s):
#     revs=""
#     for i in range(len(s)-1, -1, -1):
#         print(s[i],end="")
# reverse("kavita")

#func that takes 2 list as i/p & return their intersection   
# def common(l1,l2):
#     return list(set(l1).intersection(set(l2)))
# l1=[9,"Shreya",True]  
# l2=[9,False,True]
# print(common(l1,l2))

##func to check if a str is pallindrome or not
# def check(s):
#     for i in range(0,len(s)+1):
#         if s[i]==s[i-1]:
#             print("Yes it's a pallindrome string.")
#         else:
#             return
# s="car"
# check(s)
    
## print the sum of elements of lists if element>0
# def sum(l):
#     hehe=0
#     for i in l:
#         if i>0:
#             hehe += i
#         else:
#             continue
#     print(hehe)
# l=[2,6,-11,1,-13,77]  
# sum(l)   

## square of the elements in the list
# def square(l1):
#     '''Take a list of nos. and returns square of all the elements'''     # docstring 
#     l2 = []
#     s=0
#     for i in l1:
#         s = i * i
#         l2.append(s)
#     return l2
# l1 = [2,6,-11,1,-13,77]
# print(square.__doc__)        # to print the docstring
# print(square(l1))
# l3=[7,9]
# print(square(l3))

# import this         # The Zen of Py

########################################## OOPS #################################

## A basic example of class
# class Employee():
#     language = "py"           # class attribute as it directly belongs to the class
#     salary = 120000         # class attribute

# harry = Employee() # obj 1
# harry.name = "Harry"      # obj/instance attribute 
# print(harry.name, harry.language, harry.salary)

# sneha = Employee() # obj 2
# sneha.name = "Sneha"
# sneha.language = "Html"      # now instance attribute will take preference over class attribute, so py will not be printed in language
# print(sneha.name, sneha.language, sneha.salary)

## the concept of SELF PARAMETER
# -- the incorrect code --
# class Employee():
#     language = "py"           
#     salary = 120000        
    
#     def getInfo():    # a method/ function
#         print(f"My language is {language} and salary is {salary}")

# harry = Employee()      
# harry.getInfo()   # in this case, there will be error => Employee.getInfo() takes 0 positional arguments but 1 was given
# => as harry.getInfo works as Employee.getInfo(harry) in which 1 argument is given, but while defining the function we didn't gave any argument
# => so to solve this issue we use self parameter/argument 

# -- the correct code --
# class Employee():
#     language = "py"          
#     salary = 120000           
#     def getInfo(self):    # a method/ function
#         print(f"My language is {self.language} and salary is {self.salary}")
# harry = Employee()
# harry.getInfo() # or 
# Employee.getInfo(harry)

# ⭐=> Hum koi bhi method banaye, self parameter is necessary whether we use it or not in the function/method

## use of static method (@staticmethod)
# -- the incorrect code --
# class Employee() :
#     def greet() :
#         print("Good morning")
# harry = Employee()
# harry.greet()    # greet fn without self will show error but here no 'self' is needed that means we need not to pass a object's attribute to greet()
# => we can write @staticmethod before defining the greet() which means that this function doesn't need self parameter
# -- the correct code --
# class Employee() :
#     @staticmethod
#     def greet() :
#         print("Good morning")
# harry = Employee()
# harry.greet()

## __init__() contructor
# class Employee() :
#     language = 'py'
#     salary = 120000
    
#     def __init__(self) :   # constructor called out every time when an object is created
#         print("I'll be called out every time.")
        
# harry = Employee() 
# harry.name = "Harry"
# print(harry.name, harry.language, harry.salary)

# -- Example-- to print the attributes without writing it in different line of codes like harry.name = "Harry"
# class Employee() :
#     language = 'py'
#     salary = 120000
    
#     def __init__(self, name, language, salary) :   # constructor called out every time when an object is created
#         self.name = name 
#         self.language = language
#         self.salary = salary
#         print("I'll be called out every time.")
        
#     def getInfo(self) :
#         print(f"I am {self.name}, my favourite language is {self.language} and my salary is {self.salary}")
        
# harry = Employee("Harry", "Javascript", 130000)  # it's due to init that we are able to pass values here instead of writing manually like harry.language = "Javascript"
# harry.getInfo()

## Class to store information of programmers
# class Programmer :
#     company = "Microsoft"
#     def __init__(self, name, jobTitle, salary) :
#         self.name = name
#         self.jobTitle = jobTitle
#         self.salary = salary
#     def getInfo(self) :
#         print(f"My name is {self.name}. I am {self.jobTitle} at Microsoft and I earn {self.salary} per month.")
# #obj initialisation 
# person1 = Programmer("Sneha", "Software Developer", 120000)
# person1.getInfo()
# person2 = Programmer("Amisha", "Chief Executive", 120000)
# person2.getInfo()

## Class 'Calculator' to find square, cube and square root of a no.
# class Calculator :
#     def __init__(self, num) :
#         self.num = num
#     def square(self) :
#         print(f"{self.num ** 2}")
#     def cube(self) :
#         print(f"{self.num ** 3}")
#     def squareroot(self) :
#         print(f"{self.num ** (1/2)}")
# n1 = Calculator(4)
# n1.square()
# n1.cube()
# n1.squareroot()

## Class with class attribute a; then creating an obj from it & set a directly using object.a=0
# class Demo :
#     a = 4
# obj1 = Demo()
# print(obj1.a)
# obj1.a = 5
# print(obj1.a)  # no, class attribute doesn't changes because obj1.a just sets the instance attribute temporarily
# print(Demo.a)

## Calculator with static method to greet user with hello
# class Calculator :
#     def __init__(self, num) :
#         self.num = num
#     @staticmethod
#     def greet():
#         print("Hello")
#     def square(self) :
#         print(f"{self.num ** 2}")
#     def cube(self) :
#         print(f"{self.num ** 3}")
#     def squareroot(self) :
#         print(f"{self.num ** (1/2)}")
# n1 = Calculator(4)
# n1.greet()
# n1.square()
# n1.cube()
# n1.squareroot()

## class Train which had methods to book a ticket, get status(no. of seats) & fare info of train
# import random      # to generate random fare of train
# class Train():
#     @staticmethod
#     def greet():
#         print("Welcome to Indian Railways :)")
#     def __init__(self, trainNo):
#         self.trainNo = trainNo
#     def book(self, fro, to):    # 'fro' stands for 'from'
#         print(f"Ticket is booked in train no.: {self.trainNo} from {fro} to {to}")
#     def getStatus(self):
#         print(f"Train no.: {self.trainNo} is running on time.")
#     def getFare(self, fro, to):
#         print(f"Ticket fare in train no.: {self.trainNo} from {fro} to {to} is {random.randint(219, 5541)}")
# t = Train(221130)
# t.greet()
# t.book("Delhi", "Banglore")
# t.getStatus()
# t.getFare("Delhi","Banglore")

## Changing self parameter to something else let's slf
# class Employee():
#     language = "py"          
#     salary = 120000           
#     def getInfo(slf):    # a method/ function
#         print(f"My language is {slf.language} and salary is {slf.salary}")
# harry = Employee()
# harry.getInfo() 
# => NO effects

## Inheritance (example of Multilevel Inheritance)
# class Employee:
#     name = "Default name"
#     def showName(self) :
#         print(f"Name of the employee is {self.name}")
# class Manager(Employee):
#     company = "ITC Infotech"
#     def showCompany(self):
#         print(f"Name of the company is {self.company}")
# class Programmer(Manager):
#     lang = "Python"
#     def getInfo(self) :
#         print(f"Language I am comfortable with is {self.lang}")
# obj1 = Employee()
# obj1.showName()
# obj1.showCompany()   # show error as there is this function is not the fn of base class
# obj1.getInfo()     # show error as there is this function is not the fn of base class

# obj2 = Manager()
# obj2.showName()        # inherited the function and attribute of base class
# obj2.showCompany()  
# print(obj2.name)      # got the attribute of base class
# obj2.getInfo()        # show error as there is this function is not the fn of base class

# obj3 = Programmer()
# obj3.showName()       # inherited the function and attribute of base class
# obj3.showCompany()     # inherited the function and attribute of base class
# obj3.getInfo()

## super() METHOD => used to call the method of super class
# class Employee:
#     name = "Default name"
#     # def __init__(self) :
#     #     print("Constructor of Employee")
#     def showName(self) :
#         print(f"Name of the employee is {self.name}")
        
# class Manager(Employee):
#     company = "ITC Infotech"
#     # def __init__(self) :
#     #     super().__init__()
#     #     print("Constructor of Programmer")
#     def showCompany(self):
#         super().showName()        # this is calling the function of super class Employee
#         print(f"Name of the company is {self.company}")
# obj1 = Manager()
# print(obj1.name)
# obj1.showCompany()

## class METHOD (To print the value of class attribute even after changing it white object instantiation)
# class Employee:
#     a = 1
#     def show(self):
#         print(f"The class attribute's value of a is {self.a}")
# e = Employee()
# e.a = 45
# e.show()    # this will give the value of a = 45, But we need the a = 1 (the class value of a)
# so for this purpose we use class method

# class Employee: 
#     a = 1
#     @classmethod
#     def show(cls):          # instead of self => cls is used
#         print(f"The class attribute's value of a is {cls.a}")
# e = Employee()
# e.a = 45
# e.show()  

## => class method as alternative constructors
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
# e1 = Employee("Harry", 12000)
# print(e1.name)
# print(e1.salary)
# # in the above case imagine instead of getting input as Harry and 12000 directly, we get a string = "John-12000"
# # for this we can direclty use e2 = Employee(string.split("-")[0], int(string.split("-")[1])) to get it in the required format
# # But for a lot of objects we need to repeat this again n again, so to make code more representable, to save time and
# # to handle data in different formats, we can use class method as alternative constructors
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     @classmethod
#     def fromStr(cls, string) :
#         return cls(string.split("-")[0], int(string.split("-")[1]))     
# e1 = Employee("Harry", 12000)    # obj in simple format
# print(e1.name)
# print(e1.salary)

# string = "John-12000"
# e2 = Employee.fromStr(string)    # obj in string format
# print(e2.name)
# print(e2.salary)

## Decorators
# def hello():        # a normal function
#     print("Hello world!!")    
# hello()            # fn call
# # Now, let I want to wish good morning to user before the function run &
# # say Thank You when fn stops running 
# # instead of adding these wishes manually each time before running the fn
# # Decorators are used to extend the functionality of the fn without modifying its source code

# def greet(fx):             # Decorator fn
#     def mfx():                # The modified or new fn
#         print("Good morning")
#         fx()              # calling the original fn
#         print("Thanks for using this fn")
#     return mfx
# @greet           #calling the decorator fn
# def hello():
#     print("Hello world!")
# hello()    # or 
# #greet(hello)()

## Property Decorators
# class Employee:
#     a = 1
#     @property     # makes the fn as object attribute & sets it's value (i.e., e.name)
#     def name(self):
#         return f"{self.fname} {self.lname}"
#     @name.setter        # setter decorator is used with property decorator to set the value of the attribute
#     def name(self,value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]
# e= Employee()
# e.name = "Harry Potter"
# print(e.fname)
# print(e.lname)
# # due to @property, getter & setter decorators, all the implementation details are abstracted from user
# # as the user have to only input the name and setter will automatically split it into first name & last name

## Operator Overloading(Operators are overloaded using dunder/magic methods)
# it defines ki konsa operator... kis datatype k liye... kya operation perform krega
# class Number:
#     def __init__(self,n):
#         self.n = n
#     def __add__(self,num) :     # it defines what '+' operator should perform
#         return self.n + num.n   #'num' k sath '.n' is used to change it's datatype to int from str
# n = Number(34)
# m = Number(23)
# print(n+m)

## 2D class creating 3D class
# class TwoDVector :
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j
#     def show(self):
#         print(f"The 2D vector is {self.i}i + {self.j}j")
# class ThreeDVector (TwoDVector):
#     def __init__(self,i, j, k):
#         super().__init__(i,j)  # access the init method of TwoDVector
#         self.k = k 
#     def show(self):
#         print(f"The 2D vector is {self.i}i + {self.j}j + {self.k}k")
# a = TwoDVector(1,2)
# a.show()
# b = ThreeDVector(5,8,3)
# b.show()

## Employee's salary & more properties using @property & setter
# class Employee:
#     salary = 12000
#     increment = 25
#     @property
#     def salaryAfterincrement(self):
#         return (self.salary + self.salary * (self.increment/100))
#     @salaryAfterincrement.setter
#     def salaryAfterincrement(self, salary):
#         self.increment = ((salary / self.salary) -1) * 100
# e = Employee()
# # print(e.salaryAfterincrement)
# e.salaryAfterincrement = 15000
# print(e.increment)

## Method overloading eg using complex no.
# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i
#     def show(self):
#         print(f"Complex no. is: {self.r} + {self.i}j")
#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)
#     def __str__(self):    # without this method, the o/p was of form <__main__.Complex object at 0x000002691B1DAFF0>
#         return f"{self.r} + {self.i}j"
# c1 = Complex(2, 5)
# c2 = Complex(3, 4)
# c1.show()
# c2.show()
# print(c1 + c2)

## str() method (overloaded method) to print vector as 7i + 8j + 10k
# class Vector :
#     def __init__(self, i, j, k):
#         self.i = i
#         self.j = j
#         self.k = k
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
# v1 = Vector(7,8,10)
# print(v1)