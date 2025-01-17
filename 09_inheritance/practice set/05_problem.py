# Write a class vector representating of n dimensions. Overload the + and * operator which calculates the sum and dot(.)product of them 
class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __add__(self,c2):
        return (self.i + c2.i , self.j + c2.j , self.k + c2.k)
    def __mul__(self,c2):
        return (self.i * c2.i , self.j * c2.j , self.k * c2.k)
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
c1=Vector(1,2,3)
c2=Vector(1,2,3)
print(f"The sum of the vector is {c1 + c2}")
print(f"The dot product of vector is {c1*c2}")