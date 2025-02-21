name=input("Enter your name: ")
age= int(input("Enter your age: "))
print(f"""Hey! {name} 
I know you are {age} years old.""")

##greet acc to time
import time                         #"time" module provides functions to work with time
current_time = time.localtime()     #returns a obj having info about local time such as hour, min, sec, etc.
hour= current_time.tm_hour          #tm_hour extracts hor value (0-23) 

# alternate method
t= time.strftime('%H:%MM:%S')
hour= int(time.strftime('%H'))
if 0 <= hour < 12:                  #compulsory code for both the ways
    print("Good morning!")
elif 12 <= hour > 17:
    print("Good afternoon!")
else:
    print("Good evening!")