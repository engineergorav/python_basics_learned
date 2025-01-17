#  write a program to convert the celcius into feranote and vice versa

def celcius_to_fahrenheit(n):
    return (((9/5)*n)+32)


def fahrenheit_to_celcius(a):
    return ((a-32)*(5/9))


val=input("enter only C if you want ans in celcius and enter only F if you want ans in feranite:  ")

if(val.upper() == "C"):
    value=float(input("enter value in Fahrenheit : "))
    f=fahrenheit_to_celcius(value)
    print(f"{value}°F = {round(f,2)}°C")


elif(val.upper() == "F"):
    value=float(input("enter value in celcius : "))
    c=celcius_to_fahrenheit(value)
    print(f"{value}°C = {round(c,2)}°F")


else:
    print("invalid entery, please enter C or F: ")

