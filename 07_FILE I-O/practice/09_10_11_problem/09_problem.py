#  write a program to find out weather a file is identical and matches the content of another file 

import os
def read_file_1_2():
    if not os.path.exists("01_file.txt"):
        print("The give file 01 do not exists: ")
    else:
        with open("01_file.txt","r") as f:
            content_01=f.read()
    if not os.path.exists("02_file.txt"):
        print("The give file 01 do not exists: ")
    else:
        with open("02_file.txt","r") as f:
            content_02=f.read()
    compare(content_01,content_02)
def compare(file_01,file_02):
    if file_01.lower()==file_02.lower():
        print("yes these files are identical: ")
    else:
        print("No these files are not identical: ")
read_file_1_2()