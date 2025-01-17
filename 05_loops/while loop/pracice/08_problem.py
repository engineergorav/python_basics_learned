# write a program to print the following star pattern 
'''
***
* *
***
'''

n=int(input("enter the number:  "))
i=1
while(i<n+1):
    if(i%2==0):
        print("*","*")
        i+=1
    else:
        print("*"*n)
        i+=1