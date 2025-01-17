# / write a program to convert inches into cm and vice versa.

def inches_to_centimeter(inche):
    return (inche*2.54)

def centimeter_inches(cm):
    return(cm/2.54)

val=input("type 'cm' to convert into centimeter and type 'in' to convert into inches:   ")

if(val.lower()=="cm"):
    value=float(input("Enter value in INCHES: "))
    n=inches_to_centimeter(value)
    print(f"{value} inche = {round(n,2)} centimeter")

elif(val.lower()=="in"):
    value=float(input("Enter value in CENTIMETER: "))
    n=centimeter_inches(value)
    print(f"{value} centimeter = {round(n,2)} inches")
