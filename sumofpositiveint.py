list=[1,-4,67,-23,0,55]
sum =0
for i in list:
    if i>0:
        sum+= i 
print(sum)

## alternate method
def theSum(list):
    s=0
    for i in list:
        if i>0:
            s+=i 
    return s
print(theSum(list))