#  write a program to greet all the persons names sorted in a list  "l" and which start with S
#  l=["Harry","Soham","Sachin","Rahul"]

l=["Harry","Soham","Sachin","Rahul"]

starting_character="S"

i=0
while(i<len(l)):
    if(l[i].startswith("S")):
        print(f"hello {l[i]}")
        i+=1
    else:
        i+=1