import os

f = open("text.txt", "w")

f.write("Now is the time")
f.write("to close the file")
# print(f)

f.close()

f = open("text.txt", "r")
# f = open("text.ttt", "r") #This returns a FileNotFoundError
print(f)

text = f.read(5)
print(text)

print( f.read(1000006))
print( f.read())


# def copyFile(oldFile, newFile):
#     f1 = open(oldFile, "r")
#     f2 = open(newFile, "w")
#     while True:
#         text = f1.read(50)
#         if text == "":
#             break
#         f2.write(text)
#     f1.close()
#     f2.close()
#     return

# print(copyFile(letter.txt, lettercopy.txt))


f = open("test.dat","w")
f.write("line one\nline two\nline three\n")
f.close()
# The readline method reads all the characters up to and including the next
# newline character:
f = open("test.dat","r")
print(f.readline())
print(f.readline())
print(f.readline())
