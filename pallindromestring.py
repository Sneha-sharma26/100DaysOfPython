def ispallindrome(str):
    rev_str= str[::-1]
    return str == rev_str

str=input("Enter a string to check if it is pallindrome: ").lower()   
if ispallindrome(str):
    print("It\'s a pallindrome string")
else:
    print("not a pallindrome string")

    