#  repeat program 4 for a list of such words to be censered

import os
l=["bura","bad","donkey"]
word=input("Enter the word of replacement: ")
def read_file():
    if not os.path.exists("file.txt"):
        print("this file doesn't exists, re enter the name of file again: ")
    else:
        with open("file.txt") as f:
            content=f.read()
            for item in l:
                content=content.replace(item,word)
            updated_file(content)
def updated_file(content):
    with open("file.txt","w") as f:
        f.write(content)
        print("file is update: ")
read_file()