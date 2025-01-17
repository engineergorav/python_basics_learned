# write a program to find the factorial of a given number using for loop

fact_number=int(input("enter the number to find factorial:  "))

factorial=1

i=1
while(i<=fact_number):
    factorial*=i
    i+=1
print(factorial)