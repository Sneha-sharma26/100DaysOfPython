# OS Module can be used to automate a lot of tasks
# to create a bulk of directories or to rename them
import os

if(not os.path.exists("data")):     # os function
    os.mkdir("data")

# To make a bulk of directory/folder   
for i in range(0,6):
    os.mkdir(f"data/Day {i+1}")
    
# To rename the folders
for i in range(0,4):
    os.rename(f"data/Day {i+1}", f"data/Tutorial {i+1}")

# To print the name of folders in a directory
folders = os.listdir("data")
print(folders)       # return the list of folders in directory "data"
# to print the files of folders of dir 'data'
for folder in folders:
    print(os.listdir(f"data/{folder}"))

print(os.getcwd()) # to get the current working directory
os.chdir("/Users")      # To change the working dir
os.remove()  # remove a file
os.rmdir()  # delete a selected dir