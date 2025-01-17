class Employee:
    company="ITC"
    def show(self):
        return(f"The name of the employee is {self.name} and he gets salary around {self.salary}")
    
class codder(Employee):
    language="python"
    def show_language(self):
        return(f"Name of the company is {self.company} and preferable language is {self.language}")
    
class programmer(codder):
    company="ITC infotech"
    def place(self):
        return(f"The company is  in the {self.company}")

a=Employee()
b=programmer()
c=codder()
b.salary=1234567
b.name="Default name"
print(b.show())
print(b.show_language())
print(b.place())
