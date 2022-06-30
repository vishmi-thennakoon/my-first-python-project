import os
path = input("Input Folder.")
list = os.listdir(path)
for file in list:
    print(file)