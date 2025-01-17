# write a program to print the following star pattern 
'''
***
* *
***
'''

n=int(input("enter the number:  "))

for i in range(1,(n+1)):
    if(i%2==0):
        print("*","*")
        
    else:
        print("*"*n)
        
