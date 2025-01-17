# store the multiplication table generated in problem 3 in a file name 'Tables.txt'
ans=int(input("enter a number: ").strip())
l1=[i*ans for i in range(1,11)]
print(l1)
with open("Tables.txt","a") as f:
    f.write(str(l1)+"\n")