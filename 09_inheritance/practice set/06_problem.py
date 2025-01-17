# write __str__() method to print the vector as follow:
#  7i + 8j + 10k

class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __add__(self,c2):
        return vector(self.i + c2.i , c2.j + self.j , c2.k + self.k)
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
a=vector(1,2,3)
c2=vector(1,2,3)
print(a+c2)