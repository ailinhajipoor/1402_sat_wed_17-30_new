import os

files_list = os.listdir()
# print(len(files_list))
for i in files_list:
    if i[-4:] == ".txt":
        print(i)
