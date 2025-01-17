# write a python program to rename a file to "renamed_by_python.txt"
import os 

old_name=input("enter the old name of the file: ").strip()
new_name=input("Enter what new name you want of your file: ").strip()
os.rename(old_name,new_name)