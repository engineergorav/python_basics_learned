# write a program to print 3rd 5th and 7th element of list by using enumerator
l1=[1,2,3,4,5,6,7,8,9,10]
for i,item in enumerate(l1):
    if i==3 or i==5 or i==7:
        print(f"{i} element of the list is {item}")