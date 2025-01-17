# write a program to print the multiplication table of n till 10

def table(number):
    i=1
    while(i<11):
        print(f"{number} X {i} = {i*number}")
        i+=1
val=int(float(input("enter how many table do you want to print")))

for i in range(0,val):
    value=int(input(" enter the number of which table you want:  "))
    if(value==0):
        print(0)
    table(value)