# write a program to print the multiplication table of n in reverse order

n=int(input("enter the number whose table you want :  "))
i=10
while(i>0):
    print(n,"X",i,"=",n*i)
    i-=1