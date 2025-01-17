#  write a program to print the following star pattern
'''
  *  
 ***
*****
'''
n=int(input("enter the number:  "))
a=1
for i in range(0,(n)):
    print(" "*(n-i),"*"*a)
    a+=2