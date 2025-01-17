# find whether number is prime or not


numb=int(input("enter how many number you want to check::  "))

i=0
while(i<numb):
    number=int(input("enter the number you want to check::  "))
    if(number%2==0):
        print("it is an even number::  ")
        i+=1
    else:
        print("it is an odd number::  ")
        i+=1