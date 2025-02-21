## to read the File.txt 
# f = open('File.txt')  # No need to mention the mode, while opening a file for reading purpose! It's automatically in r = read mode
# data = f.read()
# print(data)
# f.close() # if file is opened, it must be closed then

# to write st into the file
# st = 'I\'m a girl.'
# f = open("File.txt",'a')  # w = write mode
# f.write(st)
# f.close()

# f = open("File.txt")
# data = f.read()
# print(data)
# f.close() # The text in file is now the updated one!


## reading one full line using f.readline() function
# f = open('File.txt')
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# line3 = f.readline()
# print(line3)
# line4 = f.readline()
# print(line4)
# f.close()

# the alternate can be using while loop instead of reading single-single line again n again
# f = open('File.txt')
# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()
# f.close()

## with stmt (now we don't have to close the file explicitly ... apne aap close ho jayegi file)
# with open("File.txt") as f :
#     print(f.read())

## To check if 'twinkle' word is present in the text file or not
# f = open('poems.txt')
# data = f.read()
# word = 'twinkle'
# if word in data : # OR if "twinkle" in data :
#     print("Yes twinkle is in the file")
# else :
#     print("Naah! Not found")
# f.close()

## To print the hiscore of a game
# import random
# def game():
#     print("You are playing the game...")
#     score = random.randint(1,62)  # generate the random no. as score of the user
    
#     # fetch the data or score from the file
#     with open("Hi-score.txt") as f :
#         hiscore = f.read()
#         if (hiscore != "") :  
#             hiscore = int(hiscore)
#         else :  # if file is blank assume the current hiscore acc to file is 0
#             hiscore = 0
            
#     print(f"Your score is: {score}")
#     if (score > hiscore) :  # if user's current score is greater than the score mentioned in file than update the file
#         # write this score to file Hi-score.txt
#         with open("Hi-score.txt","w") as f :
#             f.write(str(score))
#     return score
# game()

## folder of files having tables from 2 to 20
# (done by me)
# for i in range(2,21) :
#     table = ""
#     with open(f"tables2/table_{i}.txt","w") as f :
#         print(f"Table of {i}: \n")
#         for j in range(1,11) :
#             table += f"{i} * {j} = {i*n} \n"
#         f.write(table)
### OR 
# (done by cwh)
# def generateTable(n) :
#     table = ""
#     for i in range(1,11) :
#         table += f"{n} * {i} = {n*i}\n"
#     with open(f"tables/table_{n}.txt","w") as f :
#         f.write(table)

# for i in range(2,21) :
#     generateTable(i)

## To replace the some words by ######
# words = ["Donkey","ganda","bad"]
# with open("file.txt","r") as f :
#     content = f.read()
# for word in words :
#     content = content.replace(word, "#" * len(word))
# with open("file.txt","w") as f :
#     f.write(content)

## to check whether log file (log.txt) contains 'python'
# with open('log.txt','r') as f:
#     content = f.read()
# if 'python' in content :
#     print("Yes, python is present")
# else :
#     print("NO, python is not present.")

## to check whether log file (log.txt) contains 'python' with line no
# with open('log.txt','r') as f:
#     lines = f.readlines()
    
# lineno = 1   
# for line in lines :
#     if 'python' in lines :
#         print(f"Yes, python is present in line no.: {lineno}")
#         break  ## if python is found then this will break the loop and so, no else loop will be executed!!
#     lineno += 1
# else :
#     print("NO, python is not present.")
    
## to make copy of file "this.txt"
# with open('this.txt') as f :
#     content = f.read()
# with open('this_copy.txt','w') as f :
#     f.write(content)

## to check whether two files are identical and their content also matches
# with open('File.txt') as f :
#     content1 = f.read()
# with open('log.txt') as f :
#     content2 = f.read()
# if(content1 == content2):
#     print("Yes, the files are identical.")
# else:
#     print("No, the files are not identical")

## to wipe out the content of a file using py
# with open("this.txt","w") as f :
#     f.write("")
    
## to rename a file  (we just read the content of old file and pasted it into new named file) 
# with open('this.txt') as f :
#     content = f.read()  
# with open("this_copy.txt", "w") as f: 
#     f.write("content") 