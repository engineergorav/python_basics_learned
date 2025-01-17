#  write a class "Calculator" capable of finding square, cude, cube and square roots of the number 

class Calculator:

    @staticmethod
    def square(a):
        return a*a
            
    @staticmethod
    def square_root(a):
        return a**(0.5)
            
    @staticmethod
    def cube(a):
        return a*a*a
            
    @staticmethod
    def cube_root(a):
        return a**(1/3)
obj=Calculator()
while True:
    print("_________")
    print("Chose accordingly:")
    print("1 : to find square of a number ")
    print("2 : to find cube of a number ")
    print("3 : to find square root of a number ")
    print("4 : to find cube root  of a number ")
    print("5 : to exit the calculator")
    print("_________")

    inp=input("enter your choice: ")
    if (inp!="1" and inp!="2" and inp!="3" and inp!="4" and inp!="5"):
        print("your input is not valid, try again! ")
    elif inp=="5":
        print("\nThanks for using the Calculator: ")
        exit()
    else:
        value=float(input("enter the value here: "))
        if value==0:
            print("the answer is 0")
        else:
            if inp=="1":
                print(f"\nSquare  of {value} is: {round(obj.square(value),1)} \n")
            elif inp=="2":
                print(f"\nCube of {value} is: {round(obj.cube(value),1)}\n ")
            elif inp=="3":
                print(f"\nsquare root of {value} is: {round(obj.square_root(value),1)} \n")
            elif inp=="4":
                print(f"\nCube root of {value} is: {round(obj.cube_root(value),1)} \n")
            
            

