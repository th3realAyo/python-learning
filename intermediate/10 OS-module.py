# Move files around
# Navigate the file system
# Get file information
# Look and change environment variables

import os
from datetime import datetime

# Show all attributes and methods available to the OS module imported
print(dir(os))

# Fetch my current directory/folder
print(f"Previous directory: {os.getcwd()}")

# Change to a new directory/folder
os.chdir('C:/Users/AYO_AYO/Desktop/')
print(f"New directory: {os.getcwd()}")

# See what files are in the desktop/directory 
# NOTE: We can pass a file path in the listdir() but by default, it'll use my current directory
# print(os.listdir())

# Create a new folder on the desktop/directory
folder = 'test_folder'
deep_level_folder = 'main_folder/folder1/folder2'
os.mkdir(folder) # This creates just a single level folder
os.makedirs(deep_level_folder) # This create deep level folder (sub folder(s) in a folder)
print(os.listdir())

# Deleting folders in a directory
os.rmdir(folder)  # This deletes just a single level folder
os.removedirs(deep_level_folder) # This deletes deep level folder (sub folder(s) in a folder)

# Rename a file or folder
os.rename('test_folder', 'nontest_folder')

# Getting the info about a file/folder

mod_time = os.stat('1670777101072.jpg').st_mtime
created_time = os.stat('1670777101072.jpg').st_ctime
accessed_time = os.stat('1670777101072.jpg').st_atime
print(datetime.fromtimestamp(mod_time))
print(datetime.fromtimestamp(created_time))
print(datetime.fromtimestamp(accessed_time))

# print(os.stat('1670777101072.jpg'))

# See the entire directory tree (traverse the directory)
os.chdir("C:/Users/AYO_AYO/Desktop")

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path:', dirpath)
    print('Directories', dirnames)
    print('Files', filenames)
    print()

#Environment Variable
print(os.environ.get('USERPROFILE'))

# print(dir(os.path))

file_path = os.path.join(os.environ.get('USERPROFILE'), 'text.txt')
print(file_path)

# Other Methods Available to OS.PATH
print(os.path.basename(file_path))
print(os.path.dirname(file_path))
print(os.path.split(file_path))
print(os.path.exists(file_path))