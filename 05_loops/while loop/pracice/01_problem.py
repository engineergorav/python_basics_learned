#  write a program to print a multiplication table of given number

number=int(input("enter number:  "))

i=1
while(i<11):
    print(number,"X",i,"=",i*number)
    i+=1