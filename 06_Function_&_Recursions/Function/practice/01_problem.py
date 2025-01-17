#  write a program to find the greatest of 3 three numbers
def big(a,b,c):
    if(a>b and a>c):
        print(f"the greatest number out of 3 are {a}")
    elif(b>c and b>a):
        print(f"the greatest number out of 3 are {b}")
    else:
        print(f"the greatest number out of 3 are {c}")

print("enter three different numbers: -")
a=int(float(input("enter the first number:- ")))
b=int(float(input("enter the second number:- ")))
c=int(float(input("enter the thired number:- ")))
big(a,b,c)