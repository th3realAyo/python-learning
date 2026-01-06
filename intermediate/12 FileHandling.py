import os

os.chdir("C:/Users/AYO_AYO/Desktop/Python/Files")
print(os.getcwd())

# Create Multiple Files
context = open("context.txt", "w")
context.write("Damilola\nSemilore\nOlajuwon\nWisdom")
context.close()

names = open("names.txt", "w")
names.write("Damilola\nSemilore\nOlajuwon\nWisdom")
names.close()

morenames = open("morenames.txt", "w")
morenames.write("Damilola\nSemilore\nOlajuwon\nWisdom")
morenames.close()

# R = Read 
# A = Append
# W = Write
# X = Create

#READ - Error if file doesn't exist

os.chdir("C:/Users/AYO_AYO/Desktop/Python/Files")

f = open("context.txt", "r")
# print(f.read())
# Reading the first 8 characters
# print(f.read(8))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)
f.close() #Closing the file once done is very important.

#Opening a non-existent file (what to do, to avoid error):
try:
    f = open("non_existing.txt")
    print(f.read())
except:
    print("The file you want to read does not exist")    
finally:
    f.close()

#  APPEND - create the file if it doesn't exist
f = open("names.txt", "a")
f.write("\nOlakunle")
f.close()

f = open("names.txt" , "r")
print(f.read())

# WRITE - deletes the original content in the file and replace it with new
f = open("context.txt", "w")
f.write("The previous text here have been overwritten!")
f.close()

f = open("context.txt")
print(f.read())

#  TWO WAY TO CREATE A NEW FILE

# Opens a file for writing, creates the file if it doesn't exist
f = open("name_list.txt", "w")
f.close()

# Creates the specified file but returns an error if the file exist.
if not os.path.exists("newFile.txt"):
    f = open("newFile.txt", "x")
    f.close()

# Delete a file

# Avoid an error if it doesn't exist

if os.path.exists("names.txt"):
    os.remove("names.txt")
else:
    print("The file does not exist!")    


# More professional way

with open("morenames.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)