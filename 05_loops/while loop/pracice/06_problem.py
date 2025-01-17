#  write a program to print the following star pattern
'''
  *  
 ***
*****
'''
n=int(input("enter the number:  "))
i=1
a=1
while(i<(n+1)):
    print(" "*(n-i)+"*"*a)
    i+=1
    a+=2