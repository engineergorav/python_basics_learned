# write a program to find the sum of first given n numbers using for loop

natural_number=int(input("enter the natural number: "))

sum=0

for i in range(1,(natural_number+1)):
    sum+=i
print(sum)