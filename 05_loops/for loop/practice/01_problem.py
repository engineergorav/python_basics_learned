#  write a program to print a multiplication table of given number

number=int(input("enter a number:  "))
for i in range(1,11):
    print(number,"X",i,"=",number*i)