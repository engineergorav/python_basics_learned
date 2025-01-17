#  write a program to wipe out the content of file using python
import os 
def wipe_file():
    if not os.path.exists("01_file.txt"):
        print("this file doesn't exists")
    else:
        with open("01_file.txt","w")as f:
            f.write("python")
wipe_file()