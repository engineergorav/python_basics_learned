# write a program to open three files 1.txt,2.txt,3.txt if any of these files is not present 
# print a message without exiting the program 

try:
    with (open("1.txt","r") as f1,
          open("2.txt","r")as f2,
          open("3.txt","r")as f3):
        pass
except Exception:
    print("no such file is present:")
    
print("thank you")        