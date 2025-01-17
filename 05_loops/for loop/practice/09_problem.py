# write a program to print the multiplication table of n in reverse order

n=int(input("enter the number whose table you want :  "))
a=10
for i in range(1,11):
    print(n,"X",a,"=",n*a)
    a-=1