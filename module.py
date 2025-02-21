def myFunc():
    print("Hello World!")
# myFunc()

print(__name__)    #o/p = __main__
# # after writing this line of code in this file, the advanced.py file will return o/p as 'module'(original file's name)

# But if I want to execute some piece of code only in this file then,
if __name__ == "__main__":         #to execute this, comment the lines 3,5 code so that the other files cann't use this file's functions
    # if this code is directly executed by runnning the file it is present in(i.e., module.py)
    print("We are executing the original file's code")
    myFunc()
    print(__name__)