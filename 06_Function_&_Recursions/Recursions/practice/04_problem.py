#  write a recursive program to find the sum of first n natural numbers

def sum(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return (n+sum(n-1))
a=int(float(input("Enter a number: ")))

if(a<0):
    print("please enter vaild integer: ")
else:
    print(f"sum of first {a} natural numbers are {sum(a)}")