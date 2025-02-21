#1
# n= int(input("Enter the maximum no. of stars: "))
# for i in range(1,n+1):
#     pattern = "*" * (2*i-1)     # 2i-1 is to specify that the no. of stars should be odd
#     print(" " * (n-i),end="")   # to print spaces acc to req pattern & remove the default new line char as end
#     print(pattern,end="")
#     print("")                   # by default: new line char \n

#2
# n= int (input("Enter the maximum no. of stars: "))
# for i in range(1,n+1):
#     print('*' * i)    

#3
# n= int(input("Enter the max no. of stars: "))
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("*" * n, end=" ")
#     else:
#         print("*", end="")
#         print(" " * (n-2) , end ="")
#         print("*" , end="")
#     print("")

##4
# def pattern(): 
#     n=int(input("Enter the max. no. of stars: "))
#     for i in range(n, 0,-1):
#         print("*" *i)
# pattern()

# def pattern(n):       # alternate method
    # if (n==0):
    #     return 0
#     print("*"*n)
#     pattern(n-1)
# pattern(0)