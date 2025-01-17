#  pass if every marks is greater than 30 and total percentage is greater than 40 
#  otherwise fail  

m1=int(input("enter the marks 1: "))
m2=int(input("enter the marks 2: "))
m3=int(input("enter the marks 3: "))


total_percentage=((m1+m2+m3)/300)*100


if(total_percentage>=40 and m1>30  and m2>30  and m3>30):
    print("you are pass: ", total_percentage)
else:
    print("you are fail , try next year! ",total_percentage)
