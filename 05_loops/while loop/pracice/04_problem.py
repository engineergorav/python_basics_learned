# write a program to find the sum of first given n numbers using while loop

natural_number=int(input("enter the natural number: "))

sum=0
i=1
while(i<=natural_number):
    sum+=i
    i+=1
print(sum)