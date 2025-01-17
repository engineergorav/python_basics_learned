# write a program to make a copy of text file "this.txt"

import os

def read_file():
    if not os.path.exists("this.txt"):
        print("This file doesn't exists: ")
    else:
        with open("this.txt","r") as f:
            content=f.read()
            copy_file(content)
def copy_file(content):
    with open("this_copy_file.txt","w") as f:
        f.write(content)
        print("file is copied to another file: ")

read_file()