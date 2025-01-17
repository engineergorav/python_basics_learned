# write a list comprehension to print a list which contains the multiplication table of a use entered number 
ans=int(input("enter a number: ").strip())
l1=[i*ans for i in range(1,11)]
print(l1)