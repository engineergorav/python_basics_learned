# create a class "Programmer" for storing informations of few programers working at microsoft


class Programmer:
    company="Microsoft"
    
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
        print(f"Name of programer is {self.name}\nHis salary is: {self.salary}\nHe lives in area with pin code: {self.pin}")
obj=Programmer("Gorav","7,00,00,000",174201)