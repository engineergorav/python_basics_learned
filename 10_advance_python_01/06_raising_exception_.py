a= int(input("enter a number: "))
b=int(input("enter another number: "))
if (b==0):
    raise ZeroDivisionError ("cant devide a by 0:")
else:
    print (int(a/b))