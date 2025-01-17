class Employee:
    company="ITC"
    def show(self,name,salary):
        return(f"the name of the employee is {self.name} and he gets salary around {self.salary}")
class programmer(Employee):
    company="ITC infotech"
    def place(self):
        print(f"they live in the {self.city}")

a=Employee()
b=programmer()
b.salary=1234567
b.name="2nd name"
print(a.company,"\n",b.show(b.name,b.salary))
