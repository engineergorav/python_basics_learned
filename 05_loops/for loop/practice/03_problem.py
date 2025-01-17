# find whether number is prime or not


numb=int(input("enter how many number you want to check::  "))


for i in range(1,(numb+1)):
    number=int(input("enter the number you want to check:  "))
    if(number%2==0):
        print("it is an even number! ")
    else:
        print("it is an odd number!  ")
    