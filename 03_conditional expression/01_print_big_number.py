a=int(input("enter number one:  "))
b=int(input("enter number two:  "))
c=int(input("enter number three:  "))
d=int(input("enter number four:  "))


if(a>b and a>c and a>d ):
    print("greatest number is : ",a)
elif(b>a and b>c and b>d):
    print("greatest number is : ",b)
elif(c>a and c>b and c>d):
    print("greatest number is : ",c)
else:
    print("greatest number is : ",d)