## This lesson intends to teach Working with files in python
## create, open, read, write, close files
## Modes of opening file - read, write



## READ AS a single string --> Open, read, close file - encoding-utf8

# file = open("Lesson System.txt", "r")
# data = file.read()
# print(data)

## LOOP lines of file - loop , strip function,

# for line in file:
#     print(line)

# file.close()


## Ex: Print specified line in console
## Ex: Format file - show specified variables in console - 3 nefer - 3 added in format


#~~~~~~~~~~~~ APPEND ~~~~~~~~~~~~~~~~~~~~~~~~~~``
import os

file4 = open("Lesson System_copy.txt", "a")
file4.write("This is append")

file4 = open("Lesson System_copy.txt", "r")
data4 = file4.read()
print(data4)

#~~~~~~~~~~~~~ WRITE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# file3 = open("Lesson System_copy.txt", "w")
# file3.write("Demmo lesson")
# file3 = open("Lesson System_copy.txt", "r")
# last_data = file3.read()
# print(last_data)




## os.remove - os.path.exists

if os.path.exists("Lesson System_copy2.txt"):
    os.remove("Lesson System_copy2.txt")
    print("File removed")
else:
    print("File does not exist")