'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1

'''

def Factorial(n):
    if(n==1 or n==0):
        return 1
    return n*Factorial(n-1)

n=float(input("enter any number:  "))
print(f"the factorial of {n} is {Factorial(n)}")