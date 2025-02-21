import shutil

# to copy a file: copy() copy2()
shutil.copy('Files.py','FilesCopy.py')
# copy2() is same as copy() but copy2() also copy the metadata of a file
# to copy a folder: copytree() 

shutil.move(r"C:\Users\HP\Desktop\SNEHA\#100DaysPython\extraOutputFiles/table.txt", "table.txt")  
# the above command will move the "table.txt" outside the "extraOutputFiles" folder