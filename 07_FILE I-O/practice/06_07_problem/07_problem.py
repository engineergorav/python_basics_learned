# write a program to find out the line no. of the given word in the file
import os 

word=input("Enter the word whose lineyou want ot find: ").strip()
l=[]
def read_file():
    if not os.path.exists("log.txt"):
        print("The given file doesn't exists: ")
    else:
        with open("log.txt","r") as f:
            lines=f.readlines()
            line_no=0
            for line in lines:
                line_no+=1
                if word.lower() in line.lower():
                    l.append(line_no)
                else:
                    pass
            if(len(l)!=0):
                print(f"The word '{word}' is present in the lines {l}")
            else:
                print(f"No the word '{word}' is not present in the given file ")
read_file()
