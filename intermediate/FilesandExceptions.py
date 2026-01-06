# Opening a file
import os
'''
f = open("test.txt", "w")
# print(f)
# The open function takes two arguments. The first is the name of the file, and the
# second is the mode. Mode "w" means that we are opening the file for writing.
# If there is no file names text.txt, it will be created

# Writing content into our created file
f.write("Now is the time ")
f.write("for the Kingdom of God to manifest!")

# Closing the file tells the system that we are done writing and makes the file
# available for reading:
f.close() 

# Opening the file to read it's content
f = open("test.txt", "r")
# This displays the content
text = f.read()
print(text)

# read() accepts arguments that indicates how many character to read
f = open("test.txt","r")
print(f.read(10))

# Copying a file content and writing into another file:
import os
def copyFile(oldFile, newFile):
    f1 = open(oldFile, "r")
    f2 = open(newFile, "w")
    while True:
        text = f1.read(50)        
        if text == "":
            break
        f2.write(text)
    f1.close()
    f2.close()
    return 

print(copyFile("Mathew_C25_V31.txt", "file_two.txt"))
'''

# TEXT FILES
# A text file is a file that contains printable characters and whitespace, organized
# into lines separated by newline characters.
'''
file = open("newFile.txt", "w")
file.write("Now is the time")
file.write("\nto close the file")
file.close()

file = open("newFile.txt", "r")
# read can also take an argument that indicates how many characters to read:
# print(file.read(16))
print(file.readlines())

# display = file.read()
# print(display)


# f = open("tt.txt", "w")
# print(f)


nf = open("Example1.txt", "w")
nf.write("Line One\nLine Two\nLine Three")
nf.close()

nf = open("tt.txt", "r")
print(nf.readline())
print(nf.readlines())
'''

# The following is an example of a line-processing program. filterFile makes a
# copy of oldFile, omitting any lines that begin with  # :
def filterFile(oldFile, newFile):
    f1 = open(oldFile, "r")
    f2 = open(newFile, "w")
    while True:
        text = f1.readline()
        if text == "":
            break
        if text[0] == "#" :
            continue
        f2.write(text)
    f1.close()
    f2.close()
    return

# EXCEPTION
filename = input("Enter a file name: ")
try:
    f =  open(filename,"r")
except IOError:
    print("There is no file named", filename)

def inputNumber():
    x = input("Pick a number: ")
    if x == 17:
        raise ValueError ("17 is a bad number")
    return x