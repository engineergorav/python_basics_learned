# write a program to find the factorial of a given number using for loop

fact_number=int(input("enter the number to find factorial:  "))

factorial=1
for i in range(1,(fact_number+1)):
    factorial*=i
print(factorial)
