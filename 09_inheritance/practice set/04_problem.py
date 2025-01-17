# write a class "complex" to represent complex numbers, along with overloaded
# operator '+' and '*' which adds and multiplies them
class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,c2):
        return Complex(self.r + c2.r , self.i + c2.i)
    def __str__(self):
        return f"{self.r} + {self.i}i"

c1=Complex(1,5)
c2=Complex(1,5)
print(f"the complex number sum is {c1+c2}")