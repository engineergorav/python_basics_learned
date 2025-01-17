#  create a class (2-d-vector) and use it to create an another class(3-d-vector)

class Two_D_vecor:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show (self):
        return(f"The 2 D Vector is {self.i}i + {self.j}j = {self.i+self.j}")
class Three_D_vector(Two_D_vecor):
    def __init__(self,i,j,k):
        self.k=k
        super().__init__(i,j)
    def shoo(self):
        return(f"The 3 D vector is {self.i}i + {self.j}j + {self.k}k = {self.i+self.j+self.k}")
a=Two_D_vecor(1,2)
b=Three_D_vector(2,4,5)
print(a.show())
print(b.shoo())
