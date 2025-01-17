# write a program to display a/b  where a and b are integer. if b==0, display infinite by handling the 'ZeroDivisionError'

try:
    a=int(input("enter 1 number: ").strip()) 
    b=int(input("enter 2 number: ").strip()) 
    print(a/b)
    
except ZeroDivisionError:
    print("ifinite:")
