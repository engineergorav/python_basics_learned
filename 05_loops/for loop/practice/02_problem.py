#  write a program to greet all the persons names sorted in a list  "l" and which start with S
#  l=["Harry","Soham","Sachin","Rahul"]

l=["Harry","Soham","Sachin","Rahul"]

starting_character="S"

for i in l:
    if(i.startswith("S")):
        print(f"hello  {i}")