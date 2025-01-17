class Employee:
    def __init__(self):
        print("Constructor of Employee:  ")
    a=1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer:  ")
    b=2

class codder(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of codder:  ")
    c=3

o=Employee()
print(o.a)
o=Programmer()
print(o.a,o.b)
o=codder()
print(o.a,o.b,o.c)