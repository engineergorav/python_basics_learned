#  create a class (Employee) and add salary and increment properties to it.
# write a method 'salaryAfterincrement' method with a @property decorator with a setter 
# which changes the value of increment based on salary


class Employee:
    def __init__(self,salary):
        self.selary=salary
    @property
    def salary(self):
        return self.selary
    @salary.setter
    def salary(self,amout):
        if amout<=0:
            raise ValueError("this can't get incremented:")
        self.selary = amout
    def increment(self,amount):
        self.selary+=amount

    
a=Employee(10000)
print(f"the salary is {a.salary}")
a.increment(1000)
print(f"now the salary is {a.salary}")