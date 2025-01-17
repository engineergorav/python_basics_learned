# calculate the grade of students with the give scheam
# 90-100 == Ex
# 80-90 == A
# 70-80 == B
# 60-70 == C
# 50-60 == D
# <50 == F

marks=int(input("enter marks within 0 to 100: -"))

if(marks>90 and marks<=100):
    print("you have got:   Ex")
elif(marks>80 and marks<=90):
    print("you have got:   A")
elif(marks>70 and marks<=80):
    print("you have got:   B")
elif(marks>60 and marks<=70):
    print("you have got:   C")
elif(marks>50 and marks<=60):
    print("you have got:   D")
else:
    print("you are fail, better luck next time  F")