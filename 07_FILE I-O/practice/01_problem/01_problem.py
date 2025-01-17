# write a program to read a text file and tell which line contains "twinkle" word


with open("poem.txt","r") as f:
    a=f.readlines()
    f.seek(0)
    i=0
    while i<7:
        line=f.readline()
        if "twinkle" in line.lower():
            print("Yes there is twinkle in the line: ")
            i+=1
        else:
            print("No there is no twinkle in this line: ")
            i+=1