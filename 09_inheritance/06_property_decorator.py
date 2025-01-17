class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")
    @property
    def name(cls):
        print(f"The first name is {cls.fname} \nThe last name is {cls.lname}")
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
o=Employee()
o.a
o.name="Gorav Thakur"
print(o.fname)
